#!/bin/bash -u

# set -o xtrace

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

export TASK_NAME=CoLA
export OUT_DIR=$(pwd)/$TASK_NAME/teacher

echo "TEACHER FINETUNING STARTING"
pushd $TRANSFORMERS/examples
python run_glue.py \
  --data_dir $GLUE_DIR/$TASK_NAME \
  --model_type bert \
  --model_name_or_path bert-base-uncased \
  --task_name $TASK_NAME \
  --output_dir ${OUT_DIR}/ \
  --do_lower_case \
  --per_gpu_train_batch_size 32 \
  --per_gpu_eval_batch_size 64 \
  --gradient_accumulation_steps 1 \
  --learning_rate 2e-5 \
  --num_train_epochs 6 \
  --logging_steps 32 \
  --save_steps -1 \
  --overwrite_output_dir \
  --do_eval \
  --do_train \
  --evaluate_during_training \
  --rich_eval \
  # --log_examples \
  # --no_cuda \
  # --max_steps 7 \
  # --toy_mode \
  # --eval_all_checkpoints \

popd
echo "TEACHER FINETUNING FINISHED"
exit 0

export TEACHER_DIR=${OUT_DIR}
export DISTIL_DIR=$(pwd)/$TASK_NAME/distillation

echo "DISTILLATION STARTING"
pushd $TRANSFORMERS/examples
python distil_from_finetuned.py \
  --data_dir $GLUE_DIR/$TASK_NAME \
  --output_dir $DISTIL_DIR \
  --force \
  --task_name $TASK_NAME \
  --do_lower_case \
  --max_position_embeddings 512 \
  --n_layers 3 \
  --n_heads 4 \
  --dim 256 \
  --hidden_dim 1024 \
  --dropout 0.1 \
  --attention_dropout 0.1 \
  --teacher_name $TEACHER_DIR \
  --temperature 2.0 \
  --n_epoch 150 \
  --batch_size 32 \
  --per_gpu_eval_batch_size 64 \
  --gradient_accumulation_steps 2 \
  --warmup_prop 0.1 \
  --weight_decay 0.0 \
  --learning_rate 2e-5 \
  --max_grad_norm 5.0 \
  --initializer_range 0.02  \
  --n_gpu $n_gpu \
  --seed 42 \
  --log_interval 64 \
  --no_cuda "$no_cuda" \
  --evaluate_during_training \
  --rich_eval \
  # --log_examples \
  # --checkpoint_interval 200 \
  # --max_steps 10 \
  # --toy_mode \

popd
echo "DISTILLATION FINISHED"

