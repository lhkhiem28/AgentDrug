from source.models.baseline_llm import BaselineLLM

load_model = {
    'baseline_llm': BaselineLLM,
}

# Replace the following with the model paths
get_llm_path = {
    'qwen2.5-3b'      : 'Qwen/Qwen2.5-3B-Instruct'                  ,
    'qwen2.5-7b'      : 'Qwen/Qwen2.5-7B-Instruct'                  ,

    'llama-3.1-8b'    : 'meta-llama/Llama-3.1-8B-Instruct'          ,
    'llama-3.1-70b'   : 'meta-llama/Llama-3.1-70B-Instruct'         ,

    'olmo-2-7b-sft'   : 'allenai/OLMo-2-1124-7B-SFT'                ,
    'olmo-2-7b-dpo'   : 'allenai/OLMo-2-1124-7B-DPO'                ,
    'olmo-2-7b'       : 'allenai/OLMo-2-1124-7B-Instruct'           ,
    'olmo-2-13b-sft'  : 'allenai/OLMo-2-1124-13B-SFT'               ,
    'olmo-2-13b-dpo'  : 'allenai/OLMo-2-1124-13B-DPO'               ,
    'olmo-2-13b'      : 'allenai/OLMo-2-1124-13B-Instruct'          ,
}