#!/bin/bash -u

cluster_node=$1

if [[ $(hostname -s) =~ ^(greekie|uhtred)$ ]]; then
	echo "I am in the cluster"
	if [[ ( "$cluster_node" = "landonia21" ) || ( "$cluster_node" = "letha03" )  || ( "$cluster_node" = "" ) ]]; then
		home_dir=/mnt/glusterfs/teaching-home
		export PATH=$home_dir/s1513472/.miniconda/envs/minfp2/bin:$PATH
	else
		home_dir=/mnt/mscteach_home
	fi
	pwd=$home_dir/s1513472/minfp2
	export PYTORCH_TRANSFORMERS_CACHE=$home_dir/s1513472/.cache/torch/pytorch_transformers
else
	echo "I am in a DICE or other PC"
	pwd=$(pwd)
	export PYTORCH_TRANSFORMERS_CACHE=~/.cache/torch/pytorch_transformers
fi

export PROJECT_DIR=$pwd
export DATA_DIR=$pwd/data
export GLUE_DIR=$DATA_DIR/glue_data
export TRANSFORMERS=$pwd/pytorch-transformers
export DICE=/afs/inf.ed.ac.uk/user/s15/s1513472
export DBERT=$pwd/d-bert
export WORD_VECTORS_DIR=$pwd/data/word_vectors
export PYTHONPATH=$TRANSFORMERS:$DBERT:$PYTHONPATH
