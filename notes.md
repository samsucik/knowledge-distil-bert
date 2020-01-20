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
	- Adadelta (1.0) #4:	distil-bert-CoLA-Jan17-10:37:31_FCN
	- Adadelta (1.0) #5:	distil-bert-CoLA-Jan17-10:50:42_FCN
	- Adadelta (1.0) #6:	distil-bert-CoLA-Jan17-10:50:57_FCN

	- Adam (5e-4) #1: 		distil-bert-CoLA-Jan15-16:22:30_FCN
	- Adam (5e-4) #2: 		distil-bert-CoLA-Jan15-16:23:14_FCN
	- Adam (5e-4) #3: 		distil-bert-CoLA-Jan15-16:23:19_FCN
	- Adam (5e-4) #4:		distil-bert-CoLA-Jan17-10:52:11_FCN
	- Adam (5e-4) #5:		distil-bert-CoLA-Jan17-10:52:18_FCN
	- Adam (5e-4) #6:		distil-bert-CoLA-Jan17-10:52:27_FCN

	- Adam (5e-3) #1: 		distil-bert-CoLA-Jan15-16:29:04_FCN
	- Adam (5e-3) #2: 		distil-bert-CoLA-Jan15-16:29:34_FCN
	- Adam (5e-3) #3: 		distil-bert-CoLA-Jan15-16:29:47_FCN
	- Adam (5e-3) #4:		distil-bert-CoLA-Jan17-10:54:16_FCN
	- Adam (5e-3) #5:		distil-bert-CoLA-Jan17-10:54:23_FCN
	- Adam (5e-3) #6:		distil-bert-CoLA-Jan17-10:54:33_FCN

	- Adam (5e-5) #1: 		distil-bert-CoLA-Jan15-16:41:24_FCN
	- Adam (5e-5) #2: 		distil-bert-CoLA-Jan15-16:42:04_FCN
	- Adam (5e-5) #3: 		distil-bert-CoLA-Jan15-23:38:24_FCN
	- Adam (5e-5) #4:		distil-bert-CoLA-Jan17-10:56:16_FCN
	- Adam (5e-5) #5:		distil-bert-CoLA-Jan17-10:56:24_FCN
	- Adam (5e-5) #6:		distil-bert-CoLA-Jan17-14:43:55_FCN

	- Adam (5e-6) #1: 		distil-bert-CoLA-Jan15-16:44:39_FCN
	- Adam (5e-6) #2: 		distil-bert-CoLA-Jan15-16:44:47_FCN
	- Adam (5e-6) #3: 		distil-bert-CoLA-Jan15-16:44:58_FCN
	- Adam (5e-6) #4:		distil-bert-CoLA-Jan17-10:58:03_FCN
	- Adam (5e-6) #5:		distil-bert-CoLA-Jan17-10:58:09_FCN
	- Adam (5e-6) #6:		distil-bert-CoLA-Jan17-10:58:17_FCN

	- Adam (1.5e-4) #1: 	distil-bert-CoLA-Jan16-00:45:07_FCN
	- Adam (1.5e-4) #2: 	distil-bert-CoLA-Jan16-00:45:12_FCN
	- Adam (1.5e-4) #3: 	distil-bert-CoLA-Jan16-09:09:56_FCN
	- Adam (1.5e-4) #4:		distil-bert-CoLA-Jan17-11:05:05_FCN
	- Adam (1.5e-4) #5:		distil-bert-CoLA-Jan17-11:06:22_FCN
	- Adam (1.5e-4) #6:		distil-bert-CoLA-Jan17-11:06:30_FCN

	- Adam (1.5e-5) #1: 	distil-bert-CoLA-Jan16-00:47:07_FCN
	- Adam (1.5e-5) #2: 	distil-bert-CoLA-Jan16-00:47:12_FCN
	- Adam (1.5e-5) #3: 	distil-bert-CoLA-Jan16-00:47:30_FCN
	- Adam (1.5e-5) #4:		distil-bert-CoLA-Jan17-11:09:40_FCN
	- Adam (1.5e-5) #5:		distil-bert-CoLA-Jan17-11:10:08_FCN
	- Adam (1.5e-5) #6:		distil-bert-CoLA-Jan17-11:10:18_FCN

	- Adam (1.5e-3) #1: 	distil-bert-CoLA-Jan16-09:37:40_FCN
	- Adam (1.5e-3) #2: 	distil-bert-CoLA-Jan16-09:37:45_FCN
	- Adam (1.5e-3) #3: 	distil-bert-CoLA-Jan16-09:37:49_FCN
	- Adam (1.5e-3) #4:		distil-bert-CoLA-Jan17-15:27:46_FCN
	- Adam (1.5e-3) #5:		distil-bert-CoLA-Jan17-14:31:49_FCN
	- Adam (1.5e-3) #6:		distil-bert-CoLA-Jan17-14:32:57_FCN
