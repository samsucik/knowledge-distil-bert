from argparse import ArgumentParser

from gensim.models.keyedvectors import KeyedVectors
import torch
from tqdm import tqdm


if __name__ == '__main__':
    parser = ArgumentParser(description='Convert binary word2vec to txt')
    parser.add_argument('--input', default="GoogleNews-vectors-negative300.bin", required=False)
    parser.add_argument('--output', default="GoogleNews-vectors-negative300.txt", required=False)

    args = parser.parse_args()
    model = KeyedVectors.load_word2vec_format(args.input, binary=True)
    model.save_word2vec_format(args.output, binary=False)
