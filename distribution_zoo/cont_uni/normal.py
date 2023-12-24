from distribution_zoo import BaseDistribution
from distribution_zoo import language_display_name

import altair as alt
import numpy as np
import pandas as pd
import scipy.stats as stats
import streamlit as st


class Normal(BaseDistribution):

    display_name = 'Normal'
    range_min = -50.0
    range_max = 50.0
    param_range_start = -10.0
    param_range_end = 10.0
    param_mean = 0.0
    param_std = 1.0

    def __init__(self):
        super().__init__()

    def title(self):
        st.header(f'{self.display_name} distribution')

    def sliders(self):

        self.param_range_start, self.param_range_end = st.sidebar.slider(
            'Range', min_value=-50.0, max_value=50.0, value=(-10.0, 10.0), step=0.1
        )

        self.param_mean = st.sidebar.slider(
            r'Mean ($\mu$)', min_value=-30.0, max_value=30.0, value=0.0, step=0.1
        )

        self.param_std = st.sidebar.slider(
            r'Standard deviation ($\sigma$)', min_value=0.1, max_value=20.0, value=1.0, step=0.1
        )

    def plot(self):

        x = np.linspace(self.range_min, self.range_max, 1000)

        chart_data = pd.DataFrame(
            {
                'x': x,
                'pdf': stats.norm.pdf(x, loc=self.param_mean, scale=self.param_std),
                'cdf': stats.norm.cdf(x, loc=self.param_mean, scale=self.param_std),
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

    def info(self):

        self.update_code_substitutions()

        tab_titles = [
            'Formulae',
            r'$\LaTeX$',
            'Code',
            'Practical tips',
        ]

        formulae, latex, code, tips = st.tabs(tab_titles)

        with formulae:
            with open(self.data_dir / 'formulae.md', 'r') as f:
                st.markdown(f.read())

        with latex:
            with open(self.data_dir / 'latex.md', 'r') as f:
                st.markdown(f.read())

        with code:

            st.info('Code snippets are dynamically updated with the parameters', icon="ℹ️")

            all_code_files = list((self.data_dir / 'code').glob('*'))

            lang_names = [language_display_name(lang) for lang in all_code_files]

            lang_tabs = st.tabs(lang_names)

            for lang_tab, code_file in zip(lang_tabs, all_code_files):
                with open(code_file, 'r') as f:
                    markdown_text = f.read()
                    for old, new in self.code_substitutions:
                        markdown_text = markdown_text.replace(old, new)
                    lang_tab.markdown(markdown_text)

        with tips:
            with open(self.data_dir / 'tips.md', 'r') as f:
                st.markdown(f.read())

    def update_code_substitutions(self):
        self.code_substitutions = [
            (r'{{{mean}}}', str(self.param_mean)),
            (r'{{{std}}}', str(self.param_std)),
            (r'{{{range_start}}}', str(self.param_range_start)),
            (r'{{{range_end}}}', str(self.param_range_end)),
        ]
