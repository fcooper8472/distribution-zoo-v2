from inflection import underscore
from pathlib import Path

import streamlit as st

import inspect
import sys


class BaseDistribution:

    display_name = "Base distribution"

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
        raise NotImplementedError(f'Info not implemented in subclass {self.name} ({self.file_path})')
