import torch

path = "teacher-CoLA/pytorch_model.bin"
state_dict = torch.load(path, map_location=torch.device('cpu'))

for (name, value) in state_dict.items():
	nz = len(torch.nonzero(value, as_tuple=True)[0])
	total = value.numel()
	shape = "x".join([str(s) for s in value.shape])
	mean = torch.mean(value)
	std = torch.std(value)
	print("{} ({}):\n\tmean: {:.2f}, stdev: {:.4f}, {:.1f}% non-zero".format(name, shape, mean, std, 100*nz/total))
