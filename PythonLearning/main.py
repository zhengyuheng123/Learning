import torch
x = torch.rand(5,5)
print(len(x),x.size())
print(torch.cuda.is_available())
