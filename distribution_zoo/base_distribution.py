from .utils import language_display_name

from inflection import underscore
from pathlib import Path

import streamlit as st

import inspect
import sys


class BaseDistribution:

    display_name: str = "Base distribution"

    code_substitutions: list[tuple[str, str]] = []

    def __init__(self):
        self.name = self.__class__.__name__

        # Get the module of the derived class
        module = sys.modules[self.__class__.__module__]
        # Get the file path of the module
        self.file_path = Path(inspect.getfile(module)).resolve()
        self.data_dir = self.file_path.parent / underscore(self.name)

    def display(self):
        self.title()
        st.sidebar.header('Parameters:')
        self.sliders()

        self.plot()
        st.divider()
        self.info()
        st.divider()

    def title(self):
        raise NotImplementedError(f'Title not implemented in subclass {self.name} ({self.file_path})')

    def sliders(self):
        raise NotImplementedError(f'Sliders not implemented in subclass {self.name} ({self.file_path})')

    def plot(self):
        raise NotImplementedError(f'Plot not implemented in subclass {self.name} ({self.file_path})')

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
        raise NotImplementedError(f'Code substitutions not implemented in subclass {self.name} ({self.file_path})')
