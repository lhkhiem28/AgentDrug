# AgentDrug

Datasets: https://huggingface.co/datasets/lhkhiem28/AgentDrug-datasets

---

# AgentDrug: Utilizing Large Language Models in an Agentic Workflow for Zero-Shot Molecular Optimization

EMNLP '25 Findings

[![Paper](https://img.shields.io/badge/Paper-arXiv:2410.13147-red?logoWidth=40)](https://arxiv.org/abs/2410.13147)
[![Datasets](https://img.shields.io/badge/Dataset-Hugging_Face-yellow?logoWidth=40)](https://huggingface.co/datasets/lhkhiem28/AgentDrug-datasets)

## Requirements
```python
rdkit==2025.3.3
torch==2.7.1
transformers==4.53.0
autogen==0.9.4
```

## Quick start

## Reproducibility

### 1. Datasets
Download datasets from the above link and place the folder in the master directory:
```
├───AgentDrug
│   ├───autogen
│   └───source
├───AgentDrug-datasets
│   └───ZINC500
```

### 2. Run
Use the `inference.sh` script with the following arguments to reproduce our main results (Table 2):
- `llm_name`: LLM name
- `data`: path to the set of input molecules (`single/multi`/`property`/`+/-`)
- `refine`: refinement method (`are2df` for AgentDrug)
- `refine_steps`: number of refinement steps
- `hit_thres`: threshold (`l`: loose or `s`: strict)
- `DB_size`: size of the database for retrieval

Examples are provided in `*.job` files.

## Citation
```
@article{le2024utilizing,
  title={AgentDrug: Utilizing Large Language Models in an Agentic Workflow for Zero-Shot Molecular Optimization},
  author={Khiem Le and Ting Hua and Nitesh V. Chawla},
  journal={arXiv preprint arXiv:2410.13147},
  year={2024}
}
```