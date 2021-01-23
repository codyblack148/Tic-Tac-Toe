# Command Line Tic Tac Toe, created by Sol, 1/21/2021

test_board = ['X','X','O','O','O','X','X','X','O']
blank_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

#function to define and display the game board.

def display_board(board):
    """ board is an array with nine 'X' or 'O' strings corresponding to
        keys 1-9 on a numpad. [X,O,X,O,X,O,X,O,X]"""
    print(f'         |            |          \n     {board[6]}   |     {board[7]}      |   {board[8]}     \n         |            |          ')
    print('---------------------------------')
    print(f'         |            |          \n     {board[3]}   |     {board[4]}      |   {board[5]}     \n         |            |          ')
    print('---------------------------------')
    print(f'         |            |          \n     {board[0]}   |     {board[1]}      |   {board[2]}     \n         |            |          ')
#display_board(blank_board)

# Function to take in player input and assign 'X' or 'O' to board index. (Marker is X or O)
def update_board(marker,index,board):
    board[index-1] = marker
    return board
    
# Function that gets player input. Marker is passed in as the player value from the assign players function.
def player_input(marker):
    out = ''
    check_list = [1,2,3,4,5,6,7,8,9]
    while out not in check_list:
        out = int(input(f'Please enter your {marker} using the keys 1-9 on the numpad.\n'))
        if out not in check_list:
            print("You have to input a number between 1 and 9.")
    return out

# Function to check if board is full or if someone has won. Return list with 3 booleans. Booleans correspond to winning player, or tie.

def game_end_check(board,marker,player_assignment):
    

    if (board[6] == board[7] == board[8] == marker or
    board[3] == board[4] == board[5] == marker or
    board[0] == board[1] == board[2] == marker or
    board[6] == board[3] == board[0] == marker or
    board[7] == board[4] == board[1] == marker or
    board[8] == board[5] == board[2] == marker or
    board[6] == board[4] == board[2] == marker or
    board[8] == board[4] == board[0] == marker):
        if marker == 'X' and player_assignment[0] == "X":
            return [True, False, False]
        else:
            return [False, True, False]
    elif ' ' not in board:
        return [False,False,True]
    else:
        return [False,False,False]
        
#display_board(test_board)
#print(game_end_check(test_board,'X',['X','O']))

    

# Function to assign players either 'X' or 'O' at beginning of game. Returns list of size 2 with X or O corresponding to player choice.
def assign_players():
    player_values = ['','']
    check_list = ['X','O'] 
    while player_values[0] not in check_list or player_values[1] not in check_list:
        player_values[0] = input('Player 1, please choose whether you want to be X or O\n')
        if player_values[0] not in check_list:
            print('You can only choose X or O, please do it again.')
        if player_values[0] in check_list:
            if player_values[0] == 'X':
                player_values[1] = 'O'
            else:
                player_values[1] = 'X'
    return player_values


# Function to reset the board and game. keep_playing is a boolean passed in to indicate whether to run the game again or exit.
def reset(keep_playing):

    if keep_playing:
        play_game([' ',' ',' ',' ',' ',' ',' ',' ',' '])
    else:
        print('Thank you for playing! \n<3,\n Sol')
        quit()

def print_game_results(game_status):
    if game_status == [True, False, False]:
        print('Player 1 has won the game, congratulations. Player 2 extermination commencing.')
    elif game_status == [False,True,False]:
        print('Player 2 has won the game, congratulations. Player 1 extermination commencing.')
    elif game_status == [False, False, True]:
        print('The game has resulted in a tie. Extermination of both players commencing.')
    else:
        pass

def play_again():
    out = ''
    check_list = ['y','n']
    while out not in check_list:
        out = input('Do you want to play again? Enter y/n\n')
    return out == 'y'


def play_game(blank_board):
    game_board = blank_board
    keep_playing = True
    game_status = [False, False, False]

    player_assignment = assign_players()
    while keep_playing:

        # Player 1 Turn

        display_board(game_board)
        print('Player 1:')
        player_choice = player_input(player_assignment[0])
        if ' ' not in game_board[player_choice - 1]:
            print("You must choose a spot that doesn't already have an X or O.")
            continue
        game_board = update_board(player_assignment[0],player_choice,game_board)
        #print(game_board)
        game_status = game_end_check(game_board,player_assignment[0],player_assignment)
        #print(game_status)
        if True in game_status:
            display_board(game_board)
            print_game_results(game_status)
            reset(play_again())

        # Player 2 Turn

        display_board(game_board)
        print('Player 2:')
        player_choice = player_input(player_assignment[1])
        if ' ' not in game_board[player_choice-1]:
            print("You must choose a spot that doesn't already have an X or O.")
            continue
        game_board = update_board(player_assignment[1],player_choice,game_board)
        game_status = game_end_check(game_board,player_assignment[1],player_assignment)
        if True in game_status:
            display_board(game_board)
            print_game_results(game_status)
            reset(play_again())
    
        
        
        

# Begin game.

play_game(blank_board)
        
    
    
    
