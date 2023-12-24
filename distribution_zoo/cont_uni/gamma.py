from distribution_zoo import BaseDistribution

import altair as alt
import numpy as np
import pandas as pd
import scipy.stats as stats
import streamlit as st


class Gamma(BaseDistribution):

    display_name = 'Gamma'

    def __init__(self):
        super().__init__()

    def sliders(self):
        pass

    def plot(self):
        pass

    def update_code_substitutions(self):
        pass
