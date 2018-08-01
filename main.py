# constants
# cell discovered types
UNKNOWN = "X"
KNOWN = "O"

# game state
GS_MENU = "MENU"
GS_PLAY = "PLAY"
GS_LEAVE = "LEAVE"
state = {
    "game_state": GS_MENU,
    "move": None
}

# player input
player_input = ""

BOARD_SIZE = 10
BOARD_PADDING = 4

def handle_input(player_input, curr_state):
    new_state = {
        "game_state": curr_state["game_state"],
        "move": curr_state["move"]
    }

    player_input = player_input.upper()

    # game state changes
    if player_input == GS_LEAVE or player_input == GS_MENU:
        new_state["game_state"] = player_input

    return new_state

def init_board():
    return [
        [
            {"known": False} for i in range(BOARD_SIZE)
        ] for j in range(BOARD_SIZE)
    ]

def print_board(board):
    # print column markers
    col_label = ""
    for i in range(len(board[0])):
        col_label += str(i)
    col_label = " " * BOARD_PADDING + " | ".join(list(col_label))
    print(col_label)

    #print rows
    for i in range(len(board)):
        #separator
        print("- " * (len(col_label) // 2 + 1))

        #row data
        row_data = ""
        for space in board[i]:
            row_data += KNOWN if space["known"] else UNKNOWN
        row_data = str(i) + row_data
        print(" | ".join(list(row_data)))

# game loop
while state["game_state"] != GS_LEAVE:
    # play state
    if state["game_state"] == "PLAY":
        print_board(board)

        player_input = input("Input your next move: ")
    # menu state
    elif state["game_state"] == "MENU":
        print("\nWELCOME! This is the MENU.")

        player_input = input("Type\n\tPLAY to start a new game\n\tLEAVE to leave: ")
    # quit state is handled implicitly

    #process input to get new state
    state = handle_input(player_input, state)
print("\nBye\n")
