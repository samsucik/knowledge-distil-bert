from pytorch_transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("experiments/teacher-CoLA", do_lower_case=True)
tokens = tokenizer.tokenize("How are you, Sam Sucik? Good, you?")
ids = tokenizer.convert_tokens_to_ids(tokens)

print(tokens)
print(ids)
