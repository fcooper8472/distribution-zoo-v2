class DistributionClass:

    def __init__(self, display_name: str, short_name: str):
        self.display_name = display_name
        self.short_name = short_name

    def __eq__(self, other):
        if isinstance(other, DistributionClass):
            return self.display_name == other.display_name and self.short_name == other.short_name
        elif isinstance(other, str):
            return self.display_name == other or self.short_name == other
        return False

    def __hash__(self):
        return hash((self.display_name, self.short_name))

    def __str__(self):
        return self.display_name
