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
