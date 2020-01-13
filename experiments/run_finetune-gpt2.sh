#!/bin/bash -u

task=$1 
cfg=$2 # dummy argument, not used here
out_dir=$3

cache_dir=$PYTORCH_TRANSFORMERS_CACHE

export TASK_NAME=$task
export OUT_DIR=$out_dir
mkdir -p $OUT_DIR

echo "GPT-2 FINETUNING STARTING"
pushd $DBERT

# cache the dataset
echo $DATA_AUGMENTATION_DIR_LOCAL
ls -l $DATA_AUGMENTATION_DIR_LOCAL
if [ -d "$DATA_AUGMENTATION_DIR_LOCAL" ] && [ -f "${DATA_AUGMENTATION_DIR_LOCAL}/dataset" ]; then
  echo "Cached dataset exists, not generating it..."
  cached_dataset=${DATA_AUGMENTATION_DIR_LOCAL}/dataset
else
  cached_dataset=$OUT_DIR/dataset
  python -m dbert.generate.cache_datasets \
    --data-dir $GLUE_DIR_LOCAL/$TASK_NAME \
    --output-file $cached_dataset \
    --dataset_name $TASK_NAME
fi

# finetune gpt2
# use train-batch-size of 16 on Letha, on Landonia even 1 is too much
if [ -d "$DATA_AUGMENTATION_DIR_LOCAL" ] && [ -f "${DATA_AUGMENTATION_DIR_LOCAL}/pytorch_model.bin" ]; then
  echo "Finetuned GPT-2 exists, not finetuning it again..."
  finetuned_gpt=$DATA_AUGMENTATION_DIR_LOCAL
else
  finetuned_gpt=$OUT_DIR
  python -m dbert.generate.finetune_gpt \
    --save $finetuned_gpt \
    --cache-file $cached_dataset \
    --train-batch-size 16 \
    --cache-dir "$cache_dir" \
    --gpt2-model "gpt2-medium" \
    --num-train-epochs 1
fi

# sample prefixes
if [ -d "$DATA_AUGMENTATION_DIR_LOCAL" ] && [ -f "${DATA_AUGMENTATION_DIR_LOCAL}/sampled_prefixes" ]; then
  echo "Sampled prefixes found, not sampling again..."
  sampled_prefixes=${DATA_AUGMENTATION_DIR_LOCAL}/sampled_prefixes
else
  sampled_prefixes=$OUT_DIR/sampled_prefixes
  python -m dbert.generate.build_sampler \
    --cache-file $cached_dataset \
    --cache-dir "$cache_dir" \
    --save $sampled_prefixes \
    --model-type "gpt2" \
    --gpt2-model "gpt2-medium"
fi

set -o xtrace
echo "Finetuned GPT: $finetuned_gpt"
# sample sentences
if [ -d "$DATA_AUGMENTATION_DIR_LOCAL" ] && [ -f "${DATA_AUGMENTATION_DIR_LOCAL}/sampled_sentences" ]; then
  echo "Sampled sentences found, not sampling again..."
else
  python -m dbert.generate.sample_gpt \
    --prefix-file $sampled_prefixes \
    --gpt2-model "gpt2-medium" \
    --num-samples 800000 \
    --cache-dir "$cache_dir" \
    --finetuned-model "$finetuned_gpt" \
    > $OUT_DIR/sampled_sentences
fi

echo "GPT-2 FINETUNING FINISHED"
popd
