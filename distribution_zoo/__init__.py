from .base_distribution import BaseDistribution
from .distribution_class import DistributionClass
from .text_substitutions import TextSubstitutions
from .lang import Lang

from .utils import get_random_animal_emoji
from .utils import inject_custom_css
from .utils import get_indices_from_query_params
from .utils import unit_simplex_3d_uniform_cover

from .cont_uni import (
    Normal,
    Gamma,
)

from .disc_uni import (
    Poisson,
)

from .mult import (
    Dirichlet,
)

dist_mapping = {
    DistributionClass('Continuous Univariate', 'cont_uni'): [
        Normal(),
        Gamma(),
    ],
    DistributionClass('Discrete Univariate', 'disc_uni'): [
        Poisson(),
    ],
    DistributionClass('Multivariate', 'mult'): [
        Dirichlet(),
    ],
}
