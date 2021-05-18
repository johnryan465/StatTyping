from abc import ABC
from typing import Generic, TypeVar, Union
from dataclasses import dataclass
import torch
from torch._C import TensorType

TensorType = torch.TensorType
TensorShape = torch.Size


class RV(ABC):
    pass

T = TypeVar('T', bound=RV)

@dataclass
class Sample(Generic[T]):
    base_tensor: TensorType
    base_cls: T
