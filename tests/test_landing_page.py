from streamlit.testing.v1 import AppTest

from utils import app_test

import re


def test_custom_css(app_test):
    css_container = app_test.main[0]
    assert len(css_container) == 1
    assert r'Targeting the tab button with a specific attribute and its inner <p> tag' in css_container.markdown[0].value


def test_landing_page(app_test):

    # The head container should only contain a title
    cont_head = app_test.main[1]
    assert len(cont_head) == 1
    assert cont_head.title[0].body == 'Explore the Distribution Zoo'

    # The body container should contain three cols
    cont_body = app_test.main[2]
    assert len(cont_body) == 1
    assert len(cont_body.columns) == 3

    # First col contains cont uni
    current_col = cont_body.columns[0]
    assert current_col.subheader[0].body == 'Continuous Univariate'
    assert current_col.button[0].label == 'Normal'
    assert current_col.button[1].label == 'Gamma'

    # Second col contains disc uni
    current_col = cont_body.columns[1]
    assert current_col.subheader[0].body == 'Discrete Univariate'

    # Third col contains multi
    current_col = cont_body.columns[2]
    assert current_col.subheader[0].body == 'Multivariate'

    # The footer contains author and analytics
    cont_foot = app_test.main[3]

    author_subheader = cont_foot.subheader[0]
    assert author_subheader.body == 'Authors:'
    assert 'Ben Lambert' in cont_foot.markdown[0].value
    assert 'Fergus Cooper' in cont_foot.markdown[0].value

    analytics_subheader = cont_foot.subheader[1]
    assert analytics_subheader.body == 'Analytics:'

    match = re.search(r'Last month: used by (\d+) people over (\d+) sessions in (\d+) countries', cont_foot.markdown[1].value)
    assert match is not None
    people, sessions, countries = map(int, match.groups())
    assert people > 0
    assert sessions > 0
    assert countries > 0

    match = re.search(r'Since created: used by (\d+) people over (\d+) sessions in (\d+) countries', cont_foot.markdown[1].value)
    assert match is not None
    people, sessions, countries = map(int, match.groups())
    assert people > 16123
    assert sessions > 29586
    assert countries > 132
