# constants
UNKNOWN = "X"
KNOWN = "O"

BOARD_SIZE = 10
BOARD_PADDING = 4

# board initialization
board = [
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

print_board(board)
