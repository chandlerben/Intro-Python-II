# Implement a class to hold room information. This should have name and
# description attributes.
from player import Player


class Room:
    def __init__(self, title, description, items):
        self.title = title
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        str = f"""\n-----------------------------------"
                \n\n    {self.title}
                \n      {self.description}\n
                {self._see_item_string()}
                \n{self._get_exits_string()}\n"""
        return str

    def _see_item_string(self):
        if len(self.items) > 0:
            return "\nYou can see a " + ", ".join([item.name for item in self.items]) + "\n"
        else:
            return ""

    def get_item_string(self, direct_object):
        item_list = [old_item.name for old_item in self.items]
        print(item_list)
        if direct_object in item_list:
            for item in self.items:
                if item.name == direct_object:
                    del self.items.direct_object
            print("Should have worked.")
            return True
        else:
            print("That item does NOT exist")
            return False

    def _get_exits_string(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.e_to is not None:
            exits.append("e")
        if self.w_to is not None:
            exits.append("w")
        if self.s_to is not None:
            exits.append("s")
        return "Exits: " + ", ".join(exits)
