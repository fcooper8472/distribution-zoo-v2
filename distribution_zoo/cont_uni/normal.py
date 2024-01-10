from distribution_zoo import BaseDistribution

import plotly.graph_objects as go
import numpy as np
import pandas as pd
import scipy.stats as stats
import streamlit as st


class Normal(BaseDistribution):

    display_name = 'Normal'
    range_min = -50.0
    range_max = 50.0
    param_mean = st.session_state['normal_mean'] if 'normal_mean' in st.session_state else 0.0
    param_std = st.session_state['normal_std'] if 'normal_std' in st.session_state else 1.0
    param_range_start = None
    param_range_end = None

    def __init__(self):
        super().__init__()

    def sliders(self):

        if 'normal_range' not in st.session_state:
            self.update_range()

        # This slider's initial value is set from st.session_state['normal_range'], set with update_range()
        self.param_range_start, self.param_range_end = st.sidebar.slider(
            'Range', min_value=self.range_min, max_value=self.range_max, step=0.1, key='normal_range'
        )

        self.param_mean = st.sidebar.slider(
            r'Mean ($\mu$)', min_value=-16.0, max_value=16.0, value=self.param_mean, step=0.1, key='normal_mean',
            on_change=self.update_range
        )

        self.param_std = st.sidebar.slider(
            r'Standard deviation ($\sigma$)', min_value=0.1, max_value=8.0, value=self.param_std, step=0.1,
            key='normal_std', on_change=self.update_range
        )

    def update_range(self):

        mean = st.session_state['normal_mean'] if 'normal_mean' in st.session_state else self.param_mean
        std = st.session_state['normal_std'] if 'normal_std' in st.session_state else self.param_std

        new_lower = max(round(stats.norm(loc=mean, scale=std).ppf(0.0001), 1), self.range_min)
        new_upper = min(round(stats.norm(loc=mean, scale=std).ppf(0.9999), 1), self.range_max)
        st.session_state['normal_range'] = (new_lower, new_upper)

    def plot(self):
        x = np.linspace(self.param_range_start, self.param_range_end, 1000)

        chart_data = pd.DataFrame(
            {
                'x': x,
                'pdf': stats.norm.pdf(x, loc=self.param_mean, scale=self.param_std),
                'cdf': stats.norm.cdf(x, loc=self.param_mean, scale=self.param_std),
            }
        )

        line_data = pd.DataFrame(
            {
                'x': [self.param_mean, self.param_mean],
                'z': [0.0, 0.0],
                'pdf': [0.0, max(chart_data['pdf'])],
                'cdf': [0.0, max(chart_data['cdf'])],
            }
        )

        # Create Plotly chart for the PDF
        pdf_chart = go.Figure(go.Scatter(x=chart_data['x'], y=chart_data['pdf'], mode='lines', name='PDF'))
        pdf_chart.add_trace(go.Scatter(x=line_data['x'], y=line_data['pdf'], mode='lines', name=f'Mean ({self.param_mean})', line=dict(color='orange', width=2)))
        pdf_chart.add_trace(go.Scatter(x=line_data['z'], y=line_data['pdf'], mode='lines', name='Zero', line=dict(color='green', width=2, dash='dot')))
        pdf_chart.update_layout(xaxis_title='x', yaxis_title='pdf', margin=dict(l=20, r=20, t=20, b=20))

        # Create Plotly chart for the CDF
        cdf_chart = go.Figure(go.Scatter(x=chart_data['x'], y=chart_data['cdf'], mode='lines', name='CDF'))
        cdf_chart.add_trace(go.Scatter(x=line_data['x'], y=line_data['cdf'], mode='lines', name=f'Mean ({self.param_mean})', line=dict(color='orange', width=2)))
        cdf_chart.add_trace(go.Scatter(x=line_data['z'], y=line_data['cdf'], mode='lines', name=r'Zero', line=dict(color='green', width=2, dash='dot')))
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
        self.code_substitutions.add(r'{{{mean}}}', str(self.param_mean))
        self.code_substitutions.add(r'{{{std}}}', str(self.param_std))
        self.code_substitutions.add(r'{{{range_start}}}', str(self.param_range_start))
        self.code_substitutions.add(r'{{{range_end}}}', str(self.param_range_end))
