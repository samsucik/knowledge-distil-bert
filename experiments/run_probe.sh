#!/bin/bash -u

task=$1
cfg=$2
out_dir=$3

#model_type=embedding_word
model_type=LSTM
#model_dir=$(pwd)/teacher-$task
model_dir=$(pwd)/student-${task}-${model_type}-hard-logits
is_student=true

senteval_path=$PROJECT_DIR/SentEval
glue_data_dir=$GLUE_DIR/$task

pushd $TRANSFORMERS/examples > /dev/null
python probe_model.py \
    --use_word_vectors=true \
    --embed_strategy=avg \
    --layer_to_probe=0 \
    --out_dir=$out_dir \
    --senteval_path=$senteval_path \
    --glue_task=$task \
    --model_type=$model_type \
    --model_dir=$model_dir \
    --is_student=$is_student \
    --glue_data_dir=$glue_data_dir
