from pathlib import Path


class Lang:
    d_names = {}
    exts = {}
    fences = {}

    def __init__(self, d_name, ext, fence):
        self.d_name = d_name
        self.ext = ext
        self.fence = fence
        Lang.d_names[d_name] = self
        Lang.exts[ext] = self
        Lang.fences[fence] = self

    @classmethod
    def convert(cls, input_str: str, input_type: str, output_type: str):

        assert input_type in ['d_name', 'ext', 'fence']
        assert output_type in ['d_name', 'ext', 'fence']

        if input_type == 'd_name':
            language = cls.d_names.get(input_str)
        elif input_type == 'ext':
            language = cls.exts.get(input_str)
        else:  # input_type == 'fence'
            language = cls.fences.get(input_str)

        return getattr(language, output_type)

    @classmethod
    def convert_from_path(cls, input_path: Path, output_type: str):
        return cls.convert(input_str=input_path.suffix, input_type='ext', output_type=output_type)


Lang(d_name='C++', ext='.cpp', fence='cpp')
Lang(d_name='Julia', ext='.jl', fence='julia')
Lang(d_name='Mathematica', ext='.wl', fence='mathematica')
Lang(d_name='MATLAB', ext='.m', fence='matlab')
Lang(d_name='Python', ext='.py', fence='python')
Lang(d_name='R', ext='.R', fence='r')
Lang(d_name='Stan', ext='.stan', fence='stan')
