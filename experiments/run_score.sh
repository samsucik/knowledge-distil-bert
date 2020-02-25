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

student_type=BERT
score_with_teacher=true
score_with_student=false
# trained_model_dir=best-models/student-$task-$student_type
trained_model_dir=teacher-$task
teacher_dir=teacher-$task
source $cfg
trained_model_dir=$(pwd)/$trained_model_dir

TEACHER_DIR=$(pwd)/$teacher_dir
WORD_VECTORS_FILE="GoogleNews-vectors-negative300.txt"

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
  --teacher_name $TEACHER_DIR \
  --n_gpu $n_gpu \
  --no_cuda "$no_cuda" \
  --force

popd > /dev/null
echo "DISTILLATION FINISHED"
