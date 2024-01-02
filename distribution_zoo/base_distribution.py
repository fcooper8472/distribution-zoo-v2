from .utils import language_display_name
from .text_substitutions import TextSubstitutions

from inflection import underscore
from pathlib import Path

import streamlit as st

import inspect
import sys


class BaseDistribution:

    display_name: str = "Base distribution"

    code_substitutions: TextSubstitutions = TextSubstitutions()

    def __init__(self):
        # Get the module of the derived class
        module = sys.modules[self.__class__.__module__]
        # Get the file path of the module
        self.file_path = Path(inspect.getfile(module)).resolve()
        self.data_dir = self.file_path.parent / underscore(self.get_class_name())
        self.class_data_dir = self.data_dir.parent

    @classmethod
    def get_class_name(cls):
        return cls.__name__

    def display(self):
        self.title()
        st.sidebar.header('Parameters:')
        self.sliders()
        self.plot()
        st.divider()
        self.info()
        st.divider()

    def title(self):
        st.header(f'{self.display_name} distribution')

    def sliders(self):
        raise NotImplementedError(f'Sliders not implemented in subclass {self.get_class_name()} ({self.file_path})')

    def plot(self):
        raise NotImplementedError(f'Plot not implemented in subclass {self.get_class_name()} ({self.file_path})')

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
            formulae_file = self.data_dir / 'formulae.md'
            if formulae_file.exists():
                with open(formulae_file, 'r') as f:
                    st.markdown(f.read())
            else:
                st.write('No formulae yet...')

        with latex:
            latex_file = self.data_dir / 'latex.md'
            if latex_file.exists():
                with open(self.data_dir / 'latex.md', 'r') as f:
                    st.markdown(f.read())
            else:
                st.write('No LaTeX yet...')

        with code:

            all_code_files = sorted(list((self.data_dir / 'code').glob('*')))

            if len(all_code_files) > 0:

                st.info('Code snippets are dynamically updated with the parameters', icon="ℹ️")

                lang_names = [language_display_name(lang) for lang in all_code_files]

                lang_tabs = st.tabs(lang_names)

                for lang_tab, code_file in zip(lang_tabs, all_code_files):
                    class_lang_file = self.class_data_dir / 'code' / code_file.name
                    if class_lang_file.is_file():
                        with open(class_lang_file, 'r') as f:
                            expander = lang_tab.expander('Prerequisites')
                            expander.markdown(f.read())

                    lang_tab.markdown(self.code_substitutions.apply_to_file(code_file))

            else:
                st.write('No code yet...')

        with tips:
            tips_file = self.data_dir / 'tips.md'
            if tips_file.exists():
                with open(tips_file, 'r') as f:
                    st.markdown(f.read())
            else:
                st.write('No tips yet...')

    def update_code_substitutions(self):
        raise NotImplementedError(f'Code substitutions not implemented in subclass {self.get_class_name()} ({self.file_path})')
