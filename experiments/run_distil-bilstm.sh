#!/bin/bash -u

task=$1 
cfg=$2
out_dir=$3
teacher_dir=$4

TASK_NAME=$task
TRANSFER_SET_FILE=cached_train_augmented-gpt-2_msl128_logits_bilstm.csv
# TRANSFER_SET_FILE=train.tsv
WORD_VECTORS_FILE="GoogleNews-vectors-negative300.txt"

TASK_NAME_LC=$(echo "$TASK_NAME" | awk '{print tolower($0)}')

if [[ $(nvidia-smi -L 2>/dev/null) =~ "GPU" ]]
then
    echo "Some GPUs found."
    device="cuda:0"
else
    echo "No GPUs found."
    device="cpu"
fi

pushd $DBERT > /dev/null
python -m dbert.distill.run.distill_birnn \
	--config confs/birnn_${TASK_NAME_LC}.json \
	--device $device \
	--workspace $out_dir \
	--dataset_path $GLUE_DIR_LOCAL/$TASK_NAME \
	--vectors_dir $WORD_VECTORS_DIR \
	--vectors_file $WORD_VECTORS_FILE \
	--train_file $TRANSFER_SET_FILE \
	--dev_file "dev.tsv" \
	--lr 1.5e-4 \
	--distill_lambda 1.0 \
	--epochs 30 \
	--batch_size 128 \
	--mode "multichannel" \
	--optimizer "adam" \
	--warmup_prop 0.1 \
	--logits_path "" \
	--ce_lambda 0.0 \
	--n_feature_maps 0 \
	--output_channel 0 \
	--weight_decay 0.0
	# --eval_test_only

popd > /dev/null

# {'dataset_path': '/mnt/nvme/glue/CoLA', 
# 'dataset_name': 'cola', 
# 'vectors_file': 'GoogleNews-vectors-negative300.txt', 
# 'vectors_dir': '/mnt/nvme/Castor-data/embeddings/word2vec', 
# 'train_file': 'train-gpt2.tsv', 
# 'dev_file': 'dev.tsv', 
# 'test_file': 'test.tsv',

# 'distill_lambda': 1, 
# 'distill_temperature': 3, 
# 'ce_lambda': 1, 
# 'seed': 0, 
# 'workspace': 'local_workspace', 
# 'batch_size': 50, 
# 'optimizer': 'adam', 
# 'epochs': 30, 
# 'early_stop': True, 
# 'lr': 0.0005, 
# 'device': 'cuda:0', 
# 'use_data_parallel': False, 
# 'load_last_checkpoint': False, 
# 'load_best_checkpoint': False, 
# 'eval_test_only': False, 
# 'export_eval_labels': False, 
# 'use_maxpool': False, 
# 'float_score': False, 
# 'output_channel': 100, 
# 'words_dim': 300, 
# 'clip_grad': 30000, 
# 'dropout': 0.1, 
# 'n_feature_maps': 200, 
# 'rnn_type': 'lstm', 
# 'hidden_size': 300, 
# 'fc_size': 400, 
# 'weight_decay': 0.001, 
# 'mode': 'rand'}
