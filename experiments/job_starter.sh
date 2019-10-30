echo -e "\nUsage: $0 distil --config=student-configs/third.cfg --task=cola --teacher-dir=CoLA/teacher\n"

# defaults
stage=distil
task=cola
config=student-configs/third.cfg
teacher_dir=

if [ "$#" -ge 1 ]; then
  stage=$1
  shift
fi

for i in "$@"
do
case $i in
    -c=*|--config=*)
    config="${i#*=}"
    shift # past argument=value
    ;;
    -t=*|--task=*)
    task="${i#*=}"
    shift # past argument=value
    ;;
    -d=*|--teacher-dir=*)
    teacher_dir="${i#*=}"
    shift # past argument=value
    ;;
    *)
	echo "Unknown option: $i"
    ;;
esac
done

echo "stage: $stage"
echo "task: $task"
echo "config: $config"
echo "teacher-dir: $teacher_dir"

# exit 0

if [[ $(hostname -s) =~ ^(greekie|uhtred)$ ]]; then
  sbatch \
    --gres=gpu:1 \
    --partition=General_Usage \
    --job-name=$stage \
    --no-requeue \
    --output=slurm.out \
    --open-mode=append \
    --time=0-2 \
    --mem=30G \
    run_in_cluster.sh "${stage}" "${task}" "${config}" "${teacher_dir}"
else
  echo "Running locally."
  ./run_${stage}.sh "${stage}" "${task}" "${config}" "${teacher_dir}"
fi
