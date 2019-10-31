echo -e "\nUsage: $0 distil-bert --config=student-configs/third.cfg --task=CoLA --teacher-dir=CoLA/teacher\n"

# defaults
stage=distil-bert
task=CoLA
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
    shift
    ;;
    -t=*|--task=*)
    task="${i#*=}"
    shift
    ;;
    -d=*|--teacher-dir=*)
    teacher_dir="${i#*=}"
    shift
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

dt=$(date '+%b%d-%H:%M:%S')
out_dir=$stage-$task-$dt

if [[ $(hostname -s) =~ ^(greekie|uhtred)$ ]]; then
  sbatch \
    --gres=gpu:1 \
    --partition=General_Usage \
    --job-name=$stage \
    --no-requeue \
    --output=${out_dir}.out \
    --open-mode=truncate \
    --time=0-4 \
    --mem=30G \
    run_in_cluster.sh "${stage}" "${task}" "${config}" "${out_dir}" "${teacher_dir}"
else
  echo "Running locally."
  ./run_${stage}.sh "${task}" "${config}" "$(pwd)/${out_dir}" "${teacher_dir}" &> ${out_dir}.out
fi
