"""
Minesweeper Game

"""

from random import randint

NUM_COLS = 5
NUM_ROWS = 5
NUM_BOMBS = 11

class Cell(object):

    def __init__(self):
        self.bomb = False
        self.num = 0
        self.reveal = False


# Create board, a 2D array of Cell objects
board = [ [Cell() for x in range(NUM_COLS)] for y in range(NUM_ROWS) ]
neighbor_list = [ [-1, -1], [-1, 0], [-1, 1],
                  [0, -1], [0, 1],
                  [1, -1], [1, 0], [1, 1]]

def generate_bombs(board):
    """
    Generate bombs randomly, make sure you generate 11 and not overwrite them
    """
    num_bomb = 0
    while num_bomb < NUM_BOMBS:

        x = randint(0, NUM_COLS -1)
        y = randint(0, NUM_ROWS -1)

        if board[y][x].bomb is False:
            board[y][x].bomb = True
            num_bomb += 1

    return board


def calculate_number(board):
    """
    Calculate number of cells in each adjecent cell
    """
    for x in range(NUM_COLS):
        for y in range(NUM_ROWS):
            for tup in neighbor_list:
                if (y+tup[0]) in range(NUM_ROWS) and (x+tup[1]) in range(NUM_COLS):
                    if board[y+tup[0]][x+tup[1]].bomb is True:
                        board[y][x].num += 1

    return board


def show_board():
    # print out board and, if cells not revealed, print '.', if revealed print 
    # number

    # Print heading
    print "\n ",
    for col in range(NUM_COLS):
        print "  ",col,
    print

    # Print each row, with row heading on left
    for y in range(NUM_ROWS):
            print y, 
            for i in range(NUM_COLS):
                if board[y][i].reveal is True:
                    print "  ", board[y][i].num,
                else:
                    
                    print "  ", ".",
            print 


def reveal_neighbors(board, y, x):
    for tup in neighbor_list:
        if (y+tup[0]) in range(NUM_ROWS) and (x+tup[1]) in range(NUM_COLS):
                if board[y+tup[0]][x+tup[1]].num == 0:
                    board[y+tup[0]][x+tup[1]].reveal = True
                    reveal_neighbors(board, y+tup[0], x+typ[1])
                else:
                    board[y+tup[0]][x+tup[1]].reveal = True


def play_game(board):

    while True:
        show_board(board)
        move = raw_input('Please pick a location (row, col) >>>')
        if board[move[0]][move[1]].bomb is True:
            return "You lost"
        else:
            if board[move[0]][move[1]].num == 0:
                reveal_neighbors(board, move[0], move[1])

            board[move[0]][move[1]].reveal = True


generate_bombs(board)
for row in calculate_number(board):
    for item in row:

        print item.bomb
        print item.num


