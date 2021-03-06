echo -e "\nUsage: $0 distil-bert --config=student-configs/third.cfg --task=CoLA --teacher-dir=CoLA/teacher\n"

# defaults
stage=distil-bert
task=CoLA
config=student-configs/small.cfg
teacher_dir=teacher-$task

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

dt=$(date '+%b%d-%H:%M:%S')
out_dir=$stage-$task-$dt
interactive=false

if [[ $(hostname -s) =~ ^(greekie|uhtred)$ ]]; then
  nodelist=damnii07
  partition=PGR-Standard
  timelimit="7-0"
  
  nodelist=letha01
  partition=General_Usage
  timelimit="3-8"

  source $PROJECT_DIR/path.sh "$nodelist"
  echo "Project directory in cluster node ${nodelist}: ${PROJECT_DIR}"
  sbatch \
    --gres=gpu:1 \
    --partition=$partition \
    --nodelist=$nodelist \
    --job-name=$stage \
    --no-requeue \
    --output=${out_dir}.out \
    --open-mode=truncate \
    --time=$timelimit \
    --mem=30G \
    run_in_cluster.sh "${stage}" "${task}" "${config}" "${out_dir}" "${teacher_dir}" "${interactive}"
else
  echo "Running locally."
  export GLUE_DIR_LOCAL=$GLUE_DIR
  if [[ $stage == finetune* ]]; then
    export DATA_AUGMENTATION_DIR_LOCAL=$(pwd)/data_augmentation-${task}
    mkdir -p $DATA_AUGMENTATION_DIR_LOCAL
  fi
  mkdir -p $(pwd)/${out_dir}
  # here, config and teacher_dir are irrelevant in running GPT-2 finetuning
  ./run_${stage}.sh "${task}" "${config}" "$(pwd)/${out_dir}" "${teacher_dir}" #&> ${out_dir}.out
fi
