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

    def drop_item(self):
        print(f"\n You are dropping {self.name} in the current room")

    def take_item(self):
        print(f"\n You are taking {self.name} from the current room")


class Septre(Item):
    def __init__(self, name, description, material):
        super().__init__(name, description)
        self.material = material

    def __str__(self):
        return f"Item :: {self.name} : {self.description} : {self.material}"

    def __repr__(self):
        return f"Item :: {repr(self.name)} : {repr(self.description)} "


class Map(Item):
    def __init__(self, name, description, time_period):
        super().__init__(name, description)
        self.time_period = time_period

    def __str__(self):
        return f"Item :: {self.name} : {self.description} : {self.time_period}"

    def __repr__(self):
        return f"Item :: {repr(self.name)} : {repr(self.description)} "


class GoldCoins(Item):
    def __init__(self, name, description, count):
        super().__init__(name, description)
        self.count = count

    def __str__(self):
        return f"Item :: {self.name} : {self.description} : {self.count}"

    def __repr__(self):
        return f"Item :: {repr(self.name)} : {repr(self.description)} "


class HolyGrail(Item):
    def __init__(self, name, description, magical_properties):
        super().__init__(name, description)
        self.magical_properties = magical_properties

    def __str__(self):
        str = f"Item :: {self.name} : {self.description} :"
        return str + f" {self.magical_properties}"

    def __repr__(self):
        return f"Item :: {repr(self.name)} : {repr(self.description)} "
