from pathlib import Path


class TextSubstitutions:
    def __init__(self):
        self.subs = dict()

    def add(self, old: str, new: str):
        self.subs[old] = new

    def apply_to_file(self, file_path: Path) -> str:
        assert file_path.exists()

        with open(file_path, 'r') as f:
            content = f.read()
            for old, new in self.subs.items():
                content = content.replace(old, new)
        return content
