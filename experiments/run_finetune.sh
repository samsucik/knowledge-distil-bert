#!/bin/bash -u

task=$1 
cfg=$2
out_dir=$3

if [[ $(nvidia-smi -L) =~ "GPU" ]]
then
    echo "Some GPUs found."
    n_gpu=1
    no_cuda="False"
else
    echo "No GPUs found."
    n_gpu=0
    no_cuda="True"
fi

max_seq_len=128
model_name_or_path=bert-large-uncased

source $cfg

echo "###########################################"
echo "max_seq_len: $max_seq_len"
echo "model_name_or_path: $model_name_or_path"
echo "###########################################"

exit 0

export TASK_NAME=$task
export OUT_DIR=$out_dir

echo "TEACHER FINETUNING STARTING"
pushd $TRANSFORMERS/examples
python run_glue.py \
  --data_dir $GLUE_DIR/$TASK_NAME \
  --model_type bert \
  --model_name_or_path $model_name_or_path \
  --task_name $TASK_NAME \
  --output_dir ${OUT_DIR}/ \
  --do_lower_case \
  --per_gpu_train_batch_size 16 \
  --per_gpu_eval_batch_size 64 \
  --max_seq_length $max_seq_len \
  --gradient_accumulation_steps 2 \
  --learning_rate 2e-5 \
  --num_train_epochs 6 \
  --logging_steps 32 \
  --save_steps -1 \
  --overwrite_output_dir \
  --do_eval \
  --do_train \
  --evaluate_during_training \
  --rich_eval \
  --log_examples \
  --no_cuda \
  --max_steps 7 \
  --toy_mode \
  --eval_all_checkpoints \

popd
echo "TEACHER FINETUNING FINISHED"