#### Batch size
	- 32 #1:	distil-bert-CoLA-Jan17-23:27:02_FCN
	- 32 #2:	distil-bert-CoLA-Jan17-23:27:26_FCN
	- 32 #3:	distil-bert-CoLA-Jan17-23:27:48_FCN

	- 128 #1:	distil-bert-CoLA-Jan17-23:28:55_FCN
	- 128 #2:	distil-bert-CoLA-Jan17-23:29:37_FCN
	- 128 #3:	distil-bert-CoLA-Jan17-23:30:35_FCN

	- 256 #1:	distil-bert-CoLA-Jan17-23:32:15_FCN
	- 256 #2:	distil-bert-CoLA-Jan17-23:32:39_FCN
	- 256 #3:	distil-bert-CoLA-Jan17-23:33:03_FCN

	- 512 #1:	distil-bert-CoLA-Jan17-23:36:20_FCN
	- 512 #2:	distil-bert-CoLA-Jan17-23:36:28_FCN
	- 512 #3:	distil-bert-CoLA-Jan17-23:36:39_FCN
#### Warmup proportion & lr decay
	- wp=0, decay #1:		distil-bert-CoLA-Jan18-12:47:13_FCN
	- wp=0, decay #2:		distil-bert-CoLA-Jan18-12:19:11_FCN
	- wp=0, decay #3:		distil-bert-CoLA-Jan18-12:19:25_FCN

	- wp=5, decay #1:		distil-bert-CoLA-Jan18-12:21:09_FCN
	- wp=5, decay #2:		distil-bert-CoLA-Jan18-12:22:01_FCN
	- wp=5, decay #3:		distil-bert-CoLA-Jan18-12:22:39_FCN

	- wp=5, no decay #1:	distil-bert-CoLA-Jan18-12:23:19_FCN
	- wp=5, no decay #2:	distil-bert-CoLA-Jan18-12:38:36_FCN
	- wp=5, no decay #3:	distil-bert-CoLA-Jan18-12:38:46_FCN

	- wp=10, decay #1:		distil-bert-CoLA-Jan18-12:28:34_FCN
	- wp=10, decay #2:		distil-bert-CoLA-Jan18-12:28:54_FCN
	- wp=10, decay #3:		distil-bert-CoLA-Jan18-17:39:44_FC

	- wp=10, no decay #1:	distil-bert-CoLA-Jan18-17:40:29_FC
	- wp=10, no decay #2:	distil-bert-CoLA-Jan18-17:40:44_FC
	- wp=10, no decay #3:	distil-bert-CoLA-Jan18-17:41:16_FC

	- wp=15, decay #1:		distil-bert-CoLA-Jan18-17:42:14_FC
	- wp=15, decay #2:		distil-bert-CoLA-Jan18-17:42:42_FC
	- wp=15, decay #3:		distil-bert-CoLA-Jan18-17:45:26_FC

	- wp=15, no decay #1:	distil-bert-CoLA-Jan18-17:45:54_FC
	- wp=15, no decay #2:	distil-bert-CoLA-Jan18-18:06:13_FC
	- wp=15, no decay #3:	distil-bert-CoLA-Jan18-18:09:09_FC
#### Embedding type
	- wordpiece #1:				distil-bert-CoLA-Jan19-00:12:33_FC
	- wordpiece #2:				distil-bert-CoLA-Jan19-00:26:47_FC
	- wordpiece #3:				distil-bert-CoLA-Jan19-00:27:35_FC

	- wordpiece non-static #1:	distil-bert-CoLA-Jan19-00:25:02_FC
	- wordpiece non-static #2:	distil-bert-CoLA-Jan19-00:25:12_FC
	- wordpiece non-static #3:	distil-bert-CoLA-Jan19-00:25:57_FC
