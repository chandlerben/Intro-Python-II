# Implement a class to hold room information. This should have name and
# description attributes.
from player import Player


class Room:
    def __init__(self, title, description, loot):
        self.title = title
        self.description = description
        self.loot = loot
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        str = f"""\n-----------------------------------"
                \n\n    {self.title}
                \n      {self.description}\n
                \n{self._get_exits_string()}\n"""
        return str

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
