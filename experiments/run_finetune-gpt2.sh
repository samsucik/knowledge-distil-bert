#!/bin/bash -u

task=$1 
cfg=$2
out_dir=$3

cache_dir=$PYTORCH_TRANSFORMERS_CACHE

export TASK_NAME=$task
export OUT_DIR=$out_dir

echo "GPT-2 FINETUNING STARTING"
pushd $DBERT

# cache the dataset
echo $DATA_AUGMENTATION_DIR_LOCAL
ls -l $DATA_AUGMENTATION_DIR_LOCAL
if [ -d "$DATA_AUGMENTATION_DIR_LOCAL" ] && [ -f "${DATA_AUGMENTATION_DIR_LOCAL}/dataset" ]; then
  echo "Cached dataset exists, not generating it..."
else
  python -m dbert.generate.cache_datasets \
    --data-dir $GLUE_DIR_LOCAL/$TASK_NAME \
    --output-file $OUT_DIR/dataset \
    --dataset_name $TASK_NAME
fi

# finetune gpt2
# use train-batch-size of 16 on Letha, on Landonia even 1 is too much
if [ -d "$DATA_AUGMENTATION_DIR_LOCAL" ] && [ -f "${DATA_AUGMENTATION_DIR_LOCAL}/pytorch_model.bin" ]; then
  echo "Finetuned GPT-2 exists, not finetuning it again..."
else
  python -m dbert.generate.finetune_gpt \
    --save $OUT_DIR/pytorch_model.bin \
    --cache-file $OUT_DIR/dataset \
    --train-batch-size 16 \
    --cache-dir "$cache_dir" \
    --gpt2-model "gpt2-medium" \
    --num-train-epochs 1
fi

# sample prefixes
if [ -d "$DATA_AUGMENTATION_DIR_LOCAL" ] && [ -f "${DATA_AUGMENTATION_DIR_LOCAL}/sampled_prefixes" ]; then
  echo "Sampled prefixes found, not sampling again..."
else
  python -m dbert.generate.build_sampler \
    --cache-file $OUT_DIR/dataset \
    --cache-dir "$cache_dir" \
    --save "$OUT_DIR/sampled_prefixes" \
    --model-type "gpt2" \
    --gpt2-model "gpt2-medium"
fi

# sample sentences
if [ -d "$DATA_AUGMENTATION_DIR_LOCAL" ] && [ -f "${DATA_AUGMENTATION_DIR_LOCAL}/sampled_sentences" ]; then
  echo "Sampled sentences found, not sampling again..."
else
  python -m dbert.generate.sample_gpt \
    --prefix-file $OUT_DIR/sampled_prefixes \
    --gpt2-model "gpt2-medium" \
    --num-samples 800000 \
    --cache-dir "$cache_dir" \
    > $OUT_DIR/sampled_sentences
fi

echo "GPT-2 FINETUNING FINISHED"
popd
