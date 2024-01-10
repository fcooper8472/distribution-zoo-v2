from distribution_zoo import BaseDistribution

import plotly.graph_objects as go
import numpy as np
import pandas as pd
import scipy.stats as stats
import streamlit as st


class Poisson(BaseDistribution):

    display_name = 'Poisson'
    range_min = 0
    range_max = 100
    param_rate = st.session_state['poisson_rate'] if 'poisson_rate' in st.session_state else 10.0
    param_range_start = None
    param_range_end = None

    def __init__(self):
        super().__init__()

    def sliders(self):

        if 'poisson_range' not in st.session_state:
            self.update_range()

        # This slider's initial value is set from st.session_state['normal_range'], set with update_range()
        self.param_range_start, self.param_range_end = st.sidebar.slider(
            'Range', min_value=self.range_min, max_value=self.range_max, step=1, key='poisson_range'
        )

        self.param_rate = st.sidebar.slider(
            r'Rate', min_value=0.0, max_value=32.0, value=self.param_rate, step=0.1, key='poisson_rate',
            on_change=self.update_range
        )

    def update_range(self):

        rate = st.session_state['poisson_rate'] if 'poisson_rate' in st.session_state else self.param_rate

        new_lower = int(0)
        new_upper = int(min(1 + round(stats.poisson(mu=rate).ppf(0.999), 0), self.range_max))
        st.session_state['poisson_range'] = (new_lower, new_upper)

    def plot(self):
        x = range(self.param_range_start, self.param_range_end)

        chart_data = pd.DataFrame(
            {
                'x': x,
                'pmf': stats.poisson.pmf(x, mu=self.param_rate),
                'cdf': stats.poisson.cdf(x, mu=self.param_rate),
            }
        )

        line_data = pd.DataFrame(
            {
                'x': [self.param_rate, self.param_rate],
                'pmf': [0.0, max(chart_data['pmf'])],
                'cdf': [0.0, max(chart_data['cdf'])],
            }
        )

        # Create Plotly chart for the PDF
        pdf_chart = go.Figure(go.Bar(x=chart_data['x'], y=chart_data['pmf'], name='PMF'))
        pdf_chart.add_trace(go.Scatter(x=line_data['x'], y=line_data['pmf'], mode='lines', name=f'Mean ({self.param_rate})', line=dict(color='orange', width=2)))
        pdf_chart.update_layout(xaxis_title='x', yaxis_title='pmf', margin=dict(l=20, r=20, t=20, b=20))

        # Create Plotly chart for the CDF
        cdf_chart = go.Figure(go.Bar(x=chart_data['x'], y=chart_data['cdf'], name='CDF'))
        cdf_chart.add_trace(go.Scatter(x=line_data['x'], y=line_data['cdf'], mode='lines', name=f'Mean ({self.param_rate})', line=dict(color='orange', width=2)))
        cdf_chart.update_layout(xaxis_title='x', yaxis_title='cdf', margin=dict(l=20, r=20, t=20, b=20))

        # Streamlit columns for displaying the charts
        pdf_col, cdf_col = st.columns(2)

        with pdf_col:
            st.subheader('Probability mass function')
            st.plotly_chart(pdf_chart, use_container_width=True)

        with cdf_col:
            st.subheader('Cumulative distribution function')
            st.plotly_chart(cdf_chart, use_container_width=True)

    def update_code_substitutions(self):
        pass
