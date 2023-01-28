import random
import numpy as np

board = [[1,2,3],
         [4,5,6],
         [7,8,9]]
                 
def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
    sign=["X","O"]
    
    print("Game board: \n")

    print("",board[0][0],"|",board[0][1],"|",board[0][2],"\n"
          "-----------","\n",
          board[1][0],"|",board[1][1],"|",board[1][2],"\n"
          "-----------","\n",
          board[2][0],"|",board[2][1],"|",board[2][2],"\n")

    Vstatus=VictoryFor(board, sign)

    if Vstatus == 0:
        count=0
        #Checks whos go it is
        for row in range(3):
            for column in range(3):
                elem=board[row][column]
                if type(elem) == int:
                    count = count +1
        if count % 2 == 0:
            #Computer's go
            print("Computer's move: \n")
            DrawMove(board)
        else:
            #Human's go
            print("Your move... \n")
            EnterMove(board)
    

def EnterMove(board):
    #
    # the function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision
    #Convert 3x3 matrix into 1 D array
    Translator=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

    move= int(input("Please select an acceptable move number: "))

    #Basic check of input

    if type(move) == int and 0<move<10:
        

        moveCoords=Translator[move-1]
        #print("Movecoord", moveCoords)    
        AcceptableBoard=MakeListOfFreeFields(board)
        #print("ABoard", AcceptableBoard)
              
              
        if moveCoords in AcceptableBoard:
            print("Correct data entry type")
            board[moveCoords[0]][moveCoords[1]]="O"
            DisplayBoard(board)
        else:
            print("Square taken, try again")
            EnterMove(board)
              
    else:
        print("Please select an integer between 1 & 9 that is available")
        EnterMove(board)

    
def MakeListOfFreeFields(board):
    #
    # the function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers
    #
        #Creates list of acceptable numbers
    
    AcceptableBoard=[]
    
    #Iterate through rows
    for row in range(len(board)):
        for column in range(len(board)):
            coordTuple=(row,column)
            if type(board[coordTuple[0]][coordTuple[1]]) == int:
                AcceptableBoard.append(coordTuple)
            
    return AcceptableBoard

def VictoryFor(board, sign):
    #
    # the function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    #

    #Check to see if available spaces
    if len(MakeListOfFreeFields(board)):
        #print(sign)
        for player in sign:
            #print(player)
            check=[player,player,player]
            #print(check)
            column1=[board[0][0], board[1][0], board[2][0]]
            column2=[board[0][1], board[1][1], board[2][1]]
            column3=[board[0][2], board[1][2], board[2][2]]
            diagonal1=[board[0][0],board[1][1],board[2][2]]
            diagonal2=[board[0][2],board[1][1],board[2][0]]
            #b=np.array(board)
            #print(diagonal1)
            if (
            (board[1][:] == check) or 
            (board[0][:] == check) or 
            (board[2][:] == check) or 
            (column1 == check) or 
            (column2== check) or 
            (column3== check) or 
            (diagonal1 == check) or 
            (diagonal2 == check)
                ):

                
                #print("Player", player)
                #print(board)
                if player == "O":
                    print("You have won! Congratulations!")
                    Vstatus=1
                    return Vstatus
                elif player == "X":
                    print("Uh oh :( You lost")
                    Vstatus=1
                    return Vstatus
                    
            else:
                Vstatus=0
        return Vstatus
    else:
        print("It's a draw!")
        return
    
def DrawMove(board):
    #
    # the function draws the computer's move and updates the board
    #

    # 2 Dimesnional list

    #Check free moves

    free=MakeListOfFreeFields(board)
    
    compmove=random.sample(free, 1)
    #print("Comp move", compmove)

    board[compmove[0][0]][compmove[0][1]]="X"
    DisplayBoard(board)
    



print("-------- TIC TAC TOE -------- \n A game by Tom Wilson \n")
print("Game Start! \n")

DisplayBoard(board)
