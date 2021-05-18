from random_variables.random_variables import RVParameter
from dataclasses import dataclass

class DistributionMixin:
    pass

@dataclass
class FiniteMeanMixin(DistributionMixin):
    mean: RVParameter

@dataclass
class FiniteVarianceMixin(DistributionMixin):
    variance: RVParameter