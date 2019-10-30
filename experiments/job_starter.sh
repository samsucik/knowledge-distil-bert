sbatch \
	--gres=gpu:1 \
	--partition=General_Usage \
	--job-name="sams-test" \
	--no-requeue \
	--output=slurm.out \
	--open-mode=append \
	--time=0-2 \
	--mem=30G \
	gpu.sh
