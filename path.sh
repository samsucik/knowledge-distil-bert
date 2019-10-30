#!/bin/bash -u

if [[ $(hostname -s) =~ ^(greekie|uhtred)$ ]]; then
	echo "I am in the cluster"
	pwd=/mnt/mscteach_home/s1513472/minfp2
else
	echo "I am in a DICE or other PC"
	pwd=$(pwd)
fi

export GLUE_DIR=$pwd/data/glue_data
export TRANSFORMERS=$pwd/pytorch-transformers
