# Random notes

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

## Student sizes
### BERT
	theory
	- large: L=24 H=1024 A=16 I=4096
	- /12:   L=2  H=85   A=1  I=341  (183K)
	- /6:    L=4  H=171  A=3  I=683  (1.44M)
	- /5:    L=5  H=204  A=3  I=819  (2.56M) [with I=750 is 2.42M]

	practice
	- 2.42M: L=5 H=204 A=3 I=750
	- inflating: width up to 4x, depth up to 3x
### BiLSTM
	Tang: H=300 FC=400 (2.41M)

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
	- wp=10, decay #3:		distil-bert-CoLA-Jan18-17:39:44_FCN

	- wp=10, no decay #1:	distil-bert-CoLA-Jan18-17:40:29_FCN
	- wp=10, no decay #2:	distil-bert-CoLA-Jan18-17:40:44_FCN
	- wp=10, no decay #3:	distil-bert-CoLA-Jan18-17:41:16_FCN

	- wp=15, decay #1:		distil-bert-CoLA-Jan18-17:42:14_FCN
	- wp=15, decay #2:		distil-bert-CoLA-Jan18-17:42:42_FCN
	- wp=15, decay #3:		distil-bert-CoLA-Jan18-17:45:26_FCN

	- wp=15, no decay #1:	distil-bert-CoLA-Jan18-17:45:54_FCN
	- wp=15, no decay #2:	distil-bert-CoLA-Jan18-18:06:13_FCN
	- wp=15, no decay #3:	distil-bert-CoLA-Jan18-18:09:09_FCN
#### Embedding type (CoLA)
	- wordpiece #1:				distil-bert-CoLA-Jan19-00:12:33_FCN
	- wordpiece #2:				distil-bert-CoLA-Jan19-00:26:47_FCN
	- wordpiece #3:				distil-bert-CoLA-Jan19-00:27:35_FCN

	- wordpiece non-static #1:	distil-bert-CoLA-Jan19-00:25:02_FCN
	- wordpiece non-static #2:	distil-bert-CoLA-Jan19-00:25:12_FCN
	- wordpiece non-static #3:	distil-bert-CoLA-Jan19-00:25:57_FCN

	- word non-static #1:		distil-bert-CoLA-Jan25-09:40:14_FCN
	- word non-static #2:		distil-bert-CoLA-Jan25-09:40:18_FCN
	- word non-static #3:		distil-bert-CoLA-Jan25-09:40:23_FCN
#### Embedding type (Sara): wordpiece multichannel
	- wordpiece multichannel #1:	distil-bert-Sara-Jan31-19:24:12_FCN
	- wordpiece multichannel #2:				
	- wordpiece multichannel #3:				
	- word multichannel #1:			distil-bert-Sara-Jan31-10:07:57_FCN
	- word multichannel #2:			distil-bert-Sara-Jan31-19:00:40_FCN
	- word multichannel #3:			distil-bert-Sara-Jan31-19:48:53_FCN
#### Embedding type (SST-2): word multichannel
	- wordpiece multichannel #1:	distil-bert-SST-2-Feb01-19:40:33_FCN
	- wordpiece multichannel #2:				
	- wordpiece multichannel #3:				
	- word multichannel #1:			distil-bert-SST-2-Feb01-23:41:34_FCN
	- word multichannel #2:			distil-bert-SST-2-Feb01-21:32:49_FCN
	- word multichannel #3:			distil-bert-SST-2-Feb01-19:42:24_FCN
