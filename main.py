import streamlit as st
import time

from distribution_zoo import (
    get_random_animal_emoji,
    inject_custom_css,
    get_indices_from_query_params,
)

# All distributions should be imported here
from distribution_zoo.cont_uni import (
    Normal,
    Gamma,
)

# All imported distributions need to be in one of these lists
distributions_cont_uni = [
    Normal,
    Gamma,
]

distributions_disc_uni = [
]

distributions_mult = [
]

distribution_classes = [
    'Continuous Univariate',
    'Discrete Univariate',
    'Multivariate',
]

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

selected_class_index, selected_dist_index = get_indices_from_query_params(distribution_classes, distributions_cont_uni, distributions_disc_uni, distributions_mult)

inject_custom_css()

if st.sidebar.button(':house: Home'):
    st.experimental_set_query_params()
    time.sleep(0.05)
    st.rerun()
st.sidebar.title(f'Distribution Zoo  {zoo_animal}')

st.sidebar.header('Distribution class:')

selected_class = st.sidebar.selectbox(
    label='Select a distribution class',
    options=distribution_classes,
    index=selected_class_index,
    placeholder='Select a distribution class',
    label_visibility='collapsed'
)

st.sidebar.header('Distribution:')

if selected_class == 'Continuous Univariate':
    distributions = distributions_cont_uni
elif selected_class == 'Discrete Univariate':
    distributions = distributions_disc_uni
elif selected_class == 'Multivariate':
    distributions = distributions_mult
else:
    distributions = []

selected_dist = st.sidebar.selectbox(
    label='Select a distribution',
    options=distributions,
    format_func=lambda dist: dist.display_name,
    index=selected_dist_index,
    placeholder='Select a distribution',
    label_visibility='collapsed'
)

if selected_dist:
    selected_dist_inst = selected_dist()
    selected_dist_inst.display()
else:

    st.title('Explore the Distribution Zoo')

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader('Continuous Univariate:')
        for dist in distributions_cont_uni:
            if st.button(dist.display_name):
                st.experimental_set_query_params(
                    dist_class='cont_uni',
                    dist_name=dist.__name__,
                )
                time.sleep(0.05)
                st.rerun()

    with col2:
        st.subheader('Discrete Univariate:')
        for dist in distributions_disc_uni:
            st.subheader(dist.display_name)

    with col3:
        st.subheader('Multivariate:')
        for dist in distributions_mult:
            st.subheader(dist.display_name)
