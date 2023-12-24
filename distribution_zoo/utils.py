import pathlib
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
    css_file = pathlib.Path(__file__).parent.parent.resolve() / 'custom.css'
    with open(css_file, 'r') as f:
        st.markdown(f'''
        <style>
        {f.read()}
        </style>
        ''', unsafe_allow_html=True)


def language_display_name(language_file: pathlib.Path) -> str:
    return language_file.stem.capitalize()


def get_indices_from_query_params(classes: list[str], cont_uni: list, disc_uni: list, mult: list):

    qp = st.experimental_get_query_params()

    if 'dist_class' not in qp:
        return None, None

    qp_class_list = qp['dist_class']
    if len(qp_class_list) != 1:
        return None, None
    qp_class = qp_class_list[0]

    if qp_class not in ['cont_uni', 'disc_uni', 'mult']:
        return None, None

    class_index = 0
    for i, class_name in enumerate(classes):
        if qp_class[0] == class_name.lower():
            class_index = i
            break

    if 'dist_name' not in qp:
        return class_index, None

    qp_dist_list = qp['dist_name']
    if len(qp_dist_list) != 1:
        return class_index, None
    qp_dist = qp_dist_list[0]

    if qp_class == 'cont_uni':
        dists = cont_uni
    elif qp_class == 'disc_uni':
        dists = disc_uni
    elif qp_class == 'mult':
        dists = mult
    else:
        dists = []

    dist_index = -1
    for i, dist in enumerate(dists):
        if qp_dist == dist.get_class_name():
            dist_index = i
            break

    if dist_index == -1:
        return class_index, None

    return class_index, dist_index
