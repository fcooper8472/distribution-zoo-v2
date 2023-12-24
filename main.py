import streamlit as st
import time

from distribution_zoo import (
    get_random_animal_emoji,
    inject_custom_css,
    get_indices_from_query_params,
    DistributionClass
)

# All distributions should be imported here
from distribution_zoo.cont_uni import (
    Normal,
    Gamma,
)

dist_mapping = {
    DistributionClass('Continuous Univariate', 'cont_uni'): [
        Normal,
        Gamma,
    ],
    DistributionClass('Discrete Univariate', 'disc_uni'): [
    ],
    DistributionClass('Multivariate', 'mult'): [
    ],
}

zoo_animal = get_random_animal_emoji()

st.set_page_config(
    page_title="Distribution Zoo",
    page_icon=zoo_animal,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# selected_class_index, selected_dist_index = get_indices_from_query_params(distribution_classes, distributions_cont_uni, distributions_disc_uni, distributions_mult)
selected_class_index, selected_dist_index = None, None

inject_custom_css()

if st.sidebar.button(':house: Home'):
    st.experimental_set_query_params()
    time.sleep(0.05)
    st.rerun()
st.sidebar.title(f'Distribution Zoo  {zoo_animal}')

st.sidebar.header('Distribution class:')

selected_class = st.sidebar.selectbox(
    label='Select a distribution class',
    options=dist_mapping.keys(),
    format_func=lambda _dist_class: _dist_class.display_name,
    index=selected_class_index,
    placeholder='Select a distribution class',
    label_visibility='collapsed'
)

st.sidebar.header('Distribution:')

if selected_class:
    available_dists = dist_mapping[selected_class]
else:
    available_dists = []

selected_dist = st.sidebar.selectbox(
    label='Select a distribution',
    options=available_dists,
    format_func=lambda _dist: _dist.display_name,
    index=selected_dist_index,
    placeholder='Select a distribution',
    label_visibility='collapsed'
)

if selected_dist:
    selected_dist_inst = selected_dist()
    selected_dist_inst.display()
else:

    st.title('Explore the Distribution Zoo')

    cols = st.columns(len(dist_mapping.keys()))

    for col, key in zip(cols, dist_mapping.keys()):
        col.subheader(key.display_name)

        for dist in dist_mapping[key]:
            if st.button(dist.display_name):
                st.experimental_set_query_params(
                    dist_class=key.short_name,
                    dist_name=dist.get_class_name(),
                )
                time.sleep(0.05)
                st.rerun()
