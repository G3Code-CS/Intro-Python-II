class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Item :: {self.name}, Description :: {self.description}"

    def __repr__(self):
        str = f"Item :: {repr(self.name)}, Description ::"
        str = str + "{repr(self.description)}"
        return str