#### Model size (CoLA)
	- LSTM=600, FC=800 #1:			distil-bert-CoLA-Jan20-15:27:08_FCN
	- LSTM=600, FC=800 #2:			distil-bert-CoLA-Jan20-15:27:12_FCN
	- LSTM=600, FC=800 #3:			distil-bert-CoLA-Jan20-15:27:17_FCN

	- LSTM=900, FC=1200 #1:			distil-bert-CoLA-Jan20-15:27:56_FCN
	- LSTM=900, FC=1200 #2:			distil-bert-CoLA-Jan20-15:28:00_FCN
	- LSTM=900, FC=1200 #3:			distil-bert-CoLA-Jan20-15:28:04_FCN

	- LSTM=1200, FC=1600 #1:		distil-bert-CoLA-Jan20-15:28:47_FCN
	- LSTM=1200, FC=1600 #2:		distil-bert-CoLA-Jan20-15:28:50_FCN
	- LSTM=1200, FC=1600 #3:		distil-bert-CoLA-Jan20-15:28:54_FCN

	- LSTM=1500, FC=2000 #1:		distil-bert-CoLA-Jan20-15:29:35_FCN
	- LSTM=1500, FC=2000 #2:		distil-bert-CoLA-Jan20-15:29:37_FCN
	- LSTM=1500, FC=2000 #3:		distil-bert-CoLA-Jan20-15:29:41_FCN

	- LSTM=300, FC=400, L=2 #1:		distil-bert-CoLA-Jan21-00:54:41_FCN
	- LSTM=300, FC=400, L=2 #2:		distil-bert-CoLA-Jan21-00:54:45_FCN
	- LSTM=300, FC=400, L=2 #3:		distil-bert-CoLA-Jan21-00:54:50_FCN

	- LSTM=600, FC=800, L=2 #1:		distil-bert-CoLA-Jan21-00:58:53_FCN 15.4M
	- LSTM=600, FC=800, L=2 #2:		distil-bert-CoLA-Jan21-01:00:43_FCN
	- LSTM=600, FC=800, L=2 #3:		distil-bert-CoLA-Jan21-01:00:56_FCN

	- LSTM=900, FC=1200, L=2 #1:	distil-bert-CoLA-Jan21-09:08:51_FCN
	- LSTM=900, FC=1200, L=2 #2:	distil-bert-CoLA-Jan21-09:09:04_FCN
	- LSTM=900, FC=1200, L=2 #3:	distil-bert-CoLA-Jan21-09:09:08_FCN

	- LSTM=1200, FC=1600, L=2 #1:	distil-bert-CoLA-Jan21-09:10:20_FCN
	- LSTM=1200, FC=1600, L=2 #2:	distil-bert-CoLA-Jan21-09:10:25_FCN
	- LSTM=1200, FC=1600, L=2 #3:	distil-bert-CoLA-Jan21-09:10:45_FCN

	- LSTM=1500, FC=2000, L=2 #1:	distil-bert-CoLA-Jan21-09:11:59_FCN
	- LSTM=1500, FC=2000, L=2 #2:	distil-bert-CoLA-Jan21-09:12:05_FCN
	- LSTM=1500, FC=2000, L=2 #3:	distil-bert-CoLA-Jan21-09:14:17_FCN

	- LSTM=300, FC=400, L=3 #1:		distil-bert-CoLA-Jan21-09:17:10_FCN
	- LSTM=300, FC=400, L=3 #2:		distil-bert-CoLA-Jan21-09:18:42_FCN
	- LSTM=300, FC=400, L=3 #3:		distil-bert-CoLA-Jan21-10:59:59_FCN

	- LSTM=600, FC=800, L=3 #1:		distil-bert-CoLA-Jan21-11:01:09_FCN
	- LSTM=600, FC=800, L=3 #2:		distil-bert-CoLA-Jan21-11:01:29_FCN
	- LSTM=600, FC=800, L=3 #3:		distil-bert-CoLA-Jan21-11:02:02_FCN

	- LSTM=900, FC=1200, L=3 #1:	distil-bert-CoLA-Jan21-11:04:15_FCN
	- LSTM=900, FC=1200, L=3 #2:	distil-bert-CoLA-Jan21-11:04:40_FCN
	- LSTM=900, FC=1200, L=3 #3:	distil-bert-CoLA-Jan21-15:47:58_FCN

	- LSTM=1200, FC=1600, L=3 #1:	distil-bert-CoLA-Jan22-20:46:57_FCN
	- LSTM=1200, FC=1600, L=3 #2:	distil-bert-CoLA-Jan22-20:47:02_FCN
	- LSTM=1200, FC=1600, L=3 #3:	distil-bert-CoLA-Jan22-20:47:09_FCN
	
	- LSTM=1500, FC=2000, L=3 #1:	distil-bert-CoLA-Jan26-15:52:16_FCN
	- LSTM=1500, FC=2000, L=3 #2:	distil-bert-CoLA-Jan26-15:52:46_FCN
	- LSTM=1500, FC=2000, L=3 #3:	distil-bert-CoLA-Jan26-15:53:13_FCN

	- LSTM=300, FC=400, L=4 #1:		distil-bert-CoLA-Jan22-09:42:07_FCN
	- LSTM=300, FC=400, L=4 #2:		distil-bert-CoLA-Jan22-09:42:15_FCN
	- LSTM=300, FC=400, L=4 #3:		distil-bert-CoLA-Jan22-09:42:34_FCN

	- LSTM=600, FC=800, L=4 #1:		distil-bert-CoLA-Jan22-09:43:53_FCN
	- LSTM=600, FC=800, L=4 #2:		distil-bert-CoLA-Jan22-09:43:55_FCN
	- LSTM=600, FC=800, L=4 #3:		distil-bert-CoLA-Jan22-09:43:59_FCN

	- LSTM=900, FC=1200, L=4 #1:	distil-bert-CoLA-Jan22-20:49:39_FCN
	- LSTM=900, FC=1200, L=4 #2:	distil-bert-CoLA-Jan22-20:49:47_FCN
	- LSTM=900, FC=1200, L=4 #3:	distil-bert-CoLA-Jan22-20:49:50_FCN

	- LSTM=1200, FC=1600, L=4 #1:	distil-bert-CoLA-Jan24-10:10:34_FCN
	- LSTM=1200, FC=1600, L=4 #2:	distil-bert-CoLA-Jan24-10:10:36_FCN
	- LSTM=1200, FC=1600, L=4 #3:	distil-bert-CoLA-Jan24-10:10:39_FCN

	- LSTM=1500, FC=2000, L=4 #1:	distil-bert-CoLA-Jan26-15:54:02_FCN
	- LSTM=1500, FC=2000, L=4 #2:	distil-bert-CoLA-Jan26-15:53:52_FCN
	- LSTM=1500, FC=2000, L=4 #3:	distil-bert-CoLA-Jan26-15:53:57_FCN

	- LSTM=300, FC=400, L=5 #1:		distil-bert-CoLA-Jan22-09:51:35_FCN
	- LSTM=300, FC=400, L=5 #2:		distil-bert-CoLA-Jan22-09:51:40_FCN
	- LSTM=300, FC=400, L=5 #3:		distil-bert-CoLA-Jan22-09:51:54_FCN

	- LSTM=600, FC=800, L=5 #1:		distil-bert-CoLA-Jan22-20:51:12_FCN
	- LSTM=600, FC=800, L=5 #2:		distil-bert-CoLA-Jan22-20:51:17_FCN
	- LSTM=600, FC=800, L=5 #3:		distil-bert-CoLA-Jan22-20:51:25_FCN

	- LSTM=900, FC=1200, L=5 #1:	distil-bert-CoLA-Jan22-23:38:50_FCN
	- LSTM=900, FC=1200, L=5 #2:	distil-bert-CoLA-Jan22-23:39:06_FCN
	- LSTM=900, FC=1200, L=5 #3:	distil-bert-CoLA-Jan22-23:40:55_FCN

	- LSTM=1200, FC=1600, L=5 #1:	distil-bert-CoLA-Jan24-10:11:12_FCN
	- LSTM=1200, FC=1600, L=5 #2:	distil-bert-CoLA-Jan24-10:11:14_FCN
	- LSTM=1200, FC=1600, L=5 #3:	distil-bert-CoLA-Jan24-10:11:16_FCN

	- LSTM=1500, FC=2000, L=5 #1:	distil-bert-CoLA-Jan28-18:34:00_FCN
	- LSTM=1500, FC=2000, L=5 #2:	distil-bert-CoLA-Jan28-18:34:08_FCN
	- LSTM=1500, FC=2000, L=5 #3:	distil-bert-CoLA-Jan28-18:54:54_FCN
