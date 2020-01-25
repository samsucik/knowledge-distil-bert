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

### Student sizes
#### BERT
theory
- large: L=24 H=1024 A=16 I=4096
- /12:   L=2  H=85   A=1  I=341  (183K)
- /6:    L=4  H=171  A=3  I=683  (1.44M)
- /5:    L=5  H=204  A=3  I=819  (2.56M) [with I=750 is 2.42M]

practice
- 2.42M: L=5 H=204 A=3 I=750
- inflating: width up to 4x, depth up to 3x

#### BiLSTM
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

	- word non-static #1:		distil-bert-CoLA-Jan25-09:40:14
	- word non-static #2:		distil-bert-CoLA-Jan25-09:40:18
	- word non-static #3:		distil-bert-CoLA-Jan25-09:40:23
#### Model size
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

	- LSTM=600, FC=800, L=2 #1:		distil-bert-CoLA-Jan21-00:58:53_FCN
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

	- LSTM=300, FC=400, L=4 #1:		distil-bert-CoLA-Jan22-09:42:07_FCN
	- LSTM=300, FC=400, L=4 #2:		distil-bert-CoLA-Jan22-09:42:15_FCN
	- LSTM=300, FC=400, L=4 #3:		distil-bert-CoLA-Jan22-09:42:34_FCN

	- LSTM=600, FC=800, L=4 #1:		distil-bert-CoLA-Jan22-09:43:53_FCN
	- LSTM=600, FC=800, L=4 #2:		distil-bert-CoLA-Jan22-09:43:55_FCN
	- LSTM=600, FC=800, L=4 #3:		distil-bert-CoLA-Jan22-09:43:59_FCN

	- LSTM=900, FC=1200, L=4 #1:	distil-bert-CoLA-Jan22-20:49:39_FCN
	- LSTM=900, FC=1200, L=4 #2:	distil-bert-CoLA-Jan22-20:49:47_FCN
	- LSTM=900, FC=1200, L=4 #3:	distil-bert-CoLA-Jan22-20:49:50_FCN

	- LSTM=1200, FC=1600, L=4 #1:	distil-bert-CoLA-Jan24-10:10:34
	- LSTM=1200, FC=1600, L=4 #2:	distil-bert-CoLA-Jan24-10:10:36
	- LSTM=1200, FC=1600, L=4 #3:	distil-bert-CoLA-Jan24-10:10:39

	- LSTM=300, FC=400, L=5 #1:		distil-bert-CoLA-Jan22-09:51:35_FCN
	- LSTM=300, FC=400, L=5 #2:		distil-bert-CoLA-Jan22-09:51:40_FCN
	- LSTM=300, FC=400, L=5 #3:		distil-bert-CoLA-Jan22-09:51:54_FCN

	- LSTM=600, FC=800, L=5 #1:		distil-bert-CoLA-Jan22-20:51:12_FCN
	- LSTM=600, FC=800, L=5 #2:		distil-bert-CoLA-Jan22-20:51:17_FCN
	- LSTM=600, FC=800, L=5 #3:		distil-bert-CoLA-Jan22-20:51:25_FCN

	- LSTM=900, FC=1200, L=5 #1:	distil-bert-CoLA-Jan22-23:38:50_FCN
	- LSTM=900, FC=1200, L=5 #2:	distil-bert-CoLA-Jan22-23:39:06_FCN
	- LSTM=900, FC=1200, L=5 #3:	distil-bert-CoLA-Jan22-23:40:55_FCN

	- LSTM=1200, FC=1600, L=5 #1:	distil-bert-CoLA-Jan24-10:11:12
	- LSTM=1200, FC=1600, L=5 #2:	distil-bert-CoLA-Jan24-10:11:14
	- LSTM=1200, FC=1600, L=5 #3:	distil-bert-CoLA-Jan24-10:11:16

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
#### Embedding type
	- word: 					distil-bert-CoLA-Jan24-10:07:32_FCN
	- word (multichannel): 		distil-bert-CoLA-Jan24-10:07:52_FCN
	- wordpiece (multichannel): distil-bert-CoLA-Jan25-09:42:35
#### Model size
- inflating: width up to 4x, depth up to 3x
- W=1, D=1 (L=5 H=204 A=3 I=750):		not running								2.4  (1x128)
- W=2, D=1 (L=5 H=408 A=6 I=1500):		distil-bert-CoLA-Jan25-10:02:01_ 		9.6  (1x128)
- W=3, D=1 (L=5 H=612 A=9 I=2250):		distil-bert-CoLA-Jan25-10:12:42_		21.7 (2x64)
- W=4, D=1 (L=5 H=816 A=12 I=3000):		distil-bert-CoLA-Jan25-11:42:48_		38.5 (4x32)

- W=1, D=2 (L=10 H=204 A=3 I=750):		distil-bert-CoLA-Jan25-10:50:54_ 		4.8	 (2x64)
- W=2, D=2 (L=10 H=408 A=6 I=1500):		distil-bert-CoLA-Jan25-10:18:53_		19.1 (2x64)
- W=3, D=2 (L=10 H=612 A=9 I=2250):		distil-bert-CoLA-Jan25-10:45:05_ 		43   (4x32)
- W=4, D=2 (L=10 H=816 A=12 I=3000):	distil-bert-CoLA-Jan25-11:10:16_		76.4 (4x32)

- W=1, D=3 (L=15 H=204 A=3 I=750):		distil-bert-CoLA-Jan25-10:35:13_		7.2	 (2x64)
- W=2, D=3 (L=15 H=408 A=6 I=1500):		distil-bert-CoLA-Jan25-10:41:45_		28.6 (2x64)
- W=3, D=3 (L=15 H=612 A=9 I=2250):		distil-bert-CoLA-Jan25-10:47:07_ 		64.3 (4x32)
- W=4, D=3 (L=15 H=816 A=12 I=3000):	distil-bert-CoLA-Jan25-15:54:15			114.2(8x16)	

distil-bert-CoLA-Jan24-10:10:39
distil-bert-CoLA-Jan25-09:40:23
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

```bash 
dirs="distil-bert-CoLA-Jan22-23:39:06 distil-bert-CoLA-Jan23-09:47:32 distil-bert-CoLA-Jan24-10:07:32 distil-bert-CoLA-Jan24-10:07:52"
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
