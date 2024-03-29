from pathlib import Path
import numpy as np
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
        css_container = st.container()
        css_container.markdown(f'''
<style>
{f.read()}
</style>
''', unsafe_allow_html=True)


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


@st.cache_data
def unit_simplex_3d_uniform_cover(depth=3):
    """
    Uniformly cover the 3d unit simplex X+Y+Z=1 in a generative way, by repeatedly splitting the triangle into
    four smaller triangles, and calculating the centre of each. This means that 4^depth samples will be generated.

    This function avoids using random sampling, and creates a geometrically uniform cover. It is used primarily
    to create the points on which to calculate the 3d Dirichlet distribution PDF.

    Args:
        depth: Maximum depth of the subdivision.

    Returns:
        A NumPy array of shape (3, 4^{depth}) containing the simplex points.
    """
    # Define the unit simplex vertices
    simplex_vertices = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    # Initialize with the first level of subdivision
    triangles = [simplex_vertices]

    for _ in range(depth):
        new_triangles = []
        for triangle in triangles:
            midpoint1 = (triangle[0] + triangle[1]) / 2
            midpoint2 = (triangle[0] + triangle[2]) / 2
            midpoint3 = (triangle[1] + triangle[2]) / 2

            new_triangles.extend([
                [triangle[0], midpoint1, midpoint2],
                [triangle[1], midpoint1, midpoint3],
                [triangle[2], midpoint2, midpoint3],
                [midpoint1, midpoint2, midpoint3]
            ])

        triangles = new_triangles

    # Compute centroids of final triangles
    points = np.array([np.mean(triangle, axis=0) for triangle in triangles])

    # Transpose, because the Dirichlet PDF function wants the samples this way around. (This is unusual.)
    return points.T
