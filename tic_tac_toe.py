# Author: <Your name>
# Assignment #5 - Tic-tac-toe
# Date due: 2021-04-22
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

####### DO NOT EDIT CODE BELOW ########

MAX_ROUNDS = 9
NUM_ROWS = 3
NUM_COLS = 3
NUM_POSITIONS = 9
ROW_POS = 0
COL_POS = 1

def display_board(board):
    """Displays the board's current state as a 3x3 grid"""

    print("     0 1 2 ")

    for row in range(0, NUM_ROWS):
        print("  {}  ".format(row), end="")
        for col in range(0, NUM_COLS):
            if col == 0:
                print(board[(row, col)], end="")
            else:
                print("|{}".format(board[(row, col)]), end="")

        print(" ")

        if row < NUM_ROWS - 1:
            print("    --+-+--")
    print()

####### DO NOT EDIT CODE ABOVE ########


def main():

    ########## DO NOT EDIT DICTIONARY INITIALIZATION BELOW #########

    board = {
        (0,0): ' ', (0,1): ' ', (0,2): ' ',
        (1,0): ' ', (1,1): ' ', (1,2): ' ',
        (2,0): ' ', (2,1): ' ', (2,2): ' '
    }

    ########## DO NOT EDIT DICTIONARY INITIALIZATION ABOVE #########
    
    # call play_tic_tac_toe() with board as argument and remove pass below
    pass

if __name__ == '__main__':
    main()
