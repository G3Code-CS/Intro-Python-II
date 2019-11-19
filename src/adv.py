from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player_name = input('\nPlease input your name to start the game: ')
np = Player(player_name, [])
print(f"\nLet's start playing, {player_name}! Good Luck :)")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


is_done_playing = False


def possible_rooms(current_room):
    input_str = "You can choose one of following room(s) to move - \n"
    if (current_room == 'outside'):
        input_str += "\n(n)orth to Foyer"
    elif (current_room == 'foyer'):
        input_str += "\n(n)orth to overlook\n (s)outh to outside"
        input_str += "\n(e)ast to narrow"
    elif (current_room == 'overlook'):
        input_str += "\n(s)outh to foyer"
    elif (current_room == 'narrow'):
        input_str += "\n(w)est to foyer\n(n)orth to treasure"
    elif (current_room == 'treasure'):
        input_str += "\n(s)outh to narrow"
    return input_str+"\n(q)uit to end game\n\nEnter your input:"


while (is_done_playing is False):
    print("\n----------------------------------------------------------------")
    print(f"\n{np.name}, u r currently in {room[np.current_room].name}")
    print(f"\n{room[np.current_room].description}")
    print("\n----------------------------------------------------------------")
    input_str = possible_rooms(np.current_room)
    user_input = input(f"\n{input_str}").lower().strip()[0]
    if (user_input.lower() == 'q'):
        is_done_playing = True
        break
    elif (user_input.lower() == 'n'):
        np.set_current_room(((room[np.current_room].n_to).name)
                            .lower().partition(' ')[0])
    elif (user_input.lower() == 's'):
        np.set_current_room(((room[np.current_room].s_to).name).lower()
                            .partition(' ')[0])
    elif (user_input.lower() == 'e'):
        np.set_current_room(((room[np.current_room].e_to).name).lower()
                            .partition(' ')[0])
    elif (user_input.lower() == 'w'):
        np.set_current_room(((room[np.current_room].w_to).name).lower()
                            .partition(' ')[0])

    if (np.current_room == 'grand'):
        np.set_current_room('overlook')

    print(f"\n\n The current room is {np.current_room}")

print(f"\nAdios!! Thank you for playing, {np.name}. Come back soon!")
