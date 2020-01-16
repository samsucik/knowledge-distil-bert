# Random notes

## TO DO
	# longer training
	# teach student directly on hard labels
	# use student that is pre-trained BERT
	# use student that is full-size re-initialised BERT
	# scan through Sara data and note everything that needs to be removed

## GPU DICEs
- kirby
- mario
- luigi
- zelda

## Setting up environment in the cluster (or elsewhere)
```bash
mkdir minfp2
cd minfp2/
git init
git remote add origin git@github.com:samsucik/knowledge-distil-bert.git
git pull origin master
git submodule update --init --recursive
git pull --recurse-submodules origin master
conda env create -f environment.yml
source activate minfp2
pip install -e pytorch-transformers
cd data
python download_glue_data.py --tasks "CoLA"
cd ../experiments
```
Add `alias minfp='cd ~/minfp2; source activate minfp2; source path.sh'` to .bashrc/.profile

## Longjobbing on DICE
nohup './run.sh' &> nohup.log &
(echo 'UseTheRule99!' | nohup longjob -28day -c 'nice ./run.sh' ) &
(echo 'UseTheRule99!' | nohup longjob -28day -c 'nice ./run.sh student-configs/third.cfg' ) &
(echo 'UseTheRule99!' | nohup longjob -28day -c 'nice ./job_starter.sh finetune-gpt2 --config=teacher-configs/large.cfg' ) &
(echo 'UseTheRule99!' | nohup longjob -28day -c 'nice ./job_starter.sh distil-bert --config=student-configs/third.cfg --teacher-dir=teacher-CoLA' ) &
cp -r CoLA/distillation/tensorboard/
cp -r CoLA/teacher/tensorboard/

## About cluster nodes

landonia[02,19], letha03, has /disk/scratch