#### Model size
	- LSTM=600, FC=800 #1:		distil-bert-CoLA-Jan20-14:21:21
	- LSTM=600, FC=800 #2:		distil-bert-CoLA-Jan20-14:21:43
	- LSTM=600, FC=800 #3:		distil-bert-CoLA-Jan20-14:22:13
	- LSTM=900, FC=1200 #1:		distil-bert-CoLA-Jan20-14:23:57
	- LSTM=900, FC=1200 #2:		distil-bert-CoLA-Jan20-14:24:18
	- LSTM=900, FC=1200 #3:		distil-bert-CoLA-Jan20-14:24:46
	- LSTM=1200, FC=1600 #1:	distil-bert-CoLA-Jan20-14:26:20
	- LSTM=1200, FC=1600 #2:	distil-bert-CoLA-Jan20-14:26:51
	- LSTM=1200, FC=1600 #3:	distil-bert-CoLA-Jan20-14:27:11
	- LSTM=1500, FC=2000 #1:	distil-bert-CoLA-Jan20-14:29:13
	- LSTM=1500, FC=2000 #2:	distil-bert-CoLA-Jan20-14:29:30
	- LSTM=1500, FC=2000 #3:	distil-bert-CoLA-Jan20-14:29:47

### BERT
#### Learning rate
	<!-- - 5e-3 #1:		distil-bert-CoLA-Jan17-16:10:06_FCN -->
	<!-- - 1.5e-3 #1:	distil-bert-CoLA-Jan17-15:57:10_FCN -->
	<!-- - 5e-4 #1:		distil-bert-CoLA-Jan17-16:10:36_FCN -->
	<!-- - 1.5e-4 #1:	distil-bert-CoLA-Jan17-16:12:47_FCN -->
	<!-- - 5e-5 #1:		distil-bert-CoLA-Jan17-16:13:14_FCN -->
	<!-- - 1.5e-5 #1:	distil-bert-CoLA-Jan17-16:19:46_FCN -->
	<!-- - 5e-6 #1:		distil-bert-CoLA-Jan17-16:14:33_FCN -->
	- 5e-3 #1:			distil-bert-CoLA-Jan20-14:43:09
	- 1.5e-3 #1:		distil-bert-CoLA-Jan20-14:50:44
	- 5e-4 #1:			distil-bert-CoLA-Jan20-14:43:45
	- 1.5e-4 #1:		distil-bert-CoLA-Jan20-14:51:15
	- 5e-5 #1:			distil-bert-CoLA-Jan20-14:44:29
	- 1.5e-5 #1:		distil-bert-CoLA-Jan20-14:52:15
	- 5e-6 #1:			distil-bert-CoLA-Jan20-14:46:00
#### Warmup proportion & lr decay
	<!-- - wp=0, decay #1:		distil-bert-CoLA-Jan18-11:57:08_FC -->
	<!-- - wp=0, no decay #1:	distil-bert-CoLA-Jan18-11:57:42_FC -->
	<!-- - wp=5, decay #1:		distil-bert-CoLA-Jan18-11:58:22_FC -->
	<!-- - wp=5, no decay #1:	distil-bert-CoLA-Jan18-11:59:07_FC -->
	<!-- - wp=10, no decay #1:	distil-bert-CoLA-Jan18-12:08:07_FC -->
	<!-- - wp=15, decay #1:		distil-bert-CoLA-Jan18-11:59:56_FC -->
	<!-- - wp=15, no decay #1:	distil-bert-CoLA-Jan18-12:00:26_FC -->
	<!-- - wp=20, decay #1:		distil-bert-CoLA-Jan18-12:02:52_FC -->
	<!-- - wp=20, no decay #1:	distil-bert-CoLA-Jan18-12:12:15_FC -->
#### Batch size
	<!-- - 32:	distil-bert-CoLA-Jan19-10:04:57_FCN -->
	<!-- - 64:	distil-bert-CoLA-Jan19-10:05:42_FCN -->
	<!-- - 128:	distil-bert-CoLA-Jan19-10:06:41_FCN -->
	<!-- - 512:	doesn't fit into memory -->
	<!-- - 362:	distil-bert-CoLA-Jan19-11:09:55_FCN -->
#### Embedding type
	- word:
	- word (multichannel):

Letha
1:....
2:...
3:..
4:...
5:..
6:..
Damnii
1:
2:..
3:.. NO SPACE
4:....
5:.
6:..
7:..
8:..
10:.
11:....
0.05009791535310399

```bash 
dirs="distil-bert-CoLA-Jan19-10:04:57 distil-bert-CoLA-Jan19-10:05:42 distil-bert-CoLA-Jan19-10:06:41 distil-bert-CoLA-Jan19-11:09:55"
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

### Student sizes
BERT
large: L=24 H=1024 A=16 I=4096
/12:   L=2  H=85   A=1  I=341  (183K)
/6:    L=4  H=171  A=3  I=683  (1.44M)
/5:    L=5  H=204  A=3  I=819  (2.56M) [with I=750 is 2.42M]
BiLSTM
Tang: H=300 FC=400 (2.41M)


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