#### Model size (Sara) teacher=0.8753
	- LSTM=300, FC=400:			done		
	- LSTM=150, FC=200:			distil-bert-Sara-Feb01-10:23:06_FCN
	- LSTM=75, FC=100:			distil-bert-Sara-Feb01-10:24:16_FCN
	- LSTM=37, FC=50:			distil-bert-Sara-Feb01-10:25:21_FCN
#### Model size (SST-2) teacher=0.9151
	- LSTM=300, FC=400:			done		
	- LSTM=150, FC=200:			distil-bert-SST-2-Feb02-23:06:55_FCN
	- LSTM=75, FC=100:			distil-bert-SST-2-Feb02-23:08:41_FCN
	- LSTM=37, FC=50:			distil-bert-SST-2-Feb02-23:09:34_FCN
	- LSTM=19, FC=25:           distil-bert-SST-2-Feb03-09:23:05_FCN
	- LSTM=9, FC=13:			distil-bert-SST-2-Feb04-08:52:36_FCN
	- LSTM=5, FC=6:				distil-bert-SST-2-Feb04-08:52:09_FCN

### BERT
#### Learning rate
	<!-- - 5e-3 #1:		distil-bert-CoLA-Jan17-16:10:06_FCN -->
	<!-- - 1.5e-3 #1:	distil-bert-CoLA-Jan17-15:57:10_FCN -->
	<!-- - 5e-4 #1:		distil-bert-CoLA-Jan17-16:10:36_FCN -->
	<!-- - 1.5e-4 #1:	distil-bert-CoLA-Jan17-16:12:47_FCN -->
	<!-- - 5e-5 #1:		distil-bert-CoLA-Jan17-16:13:14_FCN -->
	<!-- - 1.5e-5 #1:	distil-bert-CoLA-Jan17-16:19:46_FCN -->
	<!-- - 5e-6 #1:		distil-bert-CoLA-Jan17-16:14:33_FCN -->
	- 5e-3 #1:			distil-bert-CoLA-Jan20-15:30:50_FCN
	- 1.5e-3 #1:		distil-bert-CoLA-Jan20-15:33:44_FCN
	- 5e-4 #1:			distil-bert-CoLA-Jan20-15:31:04_FCN
	- 1.5e-4 #1:		distil-bert-CoLA-Jan20-15:33:55_FCN
	- 5e-5 #1:			distil-bert-CoLA-Jan20-15:31:49_FCN
	- 1.5e-5 #1:		distil-bert-CoLA-Jan20-15:34:05_FCN
	- 5e-6 #1:			distil-bert-CoLA-Jan20-15:32:03_FCN
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
	- wp=0, decay #1:			distil-bert-CoLA-Jan21-20:50:51_FCN
	- wp=0, no decay #1:		distil-bert-CoLA-Jan21-21:12:24_FCN
	- wp=5, decay #1:			distil-bert-CoLA-Jan21-21:40:15_FCN
	- wp=5, no decay #1:		distil-bert-CoLA-Jan21-23:14:47_FCN
	- wp=10, no decay #1:		distil-bert-CoLA-Jan22-09:29:53_FCN
	- wp=15, decay #1:			distil-bert-CoLA-Jan22-09:30:36_FCN
	- wp=15, no decay #1:		distil-bert-CoLA-Jan22-09:31:03_FCN
	- wp=20, decay #1:			distil-bert-CoLA-Jan22-09:31:31_FCN
	- wp=20, no decay #1:		distil-bert-CoLA-Jan22-09:32:06_FCN
