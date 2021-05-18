from typing import Union
from .random_variables import TensorShape, TensorType
from dataclasses import dataclass


@dataclass
class ArbitraryParameter:
    name: str
    shape:TensorShape

@dataclass
class KnownParameter:
    value: TensorType
    shape: TensorShape

RVParameter = Union[ArbitraryParameter, KnownParameter]