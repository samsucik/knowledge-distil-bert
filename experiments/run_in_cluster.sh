#!/bin/bash -u

stage=$1
task=$2
config=$3
out_dir=$4
teacher_dir=$5
interactive=$6

echo "'${stage}' '${task}' '${config}' '${out_dir}' '${teacher_dir}'"

# create scratch disk space and set up paths
hostname
ls -l /disk
ls -l /disk/scratch
nvidia-smi
SPACE=/disk/scratch/s1513472
mkdir -p $SPACE/data
export GLUE_DIR_LOCAL=${SPACE}/data/glue_data
DATA_AUGMENTATION_DIR=$(pwd)/data_augmentation-${task}
export DATA_AUGMENTATION_DIR_LOCAL=${SPACE}/data_augmentation-${task}
OUT_DIR=$SPACE/$out_dir
mkdir -p $OUT_DIR

# copy data to scratch disk
rsync -az ${GLUE_DIR}/ $GLUE_DIR_LOCAL
if [ "$stage" == "finetune-gpt2" ] && [ -d "$DATA_AUGMENTATION_DIR" ]; then
  rsync -az ${DATA_AUGMENTATION_DIR}/ $DATA_AUGMENTATION_DIR_LOCAL
fi
echo $GLUE_DIR_LOCAL
ls -l $GLUE_DIR_LOCAL/CoLA

# do computation
./run_${stage}.sh "${task}" "${config}" "${OUT_DIR}" "${teacher_dir}"

if [ "$interactive" != "true" ]; then
  # copy results back to distributed FS
  rsync -az $OUT_DIR $(pwd)

  # destroy the scratch disk space
  #rm -rf $OUT_DIR
  rm -rf $SPACE/*
fi
