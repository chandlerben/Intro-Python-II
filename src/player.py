# Write a class to hold player information, e.g. what room they are in
# currently.


def print_room(room):
    print(f"\n-----------------------------------")
    print(f"\n\n{room.title}")
    print(f"\n{room.description}\n")


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
            print_room(self.current_room)
        else:
            # Else, print error message
            print("Sorry!  There is no room here.", "\n")
