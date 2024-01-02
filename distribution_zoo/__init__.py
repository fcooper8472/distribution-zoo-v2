from .base_distribution import BaseDistribution
from .distribution_class import DistributionClass
from .text_substitutions import TextSubstitutions

from .utils import get_random_animal_emoji
from .utils import inject_custom_css
from .utils import language_display_name
from .utils import get_indices_from_query_params

from .cont_uni import (
    Normal,
    Gamma,
)

dist_mapping = {
    DistributionClass('Continuous Univariate', 'cont_uni'): [
        Normal,
        Gamma,
    ],
    DistributionClass('Discrete Univariate', 'disc_uni'): [
    ],
    DistributionClass('Multivariate', 'mult'): [
    ],
}
