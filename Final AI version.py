from random import *
import time

# Credit to inventwithpython.com for AI algorithm

def initial():
    '''initialize starting board state'''
    for i in keys:
        board[i] = " " #Empty space represents an empty box

## Create a dictionary representation of a tic-tac-toe board
row = range(3)
column = range(3)
board = {}
keys = []
for i in row:
    for j in column:
        keys = keys + [(i,j)]

initial()

class player:
    def __init__(self,piece,turn):
        '''Makes a piece on the tic tac toe board unique to a player'''
        self.piece = piece
        self.turn = turn
        
    def get_piece(self):
        return self.piece

    def get_turn(self):
        return self.turn

    def win(self,board):
        '''Checks if the player wins the board state'''
        for i in range(3):
            rows = []
            columns = []
            for j in range(3):
                rows.append(board[(i,j)])
                columns.append(board[(j,i)])
            if rows.count(self.piece) == 3 or columns.count(self.piece) == 3:
                return True
        if board[(0,0)]== self.piece and board[(1,1)]== self.piece \
        and board[(2,2)]== self.piece:
            return True
        if board[(0,2)]== self.piece and board[(1,1)]== self.piece \
        and board[(2,0)]== self.piece:
            return True
        return False

    def place(self,n,board):
        '''Takes an input of tuple n and places an X or O to the
       corresponding n-square on the board'''
        if board.keys().count(n) == 0:
            return False
        board[n] = self.piece

    def myTurn(self,board):
        '''Returns true if its the player's turn to move'''
        boardstate = board.values()
        if self.turn == 0:
            if boardstate.count('X') == boardstate.count('O'):
                return True
        elif self.turn == 1:
            if boardstate.count('X') > boardstate.count('O'):
                return True
        return False
            
def make_move(board,computer,human):
    '''Top-down algorithm for the computer to select and place a move'''
    if computer.myTurn(board) == False:
        return False #Prevent computer from moving out of turn
    for i in legalmoves(board):
        computer.place(i,board)
        # Place a winning move
        if computer.win(board) == True:
            computer.place(i,board)
            return 1 # Function termination value
        board[i] = ' '
    for i in legalmoves(board):
        # Stop a win by the player
        human.place(i,board)
        if human.win(board) == True:
            computer.place(i,board)
            return 2
        board[i] = ' '
    # Take a corner if it is available
    corners = [i for i in legalmoves(board) if i == (0,0) or i == (0,2) or
               i == (2,0) or i == (2,2)]
    if corners != []:
        computer.place(choice(corners),board)
        return 3
    # Take the centre if it is available
    if board[(1,1)] == ' ':
        computer.place((1,1),board)
        return 4
    # Take the sides
    sides = [i for i in legalmoves(board)]
    computer.place(choice(sides),board)
    return 5

def legalmoves(board):
    '''Returns a list of available tuple moves on the current board state'''
    moves = [i for i in board if board[i] == ' ']
    return sorted(moves)

        
def display(board):
    '''Returns a graphical representation of the current board state'''
    for i in range(3):
        print "   |   |   "
        print " "+board[(i,0)]+" | "+board[(i,1)]+" | "+board[(i,2)]+" "
        print "   |   |   "
        if i < 2:
            print "---+---+---"

def draw(board):
    '''Checks if the board is populated and a win has not occured'''
    for i in board:
        if board[i] == ' ':
            return False
    return True

    
def main():
    print "Play a game of Tic Tac Toe against the computer!"
    print "Credit goes to inventwithpython.com for AI algorithm"
    print "Press 1 to move first or 2 to move second"
    user = input("(1 or 2): ")
    while user != 1 and user != 2:
        user = input("(1 or 2): ")
    if user == 1:
        human = player('X',0)
        computer = player('O',1)
    else:
        computer = player('X',0)
        human = player('O',1)
    print "Use the board shown below for move reference."
    print '''
    |    |   
 00 | 01 | 02 
    |    |   
----+----+----
    |    |   
 10 | 11 | 12 
    |    |    
----+----+----
    |    |    
 20 | 21 | 22 
    |    |
'''
    raw_input("Press Enter to continue.")
    time.sleep(1)
    while computer.win(board) == False and human.win(board) == False and \
    draw(board) == False:
        if make_move(board,computer,human) != False:
            print "Computer is making a move..."
            time.sleep(2)
            make_move(board,computer,human)
        else:
            print "Enter your move as an (i,j) notation"
            display(board)
            human_move = input("Enter(i,j) here: ")
            while human.place(human_move,board) == False:
                human_move = input("Enter(i,j) here: ")
            human.place(human_move,board)
            display(board)
    print "Final board:"
    display(board)
    time.sleep(2)
    if computer.win(board) == True:
        print "Computer wins! Do you want to Retry or Exit?"
        print "Press 1 to Retry or 2 to Exit."
    elif human.win(board) == True:
        print "You win! Do you want to Retry or Exit?"
        print "Press 1 to Retry or 2 to Exit."       
    else:
        print "It's a draw! Do you want to Retry or Exit?"
        print "Press 1 to Retry or 2 to Exit."
    user = input("(1 or 2): ")
    while user != 1 and user != 2:
        user = input("(1 or 2): ")
    if user == 1:
        initial()
        main()
    else:
        initial()
        print "Exiting"
        return None

main()
