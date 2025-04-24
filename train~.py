import os
import tqdm
import torch
from torch.utils.data import DataLoader
from datasets import Dataset

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import warnings; warnings.filterwarnings("ignore")

from source.utils.help_funcs import seed_everything
from source.config import parse_args_llm
from source.utils.help_funcs import _save_checkpoint, _reload_model
from source.models import load_model, get_llm_model_path
from source.datasets import load_dataset
from source.utils.evaluation import *
from source.utils.help_funcs import collate_fn

def main(args):
    seed = args.seed
    seed_everything(seed=seed)
    os.environ["WANDB_PROJECT"]=f"{args.project}~"

    # Step 1: Build Dataset
    train_dataset = load_dataset[args.dataset](path = args.path, data = args.data, split = "test", 
        hit_thres = args.hit_thres, use_DB = True
    )
    train_dataset = Dataset.from_list(train_dataset)

    # Step 2: Build Model and Optimizer
    args.llm_model_path = get_llm_model_path[args.llm_model_name]
    model = load_model[args.model_name](args=args)
    trainable_params, all_param = model.print_trainable_params()
    print("-"*len(f"No. Trainable Params: {trainable_params} ({100 * trainable_params / all_param:.4f} %)"))
    print(f"No. Trainable Params: {trainable_params} ({100 * trainable_params / all_param:.4f} %)")
    params = [p for _, p in model.named_parameters() if p.requires_grad]
    optimizer = torch.optim.Adam(
        [{'params': params, 'lr': args.lr, 'weight_decay': args.wd}],
        betas=(0.9, 0.999)
    )
    lr_scheduler = torch.optim.lr_scheduler.LambdaLR(
        optimizer, 
        lr_lambda=lambda cur_step: (1 - cur_step / len(train_dataset)) * (1 - 0.5) + 0.5, 
    )
    if args.checkpoint_path is not None:
        model = _reload_model(model, args.checkpoint_path)

    # Step 3.0: Build Reward Functions
    def is_met_reward(completions, **kwargs):
        rewards = []
        for completion, label, data, hit_thres in zip(completions, kwargs["smiles"], kwargs["data"], kwargs["hit_thres"]):
            rewards.append(
                is_met(completion, label, data, 
                       hit_thres = hit_thres, 
                )[1]
            )
        return rewards

    # Step 3: Training
    from trl import GRPOConfig, GRPOTrainer
    config = GRPOConfig(
        bf16=True,
        # gradient_checkpointing=True,
        # gradient_accumulation_steps=4,
        num_train_epochs=1,
        per_device_train_batch_size=24,

        report_to="wandb",
        run_name=f"{args.model_name}_lora_r{args.lora_r}_{args.llm_model_name}_{args.run_name}_{args.hit_thres}",
        logging_strategy="steps",
        logging_steps=1,
    )

    config.save_strategy = "no"
    trainer = GRPOTrainer(
        train_dataset=train_dataset,
        model=model.model,
        optimizers=(
            optimizer, lr_scheduler
        ),
        reward_funcs=is_met_reward,
        args=config,
    )
    trainer.train()

    _save_checkpoint(model, 1, args, is_best=True)

if __name__ == "__main__":
    args = parse_args_llm().parse_args()
    main(args)