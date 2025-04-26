from source.models.baseline_llm import BaselineLLM

load_model = {
    'baseline_llm': BaselineLLM,
}

# Replace the following with the model paths
get_llm_model_path = {
    'qwen2.5-3b'      : 'Qwen/Qwen2.5-3B-Instruct'                  ,
    'qwen2.5-7b'      : 'Qwen/Qwen2.5-7B-Instruct'                  ,
    'qwen2.5-14b'     : 'Qwen/Qwen2.5-14B-Instruct'                 ,
    'qwen2.5-32b'     : 'Qwen/Qwen2.5-32B-Instruct'                 ,
    'r1-qwen2.5-14b'  : 'deepseek-ai/DeepSeek-R1-Distill-Qwen-14B'  ,
    'r1-qwen2.5-32b'  : 'deepseek-ai/DeepSeek-R1-Distill-Qwen-32B'  ,

    'llama-3.1-8b'    : 'meta-llama/Llama-3.1-8B-Instruct'          ,
    'llama-3.1-70b'   : 'meta-llama/Llama-3.1-70B-Instruct'         ,
    'r1-llama-3.1-8b' : 'deepseek-ai/DeepSeek-R1-Distill-Llama-8B'  ,
    'r1-llama-3.1-70b': 'deepseek-ai/DeepSeek-R1-Distill-Llama-70B' ,
}