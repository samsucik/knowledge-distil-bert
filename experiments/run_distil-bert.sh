#!/bin/bash -u

task=$1 
cfg=$2
out_dir=$3
teacher_dir=$4

if [[ $(nvidia-smi -L 2>/dev/null) =~ "GPU" ]]
then
    echo "Some GPUs found."
    n_gpu=1
    no_cuda="False"
else
    echo "No GPUs found."
    n_gpu=0
    no_cuda="True"
fi

export TASK_NAME=$task
export TEACHER_DIR=$(pwd)/$teacher_dir
export DISTIL_DIR=$out_dir
WORD_VECTORS_FILE="GoogleNews-vectors-negative300.txt"
TRANSFER_SET_TSV=cached_train_augmented-gpt-2_msl128_logits_bilstm.csv

student_type=BERT
mode=non-static
optimizer=adam
learning_rate=5e-6
dropout=0.1
attention_dropout=0.1
max_seq_len=128
n_layers=3
n_heads=4
dim=256
hidden_dim=1024
use_hard_labels=false
batch_size=32
gradient_accumulation_steps=2
max_grad_norm=5.0
temperature=2.0
alpha_mse=0.0
alpha_ce=1.0
n_epochs=250
warmup_epochs=0.0
lr_decay=false
weight_decay=0.0
max_steps=-1
from_pretrained=none
checkpoint_interval=25
log_interval=128
augmentation_data_file="$(pwd)/data_augmentation-${TASK_NAME}/sampled_sentences"
token_embeddings_from_teacher=false
token_type_embedding_dimensionality=$hidden_dim
token_embedding_dimensionality=$hidden_dim
use_word_vectors=false
source $cfg

echo "###########################################"
echo "student_type: $student_type"
echo "mode: $mode"
echo "optimizer: $optimizer"
echo "learning_rate: $learning_rate"
echo "dropout: $dropout"
echo "attention_dropout: $attention_dropout"
echo "n_heads: $n_heads"
echo "n_layers: $n_layers"
echo "dim: $dim"
echo "hidden_dim: $hidden_dim"
echo "max_seq_len: $max_seq_len"
echo "use_hard_labels: $use_hard_labels"
echo "batch_size: $batch_size"
echo "gradient_accumulation_steps: $gradient_accumulation_steps"
echo "max_grad_norm: $max_grad_norm"
echo "temperature: $temperature"
echo "alpha_mse: $alpha_mse"
echo "alpha_ce: $alpha_ce"
echo "n_epochs: $n_epochs"
echo "warmup_epochs: $warmup_epochs"
echo "lr_decay: $lr_decay"
echo "weight_decay: $weight_decay"
echo "max_steps: $max_steps"
echo "from_pretrained: $from_pretrained"
echo "checkpoint_interval: $checkpoint_interval"
echo "log_interval: $log_interval"
echo "augmentation_data_file: $augmentation_data_file"
echo "token_embeddings_from_teacher: $token_embeddings_from_teacher"
echo "token_type_embedding_dimensionality: $token_type_embedding_dimensionality"
echo "token_embedding_dimensionality: $token_embedding_dimensionality"
echo "use_word_vectors: $use_word_vectors"
echo "###########################################"

echo "DISTILLATION STARTING"
pushd $TRANSFORMERS/examples > /dev/null
python distil_from_finetuned.py \
  --student_type $student_type \
  --mode $mode \
  --data_dir $GLUE_DIR/$TASK_NAME \
  --word_vectors_dir $WORD_VECTORS_DIR \
  --word_vectors_file $WORD_VECTORS_FILE \
  --transfer_set_tsv $TRANSFER_SET_TSV \
  --output_dir $DISTIL_DIR \
  --force \
  --from_pretrained "$from_pretrained" \
  --task_name $TASK_NAME \
  --do_lower_case \
  --max_position_embeddings $max_seq_len \
  --n_layers $n_layers \
  --n_heads $n_heads \
  --dim $dim \
  --hidden_dim $hidden_dim \
  --dropout $dropout \
  --attention_dropout $attention_dropout \
  --teacher_name $TEACHER_DIR \
  --use_hard_labels $use_hard_labels \
  --temperature $temperature \
  --alpha_mse $alpha_mse \
  --alpha_ce $alpha_ce \
  --n_epochs $n_epochs \
  --batch_size $batch_size \
  --per_gpu_eval_batch_size 64 \
  --gradient_accumulation_steps $gradient_accumulation_steps \
  --warmup_epochs $warmup_epochs \
  --lr_decay $lr_decay \
  --weight_decay $weight_decay \
  --optimizer $optimizer \
  --learning_rate $learning_rate \
  --max_grad_norm $max_grad_norm \
  --initializer_range 0.02  \
  --n_gpu $n_gpu \
  --seed 42 \
  --log_interval $log_interval \
  --no_cuda "$no_cuda" \
  --evaluate_during_training \
  --rich_eval \
  --log_examples \
  --checkpoint_interval $checkpoint_interval \
  --augmentation_data_file $augmentation_data_file \
  --augmentation_type gpt-2 \
  --use_word_vectors $use_word_vectors \
  --token_embeddings_from_teacher $token_embeddings_from_teacher \
  --token_type_embedding_dimensionality $token_type_embedding_dimensionality \
  --token_embedding_dimensionality $token_embedding_dimensionality \
  --max_steps $max_steps
  # --toy_mode \

popd > /dev/null
echo "DISTILLATION FINISHED"
