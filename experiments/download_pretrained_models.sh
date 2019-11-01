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