### GPU mem
- damnii[01,12]: 12GB
- damnii[02-11]: ????
- letha05: NO GPU
- letha[03,06]: 12GB
- letha[01,02,04]: ????
- landonia[01,03,25]: 6.4GB
- landonia[04-10,12-17,19-20,22-24]: ???? (doesn't permit interactive jobs)
- landonia[02,18]: ???? (doesn't permit interactive jobs)
- landonia[11,21]: ???? (doesn't permit interactive jobs)


## Interactive jobs in the cluster
```bash
stage=finetune-gpt2
task=CoLA
config=config=student-configs/third.cfg
dt=$(date '+%b%d-%H:%M:%S')
out_dir=$stage-$task-$dt
teacher_dir=
interactive=true
./run_in_cluster.sh "${stage}" "${task}" "${config}" "${out_dir}" "${teacher_dir}" "${interactive}"
```

## Finetuning GPT-2
Differences to be implemented if new pytorchtransformers code is to be used for finetuning (instead of the code from d-bert):
```
GPT-2 config

weight_decay=1e-3
correct_bias (in AdamW): False
```
## Runtimes (and minimising them)
Parallelised sampling of 800K sents (MSL=128) from GPT-2 medium on CoLA with 4 GPUs (each with 6GB of memory) and 20GB RAM took 16:39h.
Parallelised generating logits with large BERT for 800K sents (MSL=128, in batches of 2048) on 4 GPUs (12GB memory each) took 1:10h.

## Sizes
BERT (small):
	trainable parameters (all): 32771074 (32.7M)
	trainable parameters (embeddings): 31650560 (31.6M)
	non-embedding prameters: 1120514 (1.1M)
BiLSTM
	trainable parameters (all): 75354902 (75M)
	trainable parameters (embeddings): 72948900 (73M)
	all parameters: 148303802 (148M)
	non-embedding prameters: 2406002 (2.4M)

## Hparam search
### BiLSTM
#### Learning algorithm
- Adadelta (1.0) #1: 	distil-bert-CoLA-Jan16-00:37:42_FCN
- Adadelta (1.0) #2: 	distil-bert-CoLA-Jan16-00:37:50_FCN
- Adadelta (1.0) #3: 	distil-bert-CoLA-Jan16-00:37:58_FCN

- Adam (5e-4) #1: 		distil-bert-CoLA-Jan15-16:22:30_FCN
- Adam (5e-4) #2: 		distil-bert-CoLA-Jan15-16:23:14_FCN
- Adam (5e-4) #3: 		distil-bert-CoLA-Jan15-16:23:19_FCN

- Adam (5e-3) #1: 		distil-bert-CoLA-Jan15-16:29:04_FCN
- Adam (5e-3) #2: 		distil-bert-CoLA-Jan15-16:29:34_FCN
- Adam (5e-3) #3: 		distil-bert-CoLA-Jan15-16:29:47_FCN

- Adam (5e-5) #1: 		distil-bert-CoLA-Jan15-16:41:24_FCN
- Adam (5e-5) #2: 		distil-bert-CoLA-Jan15-16:42:04_FCN
- Adam (5e-5) #3: 		distil-bert-CoLA-Jan15-23:38:24_FCN

- Adam (5e-6) #1: 		distil-bert-CoLA-Jan15-16:44:39_FCN
- Adam (5e-6) #2: 		distil-bert-CoLA-Jan15-16:44:47_FCN
- Adam (5e-6) #3: 		distil-bert-CoLA-Jan15-16:44:58_FCN

- Adam (1.5e-4) #1: 	distil-bert-CoLA-Jan16-00:45:07_FCN
- Adam (1.5e-4) #2: 	distil-bert-CoLA-Jan16-00:45:12_FCN
- Adam (1.5e-4) #3: 	distil-bert-CoLA-Jan16-09:09:56

- Adam (1.5e-5) #1: 	distil-bert-CoLA-Jan16-00:47:07_FCN
- Adam (1.5e-5) #2: 	distil-bert-CoLA-Jan16-00:47:12_FCN
- Adam (1.5e-5) #3: 	distil-bert-CoLA-Jan16-00:47:30_FCN

- Adam (1.5e-3) #1: 	distil-bert-CoLA-Jan16-09:37:40
- Adam (1.5e-3) #2: 	distil-bert-CoLA-Jan16-09:37:45
- Adam (1.5e-3) #3: 	distil-bert-CoLA-Jan16-09:37:49

```bash
dirs=""
for d in $dirs; do
  echo $d
  pushd $d
  rm ./pytorch_*
  rm training_args.bin
  popd
  cp -r $d $DICE/minfp2.bak
  rm ${d}.out
done
```

### BERT



BERT
	<B=256,w=0.1>
	<B=256,w=0>
	<B=64,w=0.1>
	<B=128,w=0.1>
	<B=256,w=0.2>
	<B=256,w=0.1, lr=1.5e-4>
	<B=256, w=0.1, lr=1.5e-3>
	B=128, w=0.1, lr=5e-4, correct linear
	B=128, w=0.1, lr=5e-4, correct linear (third=2.2M)
	B=256, w=0.1, lr=5e-4, correct linear
	B=256, w=0.1, lr=5e-4, correct linear (third=2.2M)
BiLSTM
	<B=128, w=0, lr=5e-4>
	<B=50, w=0.1, lr=5e-4>
	<B=50, w=0.333, lr=5e-4>
	<B=64, w=0, lr=5e-4>


Iteration:   0%|          | 34/16172 [00:01<13:45, 19.56it/s]Traceback (most recent call last):
  File "distil_from_finetuned.py", line 739, in <module>
    main()
  File "distil_from_finetuned.py", line 735, in main
    distiller.train()
  File "/mnt/glusterfs/teaching-home/s1513472/minfp2/pytorch-transformers/examples/distillation/distiller_from_finetuned.py", line 168, in train
    self.step(batch)
  File "/mnt/glusterfs/teaching-home/s1513472/minfp2/pytorch-transformers/examples/distillation/distiller_from_finetuned.py", line 239, in step
    self.optimize(loss)
  File "/mnt/glusterfs/teaching-home/s1513472/minfp2/pytorch-transformers/examples/distillation/distiller_from_finetuned.py", line 256, in optimize
    loss.backward()
  File "/mnt/glusterfs/teaching-home/s1513472/.miniconda/envs/minfp2/lib/python3.7/site-packages/torch/tensor.py", line 118, in backward
    torch.autograd.backward(self, gradient, retain_graph, create_graph)
  File "/mnt/glusterfs/teaching-home/s1513472/.miniconda/envs/minfp2/lib/python3.7/site-packages/torch/autograd/__init__.py", line 93, in backward
    allow_unreachable=True)  # allow_unreachable flag
RuntimeError: merge_sort: failed to synchronize: an illegal memory access was encountered
