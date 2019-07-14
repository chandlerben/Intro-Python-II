# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_room, inventory):
        self.name = name
        self.current_room = starting_room
        self.inventory = []

    def travel(self, direction):
        # Check if there is a valid room in the direction
        if getattr(self.current_room, f"{direction}_to") is not None:
            # If so, update current room to new room and print description
            self.current_room = getattr(
                self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            # Else, print error message
            print("Sorry!  There is no room here.", "\n")

    def _print_inventory(self):
        if len(self.inventory) > 0:
            print("\nYou are carrying:\n   " +
                  ", ".join([item.name for item in self.inventory]) + "\n")
        else:
            print("You are carrying nothing.  Find some stuff to pick up!")
