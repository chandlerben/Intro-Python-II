# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.items = []

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

    def put_item_in_pocket(self, item):
        print("You have activated Player Get Item function")
        self.items.append(item)
        print(f"You picked up {item}")

    def _print_inventory(self):
        if len(self.items) > 0:
            print("\nYou are carrying:\n   " +
                  ", ".join([item.name for item in self.items]) + "\n")
        else:
            print("You are carrying nothing.  Find some stuff to pick up!")
