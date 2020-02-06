import torch
import argparse, os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pretrained_model_dir", default="teacher-pretrained", type=str,
                        help="Model from which to extract the pretrained embeddings.")
    parser.add_argument("--pretrained_model_file", default="pytorch_model.bin", type=str,
                        help="Model from which to extract the pretrained embeddings.")
    parser.add_argument("--word_vectors_dir", type=str, default="None",
                        help="Directory from which to take word vectors.")
    args = parser.parse_args()

    if args.word_vectors_dir != "None":
        extract_word_embeddings(args)
    else:
        extract_wordpiece_embeddings(args)

def extract_wordpiece_embeddings(args):
    embeddings_file = os.path.join(args.pretrained_model_dir, "wordpiece_embeddings_teacher_h1024.pt")
    if not os.path.exists(embeddings_file):
        state_dict = torch.load(os.path.join(args.pretrained_model_dir, args.pretrained_model_file), map_location=torch.device("cpu"))
        embedding_weights = state_dict["bert.embeddings.word_embeddings.weight"]
        token_embedding_state_dict = {"bert.embeddings.word_embeddings.weight": embedding_weights}
        torch.save(token_embedding_state_dict, embeddings_file)

def extract_word_embeddings(args):
    v = torch.load(os.path.join(args.word_vectors_dir, "GoogleNews-vectors-negative300.txt.pt"), map_location="cpu")
    vocab = v[0]
    with open(os.path.join(args.pretrained_model_dir, "word_vocab.txt"), "w") as f:
        f.write("<unk>\n")
        f.write("<pad>\n")
        for w in vocab:
            f.write("{}\n".format(w))
    embeddings = v[2]
    embeddings = torch.cat((torch.FloatTensor(2, 300).uniform_(-0.25, 0.25), embeddings))
    torch.save(embeddings, os.path.join(args.pretrained_model_dir, "word_vectors"))

if __name__ == '__main__':
    main()
