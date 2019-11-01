#!/bin/bash -u

cache_dir=$PYTORCH_TRANSFORMERS_CACHE
mkdir -p $cache_dir
cd $cache_dir

# BERT large uncased
wget -N https://s3.amazonaws.com/models.huggingface.co/bert/bert-large-uncased-pytorch_model.bin
wget -N https://s3.amazonaws.com/models.huggingface.co/bert/bert-large-uncased-config.json
wget -N https://s3.amazonaws.com/models.huggingface.co/bert/bert-large-uncased-vocab.txt

# BERT base uncased
wget -N https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased-pytorch_model.bin
wget -N https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased-config.json
wget -N https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased-vocab.txt

# GPT-2
wget -N https://s3.amazonaws.com/models.huggingface.co/bert/gpt2-medium-pytorch_model.bin
wget -N https://s3.amazonaws.com/models.huggingface.co/bert/gpt2-medium-config.json
wget -N https://s3.amazonaws.com/models.huggingface.co/bert/gpt2-medium-vocab.json
wget -N https://s3.amazonaws.com/models.huggingface.co/bert/gpt2-medium-merges.txt
