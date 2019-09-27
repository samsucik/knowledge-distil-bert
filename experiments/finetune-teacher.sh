#!/bin/bash -u

export TASK_NAME=CoLA
export OUT_DIR=$(pwd)/$TASK_NAME/teacher

pushd $TRANSFORMERS/examples

python run_glue.py \
  --data_dir $GLUE_DIR/$TASK_NAME \
  --model_type bert \
  --model_name_or_path bert-base-uncased \
  --task_name $TASK_NAME \
  --output_dir ${OUT_DIR}/ \
  --do_lower_case \
  --per_gpu_train_batch_size 8 \
  --per_gpu_eval_batch_size 16 \
  --learning_rate 2e-5 \
  --num_train_epochs 1.0 \
  --logging_steps 1 \
  --save_steps -1 \
  --no_cuda \
  --overwrite_output_dir \
  --do_eval \
  --toy_mode \
  --rich_eval \
  # --do_train \
  # --max_steps 1 \
  # --eval_all_checkpoints \


popd
