from distribution_zoo import BaseDistribution
from distribution_zoo import unit_simplex_3d_uniform_cover

import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import pickle
import scipy.stats as stats
import streamlit as st


class Dirichlet(BaseDistribution):

    display_name = 'Dirichlet'
    param_dim = st.session_state['dirichlet_dim'] if 'dirichlet_dim' in st.session_state else 3
    param_a1 = st.session_state['dirichlet_a1'] if 'dirichlet_a1' in st.session_state else 2.0
    param_a2 = st.session_state['dirichlet_a2'] if 'dirichlet_a2' in st.session_state else 2.0
    param_a3 = st.session_state['dirichlet_a3'] if 'dirichlet_a3' in st.session_state else 2.0
    param_a4 = st.session_state['dirichlet_a4'] if 'dirichlet_a4' in st.session_state else 2.0

    def __init__(self):
        super().__init__()

    def sliders(self):

        self.param_dim = st.sidebar.slider(
            r'Dimension', min_value=2, max_value=4, value=self.param_dim, step=1, key='dirichlet_dim'
        )

        self.param_a1 = st.sidebar.slider(
            r'Concentration $\alpha_1$', min_value=0.1, max_value=10.0, value=self.param_a1, step=0.1, key='dirichlet_a1'
        )

        self.param_a2 = st.sidebar.slider(
            r'Concentration $\alpha_2$', min_value=0.1, max_value=10.0, value=self.param_a2, step=0.1, key='dirichlet_a2'
        )

        if self.param_dim > 2:
            self.param_a3 = st.sidebar.slider(
                r'Concentration $\alpha_3$', min_value=0.1, max_value=10.0, value=self.param_a3, step=0.1, key='dirichlet_a3'
            )

        if self.param_dim > 3:
            self.param_a4 = st.sidebar.slider(
                r'Concentration $\alpha_4$', min_value=0.1, max_value=10.0, value=self.param_a4, step=0.1, key='dirichlet_a4'
            )

    def plot(self):

        if self.param_dim == 2:
            self.plot_2d()
        elif self.param_dim == 3:
            self.plot_3d()
        else:  # self.param_dim == 4:
            self.plot_4d()

    def plot_2d(self):
        pass

    def plot_3d(self):

        sample_points = unit_simplex_3d_uniform_cover(4)

        samples = stats.dirichlet.pdf(sample_points, [self.param_a1, self.param_a2, self.param_a3])

        # Create a 3D scatter plot
        pdf_chart = ff.create_ternary_contour(
            coordinates=sample_points,
            values=samples,
            pole_labels=['α1', 'α2', 'α3'],
            colorscale='Cividis',
            ncontours=128,
            showscale=True,
            # linecolor='blue',
        )
        for i in range(len(pdf_chart.data)):
            pdf_chart.data[i].line.width = 0

        # Display the plot in Streamlit
        st.plotly_chart(pdf_chart)

    def plot_4d(self):
        st.info('Plot is not available for the 4-dimensional Dirichlet distribution', icon="ℹ️")

    def update_code_substitutions(self):
        pass
