#!/bin/bash -u

if [[ $(hostname -s) =~ ^(greekie|uhtred)$ ]]; then
	echo "I am in the cluster"
	pwd=/mnt/mscteach_home/s1513472/minfp2
	export PYTORCH_TRANSFORMERS_CACHE=/mnt/mscteach_home/s1513472/.cache/torch/pytorch_transformers
else
	echo "I am in a DICE or other PC"
	pwd=$(pwd)
fi

export GLUE_DIR=$pwd/data/glue_data
export TRANSFORMERS=$pwd/pytorch-transformers
export DICE=/afs/inf.ed.ac.uk/user/s15/s1513472
