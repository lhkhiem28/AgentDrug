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
    'gemma-2-2b'      : 'google/gemma-2-2b-it'                      ,
    'gemma-2-9b'      : 'google/gemma-2-9b-it'                      ,
    'gemma-2-27b'     : 'google/gemma-2-27b-it'                     ,
}