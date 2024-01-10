from distribution_zoo import BaseDistribution

import plotly.graph_objects as go
import numpy as np
import pandas as pd
import scipy.stats as stats
import streamlit as st


class Gamma(BaseDistribution):

    display_name = 'Gamma'
    range_min = 0.0
    range_max = 150.0
    param_shape = st.session_state['gamma_shape'] if 'gamma_shape' in st.session_state else 1.0
    param_rate = st.session_state['gamma_rate'] if 'gamma_rate' in st.session_state else 0.5
    param_range_start = None
    param_range_end = None

    def __init__(self):
        super().__init__()

    def sliders(self):
        if 'gamma_range' not in st.session_state:
            self.update_range()

        # This slider's initial value is set from st.session_state['gamma_range'], set with update_range()
        self.param_range_start, self.param_range_end = st.sidebar.slider(
            'Range', min_value=self.range_min, max_value=self.range_max, value=(0.0, 10.0), step=0.1, key='gamma_range'
        )

        self.param_shape = st.sidebar.slider(
            r'Shape ($\alpha$)', min_value=0.05, max_value=10.0, value=self.param_shape, step=0.05, key='gamma_shape',
            on_change=self.update_range
        )

        self.param_rate = st.sidebar.slider(
            r'Rate ($\beta$)', min_value=0.2, max_value=2.0, value=self.param_rate, step=0.05, key='gamma_rate',
            on_change=self.update_range
        )

    def update_range(self):

        shape = st.session_state['gamma_shape'] if 'gamma_shape' in st.session_state else self.param_shape
        rate = st.session_state['gamma_rate'] if 'gamma_rate' in st.session_state else self.param_rate

        new_lower = 0.0
        new_upper = min(round(stats.gamma(a=shape, loc=0.0, scale=1. / rate).ppf(0.999), 1), self.range_max)
        st.session_state['gamma_range'] = (new_lower, new_upper)

    def plot(self):

        mean = self.param_shape / self.param_rate
        display_mean = round(mean, 2)

        x = np.linspace(self.param_range_start, self.param_range_end, 1000)

        chart_data = pd.DataFrame(
            {
                'x': x,
                'pdf': stats.gamma.pdf(x, a=self.param_shape, loc=0.0, scale=1. / self.param_rate),
                'cdf': stats.gamma.cdf(x, a=self.param_shape, loc=0.0, scale=1. / self.param_rate),
            }
        )

        line_data = pd.DataFrame(
            {
                'x': [mean, mean],
                'pdf': [0.0, max(chart_data['pdf'])],
                'cdf': [0.0, max(chart_data['cdf'])],
            }
        )

        # Create Plotly chart for the PDF
        pdf_chart = go.Figure(go.Scatter(x=chart_data['x'], y=chart_data['pdf'], mode='lines', name='PDF'))
        pdf_chart.add_trace(
            go.Scatter(x=line_data['x'], y=line_data['pdf'], mode='lines', name=f'Mean ({display_mean})',
                       line=dict(color='orange', width=2)))
        pdf_chart.update_layout(xaxis_title='x', yaxis_title='pdf', margin=dict(l=20, r=20, t=20, b=20))

        # Create Plotly chart for the CDF
        cdf_chart = go.Figure(go.Scatter(x=chart_data['x'], y=chart_data['cdf'], mode='lines', name='CDF'))
        cdf_chart.add_trace(
            go.Scatter(x=line_data['x'], y=line_data['cdf'], mode='lines', name=f'Mean ({display_mean})',
                       line=dict(color='orange', width=2)))
        cdf_chart.update_layout(xaxis_title='x', yaxis_title='cdf', margin=dict(l=20, r=20, t=20, b=20))

        # Streamlit columns for displaying the charts
        pdf_col, cdf_col = st.columns(2)

        with pdf_col:
            st.subheader('Probability density function')
            st.plotly_chart(pdf_chart, use_container_width=True)

        with cdf_col:
            st.subheader('Cumulative distribution function')
            st.plotly_chart(cdf_chart, use_container_width=True)

    def update_code_substitutions(self):
        pass
