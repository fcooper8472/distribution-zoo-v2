from pathlib import Path
import random
import streamlit as st

emoji_list = [
    ":ant:", ":badger:", ":bat:", ":bear:", ":beaver:", ":bee:", ":beetle:", ":bison:", ":black_cat:", ":blowfish:",
    ":boar:", ":bug:", ":butterfly:", ":camel:", ":cat:", ":chipmunk:", ":cockroach:", ":cow:", ":cricket:",
    ":crocodile:", ":deer:", ":dog:", ":dolphin:", ":dragon_face:", ":dragon:", ":elephant:", ":fish:", ":fly:",
    ":fox_face:", ":frog:", ":goat:", ":gorilla:", ":guide_dog:", ":hamster:", ":hedgehog:", ":hippopotamus:",
    ":horse:", ":kangaroo:", ":koala:", ":lady_beetle:", ":leopard:", ":lizard:", ":llama:", ":mammoth:", ":monkey:",
    ":mouse:", ":octopus:", ":orangutan:", ":otter:", ":ox:", ":panda_face:", ":pig:", ":polar_bear:", ":poodle:",
    ":rabbit:", ":raccoon:", ":racehorse:", ":ram:", ":rat:", ":rhinoceros:", ":sauropod:", ":scorpion:", ":seal:",
    ":service_dog:", ":shark:", ":sheep:", ":skunk:", ":sloth:", ":snail:", ":t-rex:", ":tiger:", ":tropical_fish:",
    ":turtle:", ":water_buffalo:", ":whale:", ":wolf:"
]


def get_random_animal_emoji():
    return random.choice(emoji_list)


def inject_custom_css():
    css_file = Path(__file__).parent.parent.resolve() / 'custom.css'
    with open(css_file, 'r') as f:
        st.markdown(f'''
        <style>
        {f.read()}
        </style>
        ''', unsafe_allow_html=True)


def language_display_name(language_file: Path) -> str:

    if language_file.stem == 'cpp':
        return 'C++'

    return language_file.stem.capitalize()


def get_indices_from_query_params(dist_mapping: dict):

    qp = st.experimental_get_query_params()

    if 'dist_class' not in qp:
        return None, None

    qp_class_list = qp['dist_class']
    if len(qp_class_list) != 1:
        return None, None
    qp_class = qp_class_list[0]

    try:
        class_index = [_class.short_name for _class in dist_mapping.keys()].index(qp_class)
    except ValueError:
        return None, None

    if 'dist_name' not in qp:
        return class_index, None

    qp_dist_list = qp['dist_name']
    if len(qp_dist_list) != 1:
        return class_index, None
    qp_dist = qp_dist_list[0]

    try:
        dist_index = [_dist.get_class_name() for _dist in list(dist_mapping.values())[class_index]].index(qp_dist)
    except ValueError:
        return class_index, None

    return class_index, dist_index
