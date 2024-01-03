from streamlit.testing.v1 import AppTest
from streamlit.testing.v1.element_tree import Tab

from distribution_zoo import Lang

from utils import at_normal
from utils import get_test_output_dir

import json
import random
import re


def save_params(params: dict, dist_name: str) -> None:
    params_dir = get_test_output_dir() / dist_name
    params_dir.mkdir(parents=True, exist_ok=True)

    with open(params_dir / 'params.json', 'w') as f:
        json.dump(params, f, indent=2)


def extract_blocks_from_code_tab(code_tab: Tab, dist_name: str) -> None:
    lang_d_name = code_tab.label
    lang_fence = Lang.convert(lang_d_name, input_type='d_name', output_type='fence')
    lang_ext = Lang.convert(lang_d_name, input_type='d_name', output_type='ext')

    code_dir = get_test_output_dir() / dist_name / lang_fence
    code_dir.mkdir(parents=True, exist_ok=True)

    block_pattern = re.compile(f'```{lang_fence}(.*?)```', re.DOTALL)

    pre_md = code_tab.markdown[0].value
    code_md = code_tab.markdown[1].value

    pre_matches = re.findall(block_pattern, pre_md)
    code_matches = re.findall(block_pattern, code_md)

    assert len(pre_matches) == 1 or len(pre_matches) == 0
    assert len(code_matches) == 3

    pre = pre_matches[0] if pre_matches else ''

    with open(code_dir / f'pdf{lang_ext}', 'w') as f:
        f.write(f'{pre}{code_matches[0]}')

    with open(code_dir / f'logpdf{lang_ext}', 'w') as f:
        f.write(f'{pre}{code_matches[1]}')

    with open(code_dir / f'rvs{lang_ext}', 'w') as f:
        f.write(f'{pre}{code_matches[2]}')


def test_extract_normal(at_normal: AppTest):

    test_params = {
        'param_range_start': round(random.uniform(-10.0, -5.0), 1),
        'param_range_end': round(random.uniform(5.0, 10.0), 1),
        'param_mean': round(random.uniform(-5.0, 5.0), 1),
        'param_std': round(random.uniform(0.5, 15.0), 1),
    }

    save_params(test_params, 'normal')

    at_normal.slider(key='normal_range').set_value((test_params['param_range_start'], test_params['param_range_end'])).run()
    at_normal.slider(key='normal_mean').set_value(test_params['param_mean']).run()
    at_normal.slider(key='normal_std').set_value(test_params['param_std']).run()

    info_section = at_normal.main[4]
    code_section = info_section.tabs[2]
    assert code_section.label == 'Code'

    for tab in code_section[1].tabs:
        extract_blocks_from_code_tab(tab, 'normal')

    assert (get_test_output_dir() / 'normal' / 'params.json').is_file()

    for fence in ['cpp', 'python']:
        ext = Lang.convert(fence, input_type='fence', output_type='ext')
        assert (get_test_output_dir() / 'normal' / fence / f'pdf{ext}').is_file()
        assert (get_test_output_dir() / 'normal' / fence / f'logpdf{ext}').is_file()
        assert (get_test_output_dir() / 'normal' / fence / f'rvs{ext}').is_file()
