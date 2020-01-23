import senteval
import numpy as np
import argparse, os

def prepare(params, samples):
	pass
	# get tokenizer
	# numericalise
	# feed into model
	# retrieve activations and save
	# load activations

def batcher(params, batch):
	# print([len(s) for s in batch])
	B = len(batch)
	max_l = np.max([len(s) for s in batch])

	batch = np.random.random((B, 10))
	# print(batch[0])
	# print(len(batch[0]))
	return batch

def main():
	parser = argparse.ArgumentParser(description="Training")
	parser.add_argument("--senteval_path", default="/home/sam/edi/minfp2/SentEval", type=str, required=False,
                        help="SentEval path.")
	parser.add_argument("--n_gpu", default="0", type=int, required=False,
                        help="# of GPUs available.")
	args = parser.parse_args()
   
	params = {'task_path': os.path.join(args.senteval_path, "data"), 
			  'seed': 42,
			  'usepytorch': args.n_gpu > 0, 
			  'kfold': 10}
	params['classifier'] = {'nhid': 100,  # in paper they chose from [50, 100, 200]
							'optim': 'adam', 
							'batch_size': 64,
	                        'tenacity': 5, 
	                        'epoch_size': 4,
	                        'dropout': 0.1, # in paper they chose from [0.0, 0.1, 0.2]
	                        }
	transfer_tasks = ['Length', 'WordContent', 'Depth', 'TopConstituents','BigramShift', 'Tense',
	'SubjNumber', 'ObjNumber', 'OddManOut', 'CoordinationInversion']
	transfer_tasks = ['Length']
	
	"""
	params = {'task_path': os.path.join(args.senteval_path, "data"), 'optim': 'rmsprop', 
			  'batch_size': 128, 'tenacity': 3, 'epoch_size': 2}
	"""

	se = senteval.engine.SE(params, batcher, prepare)
	results = se.eval(transfer_tasks)
	print(results)

if __name__ == '__main__':
	main()
