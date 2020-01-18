#!/bin/bash -u

task=$1 
cfg=$2
out_dir=$3
# teacher_dir=$4

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

# export TASK_NAME=$task
# export TEACHER_DIR=$(pwd)/$teacher_dir
# export DISTIL_DIR=$out_dir
WORD_VECTORS_FILE="GoogleNews-vectors-negative300.txt"
# TRANSFER_SET_TSV=cached_train_augmented-gpt-2_msl128_logits_bilstm.csv

student_type=BERT
score_with_teacher=true
score_with_student=false
trained_model_dir=teacher-$task
source $cfg
trained_model_dir=$(pwd)/$trained_model_dir

echo "###########################################"
echo "student_type: $student_type"
echo "score_with_teacher: $score_with_teacher"
echo "score_with_student: $score_with_student"
echo "trained_model_dir: $trained_model_dir"
echo "###########################################"

echo "DISTILLATION STARTING"
pushd $TRANSFORMERS/examples > /dev/null
python distil_from_finetuned.py \
  --task_name $task \
  --student_type $student_type \
  --score_with_student $score_with_student \
  --score_with_teacher $score_with_teacher \
  --trained_model_dir $trained_model_dir \
  --data_dir $GLUE_DIR/$task \
  --word_vectors_dir $WORD_VECTORS_DIR \
  --word_vectors_file $WORD_VECTORS_FILE \
  --output_dir $out_dir \
  --seed 42 \
  --n_gpu $n_gpu \
  --no_cuda "$no_cuda" \
  --augmentation_type gpt-2 \
  --force
  # --teacher_name $TEACHER_DIR \
  # --transfer_set_tsv $TRANSFER_SET_TSV \
  # --from_pretrained "$from_pretrained" \
  # --do_lower_case \
  # --max_position_embeddings $max_seq_len \
  # --n_layers $n_layers \
  # --n_heads $n_heads \
  # --dim $dim \
  # --hidden_dim $hidden_dim \
  # --dropout $dropout \
  # --attention_dropout $attention_dropout \
  # --use_hard_labels $use_hard_labels \
  # --temperature $temperature \
  # --alpha_mse $alpha_mse \
  # --alpha_ce $alpha_ce \
  # --n_epochs $n_epochs \
  # --batch_size $batch_size \
  # --per_gpu_eval_batch_size 64 \
  # --gradient_accumulation_steps $gradient_accumulation_steps \
  # --warmup_epochs $warmup_epochs \
  # --lr_decay $lr_decay \
  # --weight_decay $weight_decay \
  # --optimizer $optimizer \
  # --learning_rate $learning_rate \
  # --max_grad_norm $max_grad_norm \
  # --initializer_range 0.02  \
  # --log_interval $log_interval \
  # --evaluate_during_training \
  # --rich_eval \
  # --log_examples \
  # --checkpoint_interval $checkpoint_interval \
  # --augmentation_data_file $augmentation_data_file \
  # --use_word_vectors $use_word_vectors \
  # --token_embeddings_from_teacher $token_embeddings_from_teacher \
  # --token_type_embedding_dimensionality $token_type_embedding_dimensionality \
  # --token_embedding_dimensionality $token_embedding_dimensionality \
  # --max_steps $max_steps
  # --toy_mode \

popd > /dev/null
echo "DISTILLATION FINISHED"