#### Batch size
	<!-- - 32:	distil-bert-CoLA-Jan19-10:04:57_FCN -->
	<!-- - 64:	distil-bert-CoLA-Jan19-10:05:42_FCN -->
	<!-- - 128:	distil-bert-CoLA-Jan19-10:06:41_FCN -->
	<!-- - 362:	distil-bert-CoLA-Jan19-11:09:55_FCN -->
	<!-- - 512:	distil-bert-CoLA-Jan23-09:55:20_FCN
	- 32:		distil-bert-CoLA-Jan23-09:47:32_FCN
	- 64:		distil-bert-CoLA-Jan23-09:46:50_FCN
	- 128:		distil-bert-CoLA-Jan23-09:48:13_FCN
	- 512:		distil-bert-CoLA-Jan23-09:49:54_FCN
#### Embedding type (CoLA): word multichannel
	- word: 					distil-bert-CoLA-Jan24-10:07:32_FCN
	- word (multichannel): 		distil-bert-CoLA-Jan24-10:07:52_FCN
	- wordpiece (multichannel): distil-bert-CoLA-Jan25-09:42:35_FCN
#### Embedding type (Sara): wordpiece non-static
	- word (multichannel):		distil-bert-Sara-Jan31-09:34:12_FCN 		
	- wordpiece: 				distil-bert-Sara-Feb01-09:38:47_FCN
#### Embedding type (SST-2): word multichannel
	- word (multichannel):		distil-bert-SST-2-Feb01-19:47:00_FCN
	- wordpiece: 				distil-bert-SST-2-Feb01-19:44:54_FCN
