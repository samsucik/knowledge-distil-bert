#!/bin/bash -u

task=$1
cfg=$2
out_dir=$3

model_type=LSTM
model_dir=$(pwd)/good-student-lstm-new
is_student=true

model_type=pretrained
model_dir=$(pwd)/teacher-$task
is_student=false

senteval_path=$PROJECT_DIR/SentEval
glue_data_dir=$GLUE_DIR/$task

pushd $TRANSFORMERS/examples > /dev/null
python probe_model.py \
    --embed_strategy=avg \
    --layer_to_probe=5 \
    --out_dir=$out_dir \
    --senteval_path=$senteval_path \
    --glue_task=$task \
    --model_type=$model_type \
    --model_dir=$model_dir \
    --is_student=$is_student \
    --glue_data_dir=$glue_data_dir
