#!/usr/bin/env python3


from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline
from huggingface_hub import login
import transformers
import torch

import joblib 



print ("Logging in...")
login(token="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")


model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"

print ("Creating the models...")
summarizer = transformers.pipeline("summarization")


print ("saving the models...")
# Saving the models 
joblib.dump(summarizer, "summarizer.joblib") 
joblib.dump(translator, 'translator_en_to_id.joblib')