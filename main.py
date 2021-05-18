import torch
from random_variables.random_variables import KnownParameter
from random_variables.distirbutions.normal import Normal

mean = KnownParameter(value=torch.zeros((1)), shape=torch.Size((1,)))
variance = KnownParameter(value=torch.ones((1)), shape=torch.Size((1,)))

rv = Normal(mean=mean, variance=variance)
print(rv)