import torch
import argparse, os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pretrained_model_dir", default="teacher-pretrained", type=str,
                        help="Model from which to extract the pretrained embeddings.")
    parser.add_argument("--pretrained_model_file", default="pytorch_model.bin", type=str,
                        help="Model from which to extract the pretrained embeddings.")
    args = parser.parse_args()

    embeddings_file = os.path.join(args.pretrained_model_dir, "wordpiece_embeddings_teacher_h1024.pt")
    if not os.path.exists(embeddings_file):
        state_dict = torch.load(os.path.join(args.pretrained_model_dir, args.pretrained_model_file), map_location=torch.device("cpu"))
        embedding_weights = state_dict["bert.embeddings.word_embeddings.weight"]
        token_embedding_state_dict = {"bert.embeddings.word_embeddings.weight": embedding_weights}
        torch.save(token_embedding_state_dict, embeddings_file)

if __name__ == '__main__':
    main()
