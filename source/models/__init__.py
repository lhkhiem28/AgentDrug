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
    'gemma-3-1b'      : 'google/gemma-3-1b-it'                      ,
    'gemma-3-4b'      : 'google/gemma-3-4b-it'                      ,
    'gemma-3-12b'     : 'google/gemma-3-12b-it'                     ,
    'gemma-3-27b'     : 'google/gemma-3-27b-it'                     ,

    'llama-3.1-8b'    : 'meta-llama/Llama-3.1-8B-Instruct'          ,
    'llama-3.1-70b'   : 'meta-llama/Llama-3.1-70B-Instruct'         ,
}