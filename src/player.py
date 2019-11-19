# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, items):
        self.name = name
        self.items = []
        self.current_room = "outside"
   
    def __str__(self):
        str = f"Name:: {self.name}, Current room is :: {self.current_room}, "
        str = str + "Items: {self.items}"
        return str

    def __repr__(self):
        str = f"Name:: {repr(self.name)}, Current room is :: "
        str = str + "{repr(self.current_room)}, Items: {self.items}"
        return str

    def get_items(self):
        return self.items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        new_list = []
        for i in self.items:
            if (i == item):
                new_list.append(item)
        print(f"\n\n ** The new items list for the player is {new_list}**")

    def set_current_room(self, current_room):
        self.current_room = current_room
