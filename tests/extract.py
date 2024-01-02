from utils import at_normal
from utils import get_test_output_dir

import re


def test_extract_normal(at_normal):

    info_section = at_normal.main[4]
    code_section = info_section.tabs[2]
    assert code_section.label == 'Code'

    cpp_section = code_section[1].tabs[0]
    assert cpp_section.label == 'C++'

    pre_md = cpp_section[0].markdown[0].value
    code_md = cpp_section[1].value

    cpp_block_pattern = re.compile(r'```cpp(.*?)```', re.DOTALL)

    pre_code_matches = re.findall(cpp_block_pattern, pre_md)
    main_code_matches = re.findall(cpp_block_pattern, code_md)

    assert len(pre_code_matches) == 1
    assert len(main_code_matches) == 3

    code_dir = get_test_output_dir() / 'normal' / 'cpp'
    code_dir.mkdir(exist_ok=True, parents=True)

    with open(code_dir / 'pdf.cpp', 'w') as f:
        f.write(f'{pre_code_matches[0]}{main_code_matches[0]}')

    with open(code_dir / 'logpdf.cpp', 'w') as f:
        f.write(f'{pre_code_matches[0]}{main_code_matches[1]}')

    with open(code_dir / 'rvs.cpp', 'w') as f:
        f.write(f'{pre_code_matches[0]}{main_code_matches[2]}')


def test_code_files_exist():

    assert (get_test_output_dir() / 'normal' / 'cpp' / 'pdf.cpp').is_file()
    assert (get_test_output_dir() / 'normal' / 'cpp' / 'logpdf.cpp').is_file()
    assert (get_test_output_dir() / 'normal' / 'cpp' / 'rvs.cpp').is_file()