#### Model size (CoLA)
	- inflating: width up to 4x, depth up to 3x
	- W=1, D=1 (L=5 H=204 A=3 I=750):		not running								2.4  (1x128)                                      optimal_lr=5e-4
	- W=2, D=1 (L=5 H=408 A=6 I=1500):		distil-bert-CoLA-Jan25-10:02:01_FCNX    9.6  (1x128) distil-bert-CoLA-Jan28-09:23:07_X    optimal_lr=1e-4  distil-bert-CoLA-Jan29-11:08:03_FCN
	- W=3, D=1 (L=5 H=612 A=9 I=2250):		distil-bert-CoLA-Jan25-10:12:42_FCNX	21.7 (2x64)  distil-bert-CoLA-Jan28-09:20:16_X    optimal_lr=8e-5  distil-bert-CoLA-Jan29-11:17:12_FCN
	- W=4, D=1 (L=5 H=816 A=12 I=3000):		distil-bert-CoLA-Jan25-11:42:48_X		38.5 (4x32)  distil-bert-CoLA-Jan28-12:39:33_X    optimal_lr=7e-5  distil-bert-CoLA-Jan29-11:25:47_FCN
	- W=5, D=1 (L=5 H=1020 A=15 I=3750):	distil-bert-CoLA-Feb01-21:22:43_FTCN    60.2 (4x32)                                       optimal_lr=4e-5  distil-bert-CoLA-Feb02-10:42:58_FCN

	- W=1, D=2 (L=10 H=204 A=3 I=750):		distil-bert-CoLA-Jan25-10:50:54_FCN		4.8	 (2x64)                                       optimal_lr=5e-4?
	- W=2, D=2 (L=10 H=408 A=6 I=1500):		distil-bert-CoLA-Jan25-10:18:53_FCNX	19.1 (2x64)  distil-bert-CoLA-Jan28-09:18:28_X    optimal_lr=8e-5  distil-bert-CoLA-Jan29-11:09:47_FCN
	- W=3, D=2 (L=10 H=612 A=9 I=2250):		distil-bert-CoLA-Jan25-10:45:05_X 		43   (4x32)  distil-bert-CoLA-Jan28-11:57:35_X    optimal_lr=5e-5  distil-bert-CoLA-Jan29-11:18:20_FCN
	- W=4, D=2 (L=10 H=816 A=12 I=3000):	distil-bert-CoLA-Jan25-11:10:16_X		76.4 (4x32)  distil-bert-CoLA-Jan28-12:22:22_X    optimal_lr=4e-5  distil-bert-CoLA-Jan29-11:38:07_FCN
	- W=5, D=2 (L=10 H=1020 A=15 I=3750):	distil-bert-CoLA-Feb01-21:51:43_FTCN    119.3(8x16)                                       optimal_lr=4e-5  distil-bert-CoLA-Feb02-11:02:51_FT
	
	- W=1, D=3 (L=15 H=204 A=3 I=750):		distil-bert-CoLA-Jan25-10:35:13_FCN		7.2	 (2x64)                                       optimal_lr=1e-4? distil-bert-CoLA-Jan29-13:58:24_FCN
	- W=2, D=3 (L=15 H=408 A=6 I=1500):		distil-bert-CoLA-Jan25-10:41:45_X		28.6 (4x32)  distil-bert-CoLA-Jan29-00:18:17_X    optimal_lr=7e-5? distil-bert-CoLA-Jan29-14:42:48_FCN
	- W=3, D=3 (L=15 H=612 A=9 I=2250):		distil-bert-CoLA-Jan25-10:47:07_X		64.3 (4x32)  distil-bert-CoLA-Jan28-18:22:38_X    optimal_lr=5e-5  distil-bert-CoLA-Jan29-11:23:24_FCN
	- W=4, D=3 (L=15 H=816 A=12 I=3000):	distil-bert-CoLA-Jan25-15:54:15_X		114.2(8x16)	 distil-bert-CoLA-Jan28-18:24:05_X    optimal_lr=4e-5  distil-bert-CoLA-Jan29-11:38:51_FTCN
#### Model size (SST-2)
	- W=1, D=1 (L=5 H=204 A=3 I=750):		tried already
	- W=1, D=/2 (L=3 H=204 A=3 I=750):		distil-bert-SST-2-Feb02-23:14:33_FCN
	- W=1, D=/3 (L=2 H=204 A=3 I=750):		distil-bert-SST-2-Feb02-23:15:03_FCN
	- W=1, D=/4 (L=1 H=204 A=3 I=750):		distil-bert-SST-2-Feb02-23:15:27_FCN

	- W=/2, D=1 (L=5 H=102 A=2 I=375):		distil-bert-SST-2-Feb02-23:16:54_FCN
	- W=/2, D=/2 (L=3 H=102 A=2 I=375):	    distil-bert-SST-2-Feb02-23:21:13_FCN
	- W=/2, D=/3 (L=2 H=102 A=2 I=375):		distil-bert-SST-2-Feb02-23:21:48_FCN
	- W=/2, D=/4 (L=1 H=102 A=2 I=375):		distil-bert-SST-2-Feb02-23:22:20_FCN
	
	- W=/3, D=1 (L=5 H=68 A=1 I=250):		distil-bert-SST-2-Feb02-23:23:19_FCN
	- W=/3, D=/2 (L=3 H=68 A=1 I=250):		distil-bert-SST-2-Feb03-09:12:00_FCN
	- W=/3, D=/3 (L=2 H=68 A=1 I=250):		distil-bert-SST-2-Feb03-09:12:45_FCN
	- W=/3, D=/4 (L=1 H=68 A=1 I=250):		distil-bert-SST-2-Feb03-09:13:07_FCN

	- W=/4, D=1 (L=5 H=51 A=1 I=188):		distil-bert-SST-2-Feb03-23:43:57_FCN
	- W=/4, D=/2 (L=3 H=51 A=1 I=188):		distil-bert-SST-2-Feb03-23:40:47_FCN
	- W=/4, D=/3 (L=2 H=51 A=1 I=188):		distil-bert-SST-2-Feb03-23:44:39_FCN
	- W=/4, D=/4 (L=1 H=51 A=1 I=188):		distil-bert-SST-2-Feb03-23:45:04_FCN

	- W=/8, D=1 (L=5 H=26 A=1 I=94):		distil-bert-SST-2-Feb04-08:54:55_FCN
	- W=/8, D=/2 (L=3 H=26 A=1 I=94):		distil-bert-SST-2-Feb03-23:48:53_FCN
	- W=/8, D=/3 (L=2 H=26 A=1 I=94):		distil-bert-SST-2-Feb03-23:48:23_FCN
	- W=/8, D=/4 (L=1 H=26 A=1 I=94):		distil-bert-SST-2-Feb03-23:47:57_FCN

	- W=/16, D=1 (L=5 H=13 A=1 I=47):		distil-bert-SST-2-Feb04-12:29:47_FCN
	- W=/16, D=/2 (L=3 H=13 A=1 I=47):		distil-bert-SST-2-Feb04-12:30:49_FCN
	- W=/16, D=/3 (L=2 H=13 A=1 I=47):		distil-bert-SST-2-Feb04-12:31:23_FCN
	- W=/16, D=/4 (L=1 H=13 A=1 I=47):		distil-bert-SST-2-Feb04-12:31:51_FCN
