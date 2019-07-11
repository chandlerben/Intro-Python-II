# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def _get_item_string(self):
        if len(self.items) > 0:
            return "\n" + ", ".join([item.name for item in self.items]) + "\n"
        else:
            return ""

    def _get_exits_string(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.n_to is not None:
            exits.append("e")
        if self.n_to is not None:
            exits.append("w")
        if self.n_to is not None:
            exits.append("s")
        return "Exits:", "+ ".join(exits)

    def __str__(self):
        str = f"""\n-----------------------------------"
                \n\n{self.title}
                \n      {self.description}\n
                \n{self._get_exits_string()}\n
                \n{self._get_item_string()}\n"""

        return str
