# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for ... (displaying the board?)
def board_init():
    """
    # 1. assign the values to the structure: (1, 2, 3)
    #                                        (4, 5, 6)
    #                                        (7, 8, 9)
    # Data type: Dictionary with above keys and values input by player
    """
    tic_tac_toe_dic_l = {}
    for i in range(1,10):
        tic_tac_toe_dic_l[i] = i
    return tic_tac_toe_dic_l


def board_update(tic_tac_toe_dic_l, input_loc_l, input_symbol_l):
# update the board
    tic_tac_toe_dic_l[int(input_loc_l)] = input_symbol_l
    return tic_tac_toe_dic_l


# Function for... (choosing a player?)
def player_choice():
    # Ask first player the symbol : 'X' / 'O'. By default the second player will have other choice.
    player1_sym_l = input("Which symbol do you want 'X' or 'O': ")
    player2_sym_l = 'X'
    
    if player1_sym_l == 'X':
        player2_sym_l = 'O'
    elif player1_sym_l == 'O':
        player2_sym_l = 'X'
    else:
        print('Invalid Symbol')
        player_choice()
    return player1_sym_l, player2_sym_l


def display_board(tic_tac_toe_dic_l):
# Display the board 
    print(tic_tac_toe_dic_l[1], tic_tac_toe_dic_l[2], tic_tac_toe_dic_l[3])
    print(tic_tac_toe_dic_l[4], tic_tac_toe_dic_l[5], tic_tac_toe_dic_l[6])
    print(tic_tac_toe_dic_l[7], tic_tac_toe_dic_l[8], tic_tac_toe_dic_l[9])


def player_input(turn_l):
    # Ask player turn by turn for the input. 
    # Flag to track which player's turn it is.
    # check the dictionary value, if it is not occupied then it is valid, else give error
    if turn_l == 1:
        input_location_l = input('Player 1: where?: ')
    else:
        input_location_l = input('Player 2: where?: ')
    return input_location_l


def check_winner(tic_tac_toe_dic_l, already_true):
# Check 8 cases in which player can be a winner    
    for i in range(1,8,3):
        if already_true == i:
            pass
        elif tic_tac_toe_dic_l[i+0] == tic_tac_toe_dic_l[i+1] == tic_tac_toe_dic_l[i+2]:
            return i
    
    for i in range(1,4):
        if already_true == i+10:
            pass
        elif tic_tac_toe_dic_l[i] == tic_tac_toe_dic_l[i+3] == tic_tac_toe_dic_l[i+6]:
            return i + 10

    if already_true == 8:
        pass
    elif tic_tac_toe_dic_l[1] == tic_tac_toe_dic_l[5] == tic_tac_toe_dic_l[9]:
        return 8

    if already_true == 9:
        pass
    elif tic_tac_toe_dic_l[3] == tic_tac_toe_dic_l[5] == tic_tac_toe_dic_l[7]:
        return 9    
        
    return 0
   

def check_end_of_game(tic_tac_toe_dict_l):
# Check end of game
    for i in range(1,10):
        if tic_tac_toe_dict_l[i] == i:
            return False    
    return True


# Tic-tac-toe game
if __name__ == "__main__":

    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")

    # Initialize the flags
    turn = 1
    winner1_flag = 0
    winner2_flag = 0
    end_of_game = False
    tic_tac_toe_dict = board_init()
    player_1, player_2 = player_choice()
    already_true = 0
    
    # Playing Loop
    while end_of_game == False:
        display_board(tic_tac_toe_dict)
        input_loc = player_input(turn)
        if turn == 1:
            input_symbol = player_1
        else:
            input_symbol = player_2
        tic_tac_toe_dict = board_update(tic_tac_toe_dict, input_loc, input_symbol)
        winner = check_winner(tic_tac_toe_dict, winner1_flag)

    # Conditions of various winning scenarios:
        # Player 1 is winner
        # Player 2 is winner
        # No player is winner
        # Draw (Player 1 is winner and then Player 2 also wins in the next chance)
        if winner != 0 or winner1_flag != 0:
            if turn == 1:
                winner1_flag = winner
                print("It can be a Draw. Let's see!")
            else:
                winner2_flag = winner
                if winner1_flag != 0 and winner2_flag != 0:
                    print("It's Draw")
                elif winner1_flag != 0:
                    print("Player 1 is the winner")
                elif winner2_flag != 0:
                    print("Player 2 is the winner")
                end_of_game = True
        else:    
            if check_end_of_game(tic_tac_toe_dict):
                print("No Winner, try again")
                end_of_game = True

    # change of turns
        if turn == 1:
            turn = 2
        else:
            turn = 1
        

