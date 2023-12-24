import streamlit as st

from distribution_zoo import (
    get_random_animal_emoji,
    inject_custom_css
)

# All distributions should be imported here
from distribution_zoo.cont_uni import (
    Normal
)

# All imported distributions need to be in one of these lists
distributions_cont_uni = [
    Normal
]

distributions_disc_uni = [
]

distributions_mult = [
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

query_params = st.experimental_get_query_params()

selected_class_index = None
if 'dist_class' in query_params:
    selected_class_index = 0

selected_dist_index = None
if 'dist_name' in query_params:
    selected_dist_index = 0

inject_custom_css()

if st.sidebar.button(':house: Home'):
    st.experimental_set_query_params()
    st.rerun()
st.sidebar.title(f'Distribution Zoo  {zoo_animal}')

st.sidebar.header('Distribution class:')

distribution_classes = [
    'Continuous Univariate',
    'Discrete Univariate',
    'Multivariate',
]

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
                st.rerun()

    with col2:
        st.subheader('Discrete Univariate:')
        for dist in distributions_disc_uni:
            st.subheader(dist.display_name)

    with col3:
        st.subheader('Multivariate:')
        for dist in distributions_mult:
            st.subheader(dist.display_name)
