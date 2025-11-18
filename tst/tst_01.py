import torch
import numpy as np

from array_print_shape import enable_torch_shape

enable_torch_shape()
a = torch.tensor([0, 1, 2, 3])
print(a)
