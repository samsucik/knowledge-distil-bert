#!/bin/bash -u

TASK_NAME=CoLA
python $DBERT/dbert/distill/run/join_logits.py \
	--logits_file $GLUE_DIR/$TASK_NAME/cached_train_augmented-gpt-2_msl128_logits \
    --n_logits 2 \
    --dataset_file $GLUE_DIR/$TASK_NAME/train.tsv \
    --augmentation_file data_augmentation-$TASK_NAME/sampled_sentences \
    --format "tsv" \
    --output_file $GLUE_DIR/$TASK_NAME/cached_train_augmented-gpt-2_msl128_logits_bilstm.csv \
    --dataset_name $TASK_NAME
