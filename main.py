import json
import requests
import streamlit as st
import time
from pathlib import Path

from distribution_zoo import (
    get_random_animal_emoji,
    inject_custom_css,
    get_indices_from_query_params,
    TextSubstitutions,
    dist_mapping,
)

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

selected_class_index, selected_dist_index = get_indices_from_query_params(dist_mapping)

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
    index=selected_class_index,
    placeholder='Select a distribution class',
    label_visibility='collapsed',
    key='dist_class',
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
    label_visibility='collapsed',
    key='dist',
)

if selected_dist:
    selected_dist_inst = selected_dist()
    selected_dist_inst.display()
else:

    with st.container():
        st.title('Explore the Distribution Zoo')

    with st.container():
        cols = st.columns(len(dist_mapping.keys()))

        for col, key in zip(cols, dist_mapping.keys()):
            col.subheader(key.display_name)

            for dist in dist_mapping[key]:
                if col.button(dist.display_name):
                    st.experimental_set_query_params(
                        dist_class=key.short_name,
                        dist_name=dist.get_class_name(),
                    )
                    time.sleep(0.05)
                    st.rerun()

    with st.container():
        st.subheader('Authors:')
        st.markdown(TextSubstitutions().apply_to_file(Path('homepage_authors.md')))

        response_1 = requests.get('https://fcooper8472.github.io/distribution-zoo-analytics/data_30.json')
        response_2 = requests.get('https://fcooper8472.github.io/distribution-zoo-analytics/data_all_time.json')

        if response_1.status_code == 200 and response_2.status_code == 200:

            data_month = json.loads(response_1.text)
            data_all_time = json.loads(response_2.text)

            substitutions = TextSubstitutions()
            substitutions.add(r'{{{month_users}}}', str(data_month['user_count']))
            substitutions.add(r'{{{month_sessions}}}', str(data_month['session_count']))
            substitutions.add(r'{{{month_countries}}}', str(data_month['country_count']))
            substitutions.add(r'{{{all_users}}}', str(data_all_time['user_count']))
            substitutions.add(r'{{{all_sessions}}}', str(data_all_time['session_count']))
            substitutions.add(r'{{{all_countries}}}', str(data_all_time['country_count']))

            st.subheader('Analytics:')
            st.markdown(substitutions.apply_to_file(Path('homepage_analytics.md')))
