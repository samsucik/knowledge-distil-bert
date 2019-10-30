#!/bin/bash -u

stage=$1
task=$2
config=$3
out_dir=$4
teacher_dir=$5

echo "'${stage}' '${task}' '${config}' '${out_dir}' '${teacher_dir}'"

# create scratch disk space and set up paths
SPACE=/disk/scratch/s1513472
mkdir -p $SPACE/data
GLUE_DIR_LOCAL=${SPACE}/data/glue_data
OUT_DIR=$SPACE/$out_dir
mkdir -p $OUT_DIR

# copy data to scratch disk
rsync -az ${GLUE_DIR}/ $GLUE_DIR_LOCAL

# do computation
./run_${stage}.sh "${task}" "${config}" "${OUT_DIR}" "${teacher_dir}"

# copy results back to distributed FS
rsync -az $OUT_DIR $(pwd)

# destroy the scratch disk space
rm -rf $SPACE/*
