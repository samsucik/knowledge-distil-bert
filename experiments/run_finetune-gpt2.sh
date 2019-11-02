#!/bin/bash -u

task=$1 
cfg=$2
out_dir=$3

# if [[ $(nvidia-smi -L) =~ "GPU" ]]
# then
#     echo "Some GPUs found."
#     n_gpu=1
#     no_cuda="False"
# else
#     echo "No GPUs found."
#     n_gpu=0
#     no_cuda="True"
# fi

# max_seq_len=128
# n_epoch=3
# train_batch_size=32
# learning_rate=5e-5
# warmup_proportion=0.1
# model_name_or_path=bert-large-uncased
# gradient_accumulation_steps=1
# logging_steps=50

# source $cfg

cache_dir=$PYTORCH_TRANSFORMERS_CACHE

# echo "###########################################"
# echo "max_seq_len: $max_seq_len"
# echo "model_name_or_path: $model_name_or_path"
# echo "n_epoch: $n_epoch"
# echo "train_batch_size: $train_batch_size"
# echo "learning_rate: $learning_rate"
# echo "warmup_proportion: $warmup_proportion"
# echo "gradient_accumulation_steps: $gradient_accumulation_steps"
# echo "logging_steps: $logging_steps"
# echo "###########################################"

# exit 0

export TASK_NAME=$task
export OUT_DIR=$out_dir

echo "GPT-2 FINETUNING STARTING"
pushd $DBERT

# cache the dataset
#python -m dbert.generate.cache_datasets \
#  --data-dir $GLUE_DIR_LOCAL/$TASK_NAME \
#  --output-file $OUT_DIR/dataset \
#  --dataset_name $TASK_NAME

# finetune gpt2
python -m dbert.generate.finetune_gpt \
  --save $OUT_DIR/pytorch_model.bin \
  --cache-file $OUT_DIR/dataset \
  --train-batch-size 16 \
  --cache-dir "$cache_dir" \
  --gpt2-model "gpt2-medium" \
  --num-train-epochs 1
exit 0
# sample prefixes
python -m dbert.generate.build_sampler \
  --cache-file $OUT_DIR/dataset \
  --save $OUT_DIR/sampled_prefixes \
  --model-type gpt2

# sample sentences
python -m dbert.generate.sample_gpt \
  --prefix-file $OUT_DIR/sampled_prefixes \
  > $OUT_DIR/sampled_sentences

echo "GPT-2 FINETUNING FINISHED"
popd

# python run_glue.py \
#   --data_dir $GLUE_DIR_LOCAL/$TASK_NAME \
#   --model_type bert \
#   --model_name_or_path $model_name_or_path \
#   --cache_dir "$cache_dir" \
#   --task_name $TASK_NAME \
#   --output_dir ${OUT_DIR}/ \
#   --do_lower_case \
#   --per_gpu_train_batch_size $train_batch_size \
#   --per_gpu_eval_batch_size 64 \
#   --max_seq_length $max_seq_len \
#   --gradient_accumulation_steps $gradient_accumulation_steps \
#   --learning_rate $learning_rate \
#   --warmup_proportion $warmup_proportion \
#   --num_train_epochs $n_epoch \
#   --logging_steps $logging_steps \
#   --save_steps -1 \
#   --overwrite_output_dir \
#   --do_eval \
#   --do_train \
#   --evaluate_during_training \
#   --rich_eval \
#   --log_examples \
# #  --no_cuda \
# #  --max_steps 7 \
# #  --toy_mode \
# #  --eval_all_checkpoints \

# popd
