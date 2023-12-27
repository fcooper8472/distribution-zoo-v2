from distribution_zoo import BaseDistribution

import altair as alt
import numpy as np
import pandas as pd
import scipy.stats as stats
import streamlit as st


class Gamma(BaseDistribution):

    display_name = 'Gamma'
    range_min = 0.0
    range_max = 100.0
    param_range_start = 0.0
    param_range_end = 10.0
    param_shape = 0.0
    param_rate = 1.0

    def __init__(self):
        super().__init__()

    def sliders(self):

        self.param_range_start, self.param_range_end = st.sidebar.slider(
            'Range', min_value=self.range_min, max_value=self.range_max, value=(0.0, 10.0), step=0.1
        )

        self.param_shape = st.sidebar.slider(
            r'Shape ($\alpha$)', min_value=0.05, max_value=10.0, value=1.0, step=0.05
        )

        self.param_rate = st.sidebar.slider(
            r'Rate ($\beta$)', min_value=0.05, max_value=2.0, value=0.5, step=0.05
        )

    def plot(self):

        x = np.linspace(self.range_min, self.range_max, 1000)

        chart_data = pd.DataFrame(
            {
                'x': x,
                'pdf': stats.gamma.pdf(x, a=self.param_shape, loc=0.0, scale=1./self.param_rate),
                'cdf': stats.gamma.cdf(x, a=self.param_shape, loc=0.0, scale=1./self.param_rate),
            }
        )

        # Define the initial x-axis range for the view
        initial_x_range = [self.param_range_start, self.param_range_end]

        # Create an Altair chart for the PDF
        pdf_chart = alt.Chart(chart_data).mark_line().encode(
            x=alt.X('x:Q', scale=alt.Scale(domain=initial_x_range)),
            y='pdf:Q',
            tooltip=['x', 'pdf']
        ).interactive()

        # Create an Altair chart for the CDF
        cdf_chart = alt.Chart(chart_data).mark_line().encode(
            x=alt.X('x:Q', scale=alt.Scale(domain=initial_x_range)),
            y='cdf:Q',
            tooltip=['x', 'cdf']
        ).interactive()

        pdf_col, cdf_col = st.columns(2)

        with pdf_col:
            st.subheader('Probability density function')
            st.altair_chart(pdf_chart, use_container_width=True)
        with cdf_col:
            st.subheader('Cumulative distribution function')
            st.altair_chart(cdf_chart, use_container_width=True)

    def update_code_substitutions(self):
        pass
