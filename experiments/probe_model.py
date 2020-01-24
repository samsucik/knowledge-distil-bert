import senteval
import glob
import numpy as np
import argparse, os
from types import SimpleNamespace
import torch
from tqdm import tqdm

from examples.distillation.utils import parse_str2bool
from examples.distil_from_finetuned import create_word_level_tokenizer, numericalise_sentence
from pytorch_transformers.tokenization_bert import BertTokenizer
from pytorch_transformers.modeling_bert import BertForSequenceClassification

def dict_to_namespace(d):
    return SimpleNamespace(**d)

def numerisalise_batch(args, samples, tokenizer, cls_token, sep_token, pad_token_id):
    numericalised_samples = {"sentence": []}
    if args["model_type"] == "BERT": numericalised_samples["attention_mask"] = []
    for example in tqdm(samples[:50]):
        example_numericalised = numericalise_sentence(dict_to_namespace(args), " ".join(example), tokenizer,
                                                      cls_token=cls_token, sep_token=sep_token, 
                                                      pad_token_id=pad_token_id)
        if args["model_type"] == "BERT":
            mask = (np.array(example_numericalised) != pad_token_id).astype(int)
            numericalised_samples["attention_mask"].append(torch.LongTensor(mask))
        numericalised_samples["sentence"].append(torch.LongTensor(example_numericalised))
    return numericalised_samples

def prepare(args, samples):
    print("Creating a tokenizer...")
    model_args = torch.load(os.path.join(args["model_dir"], "training_args.bin"), map_location=args["device"])
    if args["use_word_vectors"]:
        vocab_file = os.path.join(args["glue_data_dir"], "transfer_set_vocab.txt")
        args["processed_word_vectors_file"] = os.path.join(args["glue_data_dir"], "word_vectors")
        args["max_seq_length"] = model_args.max_seq_length
        args["do_lower_case"] = model_args.do_lower_case
        tokenizer = create_word_level_tokenizer(dict_to_namespace(args), vocab_file, args["processed_word_vectors_file"], 
                                                transfer_dataset_raw=None, transfer_dataset_raw_file=None)
    else:
        tokenizer = BertTokenizer.from_pretrained(args["model_dir"], do_lower_case=model_args.do_lower_case)
    args["tokenizer"] = tokenizer
    
    args["cls_token"], args["sep_token"], pad_token = tokenizer.cls_token, tokenizer.sep_token, tokenizer.pad_token
    args["pad_token_id"] = tokenizer.convert_tokens_to_ids([pad_token])[0]

    print("Loading the trained model...")
    if args["is_student"]:
        file =  glob.glob(os.path.join(args["model_dir"], "pytorch_model_best*.pt"))
        model = torch.load(file[0], map_location=args["device"])
    else:
        model = BertForSequenceClassification.from_pretrained(args["model_dir"])
    model.to(args["device"])
    model.eval()
    args["model"] = model
    # torch.cuda.empty_cache()
    exit(0)

    return

def batcher(args, batch):
    batch_numericalised = numerisalise_batch(args, batch, args["tokenizer"], args["cls_token"], args["sep_token"], args["pad_token_id"])


    # feed into model
    exit(0)
    # retrieve activations and save
    # load activations
    # print([len(s) for s in batch])
    B = len(batch)
    print(batch[0])
    max_l = np.max([len(s) for s in batch])

    batch = np.random.random((B, 10))
    # print(batch[0])
    # print(len(batch[0]))
    return batch

def main():
    parser = argparse.ArgumentParser(description="Training")
    parser.add_argument("--senteval_path", default="/home/sam/edi/minfp2/SentEval", type=str, required=False,
                        help="SentEval path.")
    # parser.add_argument("--n_gpu", default="0", type=int, required=False,
    #                     help="# of GPUs available.")
    parser.add_argument("--glue_task", default="CoLA", type=str, required=False,
                        help="One of: CoLA, SST-2, Sara.")
    parser.add_argument("--model_type", default="BERT", type=str, required=False,
                        help="One of: BERT, LSTM.")
    parser.add_argument("--model_dir", default="teacher-CoLA", type=str, required=False,
                        help="Directory where trained model is saved.")
    parser.add_argument("--is_student", type=parse_str2bool, default=False,
                        help="Whether the model to probe is a student model or a teacher model.")
    parser.add_argument("--glue_data_dir", default="/home/sam/edi/minfp2/data/glue_data/CoLA", type=str, required=False,
                        help="Directory where the GLUE dataset is stored.")
    args = parser.parse_args()

    args.n_gpu = 1 if torch.cuda.is_available() else 0
    args.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    args.use_word_vectors = args.is_student and args.model_type == "LSTM" # TODO: make sure this is correct for BERT students!
    args.student_type = args.model_type
   
    params = {'task_path': os.path.join(args.senteval_path, "data"), 
              'seed': 42,
              'usepytorch': True, # args.n_gpu > 0, 
              'kfold': 10,
              **args.__dict__}
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
