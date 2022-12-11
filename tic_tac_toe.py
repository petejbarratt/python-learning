
def display_board(board):
    print("\
+-------+-------+-------+\n\
|       |       |       |\n\
|   ",board[0][0],"   |   ",board[0][1],"   |   ",board[0][2],"   |\n\
|       |       |       |\n\
+-------+-------+-------+\n\
|       |       |       |\n\
|   ",board[1][0],"   |   ",board[1][1],"   |   ",board[1][2],"   |\n\
|       |       |       |\n\
+-------+-------+-------+\n\
|       |       |       |\n\
|   ",board[2][0],"   |   ",board[2][1],"   |   ",board[2][2],"   |\n\
|       |       |       |\n\
+-------+-------+-------+\n",sep="")

board = [[1,2,3],[4,"X",6],[7,8,9]]
square_ids = ((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2))

def list_of_free_fields(board):
    free_fields = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if type(board[i][j]) is int: #because the board is set up with numbers at the start
                free_fields.append(board[i][j]) #to get list of available square numbers
    return free_fields

def enter_player_move(board):
    global square_ids #tuple with square ids defined above with board initialisation
    is_move_valid = False
    while is_move_valid == False:
        try:
            move = int(input("Enter square number of your next move: "))
            if move <1 or move >9:
                print("No, number must be between 1 and 8.")
            elif move in list_of_free_fields(board): #check that the square is available
                is_move_valid = True
            else:
                print("Sorry, square taken. Try again")

        except ValueError:
            print("Input not recognised.")

    if is_move_valid == True:
        #update the board
        board[square_ids[move - 1][0]][square_ids[move - 1][1]] = "O"

def computer_move(board):
    global square_ids
    free_fields = list_of_free_fields(board)
    from random import randrange
    computers_move = free_fields[randrange(len(free_fields))]
    board[square_ids[computers_move - 1][0]][square_ids[computers_move - 1][1]] = "X"
    

def victory_for(board,sign):
    victory = False
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == sign:
            victory = True
    for j in range(3):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j] and board[0][j] == sign:
            victory = True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == sign:
            victory = True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == sign:
            victory = True
    return victory
    
display_board(board)
counter = 1
print("Computer is 'X', you are 'O'. Computer has already made first move.")
while victory_for(board,"X") == False and victory_for(board,"O") == False:
    enter_player_move(board)
    counter += 1
    display_board(board)
    if victory_for(board,"O") == True:
        print("Victory for you!")
        break #otherwise it will still do the next computer's move even if the player has already won
    computer_move(board)
    counter += 1
    display_board(board)
    if victory_for(board,"X") == True:
        print("Victory for Computer")
    else:
        if counter == 9:
            print("Nobody wins")
            break
