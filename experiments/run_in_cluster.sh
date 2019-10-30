#!/bin/bash -u

stage=$1
task=$2
config=$3
teacher_dir=$4

echo "'${stage}' '${task}' '${config}' '${teacher_dir}'"

# create scratch disk space and set up paths
mkdir -p /disk/scratch/s1513472
SPACE=/disk/scratch/s1513472
mkdir -p $SPACE/data
GLUE_DIR_LOCAL=${SPACE}/data/glue_data
TGT_DIR=$SPACE/slurm-${SLURM_JOB_NAME}-${SLURM_JOB_ID}
mkdir -p $TGT_DIR
OUT_F=$TGT_DIR/out.txt
touch $OUT_F

# copy data to scratch disk
rsync -az ${GLUE_DIR}/ $GLUE_DIR_LOCAL

# do computation
nvidia-smi >> $OUT_F
hostname >> $OUT_F
head $GLUE_DIR_LOCAL/CoLA/test.tsv >> $OUT_F
echo $TRANSFORMERS >> $OUT_F
echo $GLUE_DIR >> $OUT_F

# copy results back to distributed FS
rsync -az $TGT_DIR $(pwd)

# destroy the scratch disk space
rm -rf $SPACE/*
