# Description: Building an LLM from scratch

# Import the necessary packages
import numpy as np
import pandas as pd
import torch
import os
import re

# Pre-processing the data
print(os.getcwd())

# Load the data
with open('the_verdict.txt', 'r') as f:
    raw_text = f.read()

print("Total number of character:", len(raw_text))
# print(raw_text[:99])

# Tokenize the data
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print('The number of tokens are: ' + str(len(preprocessed)))
# print(preprocessed[:30])

# Getting the vocabulary size
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print('The size of the vocab is: ' + str(vocab_size))
vocab = {token:integer for integer,token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break


class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}
    def encode(self, text):
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [
        item.strip() for item in preprocessed if item.strip()
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text