import torch
from llmtune.llms.opt.config import (
    OPT7B4BitConfig,
    OPT13B4BitConfig,
    OPT7B3BitConfig,    
    OPT13B3BitConfig    
)
from llmtune.llms.llama.config import (
    LLama7B4BitConfig, 
    LLama13B4BitConfig, 
    LLama30B4BitConfig, 
    LLama65B4BitConfig,
    LLama7B3BitConfig,
    LLama13B3BitConfig,
    LLama30B3BitConfig,
    LLama65B3BitConfig,
    LLama7B2BitConfig, 
    LLama65B2BitConfig,
)
from llmtune.engine.lora.config import FinetuneConfig

# ----------------------------------------------------------------------------

# define some constants
DEV = torch.device('cuda')
LLAMA_MODELS = [
    "llama-7b-4bit", "llama-13b-4bit", "llama-30b-4bit", "llama-65b-4bit",
    "llama-7b-3bit", "llama-13b-3bit", "llama-30b-3bit", "llama-65b-3bit",
    "llama-7b-2bit", "llama-65b-2bit", 
]
OPT_MODELS  = [
    "opt-6.7b-4bit", "opt-13b-4bit",
    "opt-6.7b-3bit", "opt-13b-3bit",
]
LLM_MODELS = LLAMA_MODELS + OPT_MODELS

# define some helpers
def get_llm_config(model):
    if model == "llama-7b-4bit":
        return LLama7B4BitConfig
    elif model == "llama-13b-4bit":
        return LLama13B4BitConfig
    elif model == "llama-30b-4bit":
        return LLama30B4BitConfig
    elif model == "llama-65b-4bit":
        return LLama65B4BitConfig
    elif model == "llama-7b-3bit":
        return LLama7B3BitConfig 
    elif model == "llama-13b-3bit":
        return LLama13B3BitConfig 
    elif model == "llama-30b-3bit":
        return LLama30B3BitConfig 
    elif model == "llama-65b-3bit":
        return LLama65B3BitConfig             
    elif model == "llama-7b-2bit":
        return LLama7B2BitConfig 
    elif model == "llama-65b-2bit":
        return LLama65B2BitConfig            
    elif model == "opt-6.7b-4bit":
        return OPT7B4BitConfig      
    elif model == "opt-13b-4bit":
        return OPT13B4BitConfig
    elif model == "opt-6.7b-3bit":
        return OPT7B3BitConfig      
    elif model == "opt-13b-3bit":
        return OPT13B3BitConfig
    else:
        raise ValueError(f"Invalid model name: {model}")

# ----------------------------------------------------------------------------

# helpers for loading finetuning configs
def get_finetune_config(args):
    return FinetuneConfig(
        dataset=args.dataset, 
        ds_type=args.data_type, 
        lora_out_dir=args.adapter, 
        mbatch_size=args.mbatch_size,
        batch_size=args.batch_size,
        epochs=args.epochs, 
        lr=args.lr,
        cutoff_len=args.cutoff_len,
        lora_r=args.lora_r, 
        lora_alpha=args.lora_alpha, 
        lora_dropout=args.lora_dropout,
        val_set_size=args.val_set_size,
        warmup_steps=args.warmup_steps,
        save_steps=args.save_steps,
        save_total_limit=args.save_total_limit,
        logging_steps=args.logging_steps,
    )
