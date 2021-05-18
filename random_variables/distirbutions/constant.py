from dataclasses import dataclass
from random_variables.random_variables import FiniteMeanMixin, RV


@dataclass
class Constant(RV, FiniteMeanMixin):
    pass