#### Model size (Sara)
	- W=1, D=1 (L=5 H=204 A=3 I=750):		tried already
	- W=1, D=/2 (L=3 H=204 A=3 I=750):		distil-bert-Sara-Feb02-11:31:12_FCN
	- W=1, D=/3 (L=2 H=204 A=3 I=750):		distil-bert-Sara-Feb02-11:31:48_FCN
	- W=1, D=/4 (L=1 H=204 A=3 I=750):		distil-bert-Sara-Feb03-09:18:48_FCN
	
	- W=/2, D=1 (L=5 H=102 A=2 I=375):		distil-bert-Sara-Feb02-11:32:57_FCN
	- W=/2, D=/2 (L=3 H=102 A=2 I=375):	    distil-bert-Sara-Feb02-11:33:27_FCN
	- W=/2, D=/3 (L=2 H=102 A=2 I=375):		distil-bert-Sara-Feb02-11:34:20_FCN
	- W=/2, D=/4 (L=1 H=102 A=2 I=375):		distil-bert-Sara-Feb03-09:17:40_FCN
	
	- W=/3, D=1 (L=5 H=68 A=1 I=250):		distil-bert-Sara-Feb02-11:36:05_FCN
	- W=/3, D=/2 (L=3 H=68 A=1 I=250):		distil-bert-Sara-Feb02-11:36:39_FCN
	- W=/3, D=/3 (L=2 H=68 A=1 I=250):		distil-bert-Sara-Feb02-11:37:33_FCN
	- W=/3, D=/4 (L=1 H=68 A=1 I=250):		distil-bert-Sara-Feb03-09:16:28_FCN

## Student models for analysis
### CoLA
#### BERT:  word multichannel (41.9, 45.0)
	- W=2, D=2 (L=10 H=408 A=6 I=1500), 19.1M, B=2x64, lr=8e-5 #1:	distil-bert-CoLA-Feb05-16:41:03_F 42.9
	- W=2, D=2 (L=10 H=408 A=6 I=1500), 19.1M, B=2x64, lr=8e-5 #2:	distil-bert-CoLA-Feb05-16:42:01_FT 43.6
	- W=2, D=2 (L=10 H=408 A=6 I=1500), 19.1M, B=2x64, lr=8e-5 #3:	distil-bert-CoLA-Feb08-23:53:40_F 41.9 <<
	- W=2, D=2 (L=10 H=408 A=6 I=1500), 19.1M, B=2x64, lr=8e-5 #4:	distil-bert-CoLA-Feb08-23:53:48_F 41.9

	- W=4, D=1 (L=5 H=816 A=12 I=3000), 38.5M, B=4x32, lr=7e-5 #1:	distil-bert-CoLA-Feb05-16:46:03_FT 41.6
	- W=4, D=1 (L=5 H=816 A=12 I=3000), 38.5M, B=4x32, lr=7e-5 #2:	distil-bert-CoLA-Feb05-16:46:28_FT 41.4
	- W=4, D=1 (L=5 H=816 A=12 I=3000), 38.5M, B=4x32, lr=7e-5 #3:	distil-bert-CoLA-Feb09-00:12:44 41
	- W=4, D=1 (L=5 H=816 A=12 I=3000), 38.5M, B=4x32, lr=7e-5 #4:	distil-bert-CoLA-Feb09-00:12:53 32
	- W=4, D=1 (L=5 H=816 A=12 I=3000), 38.5M, B=4x32, lr=7e-5 #5:	distil-bert-CoLA-Feb09-00:24:58 33
	- W=4, D=1 (L=5 H=816 A=12 I=3000), 38.5M, B=4x32, lr=7e-5 #6:	distil-bert-CoLA-Feb09-00:25:16 32
