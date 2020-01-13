from rasa.nlu.training_data.loading import _load as load_md_file

train_data = load_md_file("train.md", language="en")
test_data = load_md_file("test.md", language="en")

# gather all intents and create mapping to integers
intent_set_train = set([msg.data["intent"] for msg in train_data.training_examples])
intent_set_test = set([msg.data["intent"] for msg in test_data.training_examples])
assert intent_set_train == intent_set_test
intent_set = sorted(list(intent_set_train))
n_intents = len(intent_set)
intent_to_int = {intent: i for i, intent in enumerate(intent_set)}
int_to_intent = {i: intent for intent, i in intent_to_int.items()}

# we have train:test 80:20 split, now further split the training data into train and eval (60:20)
dev_examples, train_examples = train_data.split_nlu_examples(0.75)
test_examples = test_data.training_examples

print("Split into {} training, {} evaluation and {} test examples.".format(len(train_examples), len(dev_examples), len(test_examples)))

for label, examples in [("train", train_examples), ("dev", dev_examples), ("test", test_examples)]:
	with open("{}.tsv".format(label), "w") as f:
		for example in examples:
			f.write("{}\t{}\n".format(intent_to_int[example.data["intent"]], example.text))

with open("int_to_intent.tsv", "w") as f:
	for i in range(n_intents):
		f.write("{}\t{}\n".format(i, int_to_intent[i]))
