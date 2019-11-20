# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def get_name(self):
        return self.name

    def __str__(self):
        str = f"Room: {self.name} :: Description: {self.description} ::"
        str = str + " Items: {self.items}"

    def __repr__(self):
        str = f"Room: ({repr(self.name)}), Description:"
        str = str + " ({repr(self.description)}), Items: ({repr(self.items)})"
        return str

    def print_items(self):
        for i in self.items:
            print(i)
        print("\n")

    def add_item(self, item):
        return self.items.append(item)

    def remove_items(self, item):
        new_list = []
        for i in self.items:
            if (i == item):
                new_list.append(item)
        self.items = new_list
        print(f"\n**The new list is {new_list}**\n")