#### LSTM: word multichannel (44.8)
	- W=2, D=2, LSTM=600, FC=800, L=2 #1:	distil-bert-CoLA-Feb05-16:49:47_F 44.2 <<
	- W=2, D=2, LSTM=600, FC=800, L=2 #2:	distil-bert-CoLA-Feb05-16:50:12_FC 43.5
	- W=2, D=2, LSTM=600, FC=800, L=2 #3:	distil-bert-CoLA-Feb06-09:56:35_FC 43.5
	- W=2, D=2, LSTM=600, FC=800, L=2 #4:	distil-bert-CoLA-Feb06-09:56:39_FC 43.5
	- W=2, D=2, LSTM=600, FC=800, L=2 #5:	distil-bert-CoLA-Feb06-09:57:38_FC 44.2
	- W=2, D=2, LSTM=600, FC=800, L=2 #6:	distil-bert-CoLA-Feb06-22:22:07_FC 43.5
	- W=2, D=2, LSTM=600, FC=800, L=2 #7:	distil-bert-CoLA-Feb06-22:22:12_FC 43.5
	- W=2, D=2, LSTM=600, FC=800, L=2 #8:	distil-bert-CoLA-Feb06-22:22:17_FC 44.2
### SST-2
#### BERT: word multichannel (89.2)
	- default #1:	distil-bert-SST-2-Feb05-17:35:22_F 89.3 <<
	- default #2:	distil-bert-SST-2-Feb05-17:35:27_FC 89.3
#### LSTM: word multichannel (91.9)
	- default #1:	distil-bert-SST-2-Feb05-17:02:41_F 91.2 <<
	- default #2:	distil-bert-SST-2-Feb05-17:03:29_FC 91.2
	- default #3:	distil-bert-SST-2-Feb07-09:53:26_FC 91.2
	- default #4:	distil-bert-SST-2-Feb07-09:53:29_FC 91.2
	- default #5:	distil-bert-SST-2-Feb07-09:53:33_FC 91.2
### Sara
#### BERT: wordpiece non-static (87.1)
	- default #1:	distil-bert-Sara-Feb05-16:59:56_FC 86.3
	- default #2:	distil-bert-Sara-Feb06-22:24:58_F 87.1 <<
	- default #3:	distil-bert-Sara-Feb06-22:26:22_FC 87.1
	- default #4:	distil-bert-Sara-Feb06-22:26:26_FC 87.1
#### LSTM: wordpiece multichannel (86.5)
	- default #1:	distil-bert-Sara-Feb05-17:04:42_F 86.5 <<

## TO-DO
	- probe word embeddings
	- probe wordpiece embeddings
	- do 3-way analysis on CoLA: small (w=2, d=2, 15.4M) BiLSTM vs small BERT (w=2, d=2, 19.1M) vs big BERT (w=4, d=1, 38.5M). hypothesis: size-comparable models absorb the same amount of probing knowledge, mcc-comparable models comparable in terms of their mistakes.
	- compare only 2.4M models on SST-2 and Sara

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
	7:
	8:..
	10:.
	11:....

```bash
dirs=""
for d in $dirs; do
  echo $d
  pushd $d
  rm ./pytorch_*
  popd
  cp -r $d $DICE/minfp2.bak
  rm ${d}.out
done
```

## Probing
### Pretrained
	avg+search:		   probe-CoLA-Jan29-11:12:46_FC
	avg+search_L=17    probe-CoLA-Jan30-09:12:26_FC
	avg+search_L=11    probe-CoLA-Jan29-11:31:13_FC
	avg+search_L=5     probe-CoLA-Jan30-09:16:05_FC
	avg+search_L=0     probe-CoLA-Jan29-12:15:07_FC
	avg+search_L=E     probe-CoLA-Feb09-13:21:42_FC
	embed_wordpiece:   probe-pretrained-Feb08-23:36:19_FC
	embed_word:        probe-pretrained-Feb08-00:20:49_FC
