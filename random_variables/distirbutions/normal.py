from dataclasses import dataclass
from random_variables.random_variables import FiniteMeanMixin, FiniteVarianceMixin, RV


@dataclass
class Normal(RV, FiniteMeanMixin, FiniteVarianceMixin):
    pass