### CoLA
	avg+search:		   probe-CoLA-Jan26-17:56:54_FC
	max+search:		   probe-CoLA-Jan26-17:58:15_FC
	single+search:	   probe-CoLA-Jan26-15:10:51_FC
	avg+search_L=17    probe-CoLA-Jan29-14:37:41_FC
	avg+search_L=11    probe-CoLA-Jan27-09:22:06_FC
	single+search_L=11 probe-CoLA-Jan28-09:29:52_FC
	max+search_L=11    probe-CoLA-Jan28-09:31:40_FC
	avg+search_L=5     probe-CoLA-Jan29-14:39:58_FC
	avg+search_L=0 	   probe-CoLA-Jan27-13:34:50_FC
	avg+search_L=E 	   probe-CoLA-Feb09-13:16:42_FC
	single+search_L=0  probe-CoLA-Jan28-12:53:24_FC
	max+search_L=0     probe-CoLA-Jan28-12:54:55_FC
	embed_wordpiece    probe-CoLA-Feb08-23:36:58_FC
	embed_word         probe-CoLA-Feb08-00:37:24_FC
	student-BERT_L9	   probe-CoLA-Feb10-23:46:23
	student-BERT_L8	   probe-CoLA-Feb10-23:45:40
	student-BERT_L7	   probe-CoLA-Feb10-23:45:12
	student-BERT_L6	   probe-CoLA-Feb10-23:44:48
	student-BERT_L5	   probe-CoLA-Feb10-23:44:18
	student-BERT_L4	   probe-CoLA-Feb10-23:43:02
	student-BERT_L3	   probe-CoLA-Feb10-23:42:20
	student-BERT_L2	   probe-CoLA-Feb10-23:41:55
	student-BERT_L1	   probe-CoLA-Feb10-23:41:25
	student-BERT_L0	   probe-CoLA-Feb10-23:40:58
	student-BERT_LE    probe-CoLA-Feb10-23:39:27
	student-LSTM       probe-CoLA-Feb08-23:25:58_FC
### SST-2
	single+search:     probe-SST-2-Jan26-16:17:27_FC
	max+search:		   probe-SST-2-Jan27-09:18:31_FC
	avg+search:		   probe-SST-2-Jan27-09:16:19_FC
	avg+search_L=17    probe-SST-2-Jan29-14:56:56_FC
	avg+search_L=11    probe-SST-2-Jan27-23:07:32_FC
	avg+search_L=5     probe-SST-2-Jan29-14:58:56_FC
	avg+search_L=0     probe-SST-2-Jan27-23:44:08_FC
	avg+search_L=E     probe-SST-2-Feb09-13:17:18_FC
	embed_wordpiece    probe-SST-2-Feb08-23:37:10_FC
	embed_word         probe-SST-2-Feb08-00:37:28_FC
	student-BERT_L4	   probe-SST-2-Feb08-01:01:40_FC
	student-BERT_L3	   probe-SST-2-Feb09-12:53:24_FC
	student-BERT_L2	   probe-SST-2-Feb08-01:03:42_FC
	student-BERT_L1	   probe-SST-2-Feb09-12:53:04_FC
	student-BERT_L0	   probe-SST-2-Feb08-01:04:12_FC
	student-BERT_LE    probe-SST-2-Feb09-13:05:50_FC
	student-LSTM       probe-SST-2-Feb08-23:25:47_FC
### Sara
	single+search:	   probe-Sara-Jan27-09:06:41_FC
	avg+search:		   probe-Sara-Jan28-12:51:15_FC
	avg+search_L=17    probe-Sara-Jan30-09:10:25_FC
	avg+search_L=11    probe-Sara-Jan27-23:59:21_FC
	avg+search_L=5     probe-Sara-Jan30-09:10:53_FC
	avg+search_L=0     probe-Sara-Jan28-00:00:16_FC
	avg+search_L=E     probe-Sara-Feb09-13:19:54_FC
	embed_wordpiece    probe-Sara-Feb08-23:37:14_FC
	embed_word         probe-Sara-Feb08-00:37:34_FC
	student-BERT_L4	   probe-Sara-Feb08-00:54:22_FC
	student-BERT_L3	   probe-Sara-Feb09-12:55:26_FC
	student-BERT_L2	   probe-Sara-Feb08-00:57:37_FC
	student-BERT_L1	   probe-Sara-Feb09-12:55:10_FC
	student-BERT_L0	   probe-Sara-Feb08-00:59:38_FC
	student-BERT_LE	   probe-Sara-Feb09-13:04:50_FC
	student-LSTM	   probe-Sara-Feb08-23:15:54_FC

```bash
dirs="probe-CoLA-Feb09-13:21:42"
for d in $dirs; do
  echo $d
  rm -rf $d
  mv ${d}.out $DICE/minfp2.bak/probing-logs
done
```

# Trash
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

## Old sizes
BERT (small):
	trainable parameters (all): 32771074 (32.7M)
	trainable parameters (embeddings): 31650560 (31.6M)
	non-embedding prameters: 1120514 (1.1M)
BiLSTM
	trainable parameters (all): 75354902 (75M)
	trainable parameters (embeddings): 72948900 (73M)
	all parameters: 148303802 (148M)
	non-embedding prameters: 2406002 (2.4M)
