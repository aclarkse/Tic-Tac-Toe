from IPython.display import clear_output
import random

# Define global variables
board = [" "] * 10
game_state = True
players = {"Player 1": "", "Player 2": ""}
game_result = ""
starting_player = ""

def display_board():
    """ This function displays the board.
        Returns:: A numpad output of the board
    """
    
    clear_output()
    print(" {0} | {1} | {2} ".format(board[7], board[8], board[9]))
    print("-----------")
    print(" {0} | {1} | {2} ".format(board[4], board[5], board[6]))
    print("-----------")
    print(" {0} | {1} | {2} ".format(board[1], board[2], board[3]))

def reset_board():
    """ This function resets the board, a list of
        length 10 in which the 0 index is ignored. """
    
    global board, game_state
    board = [" "] * 10
    game_state = True


def initialize_game():
    """ This function choose which player goes first and assigns
        the corresponding marker to each player.
        Returns:: a tuple with the marker each player has
    """
    
    global players, starting_player
    
    # To store which player is "X" and which is "O"
    players = {"Player 1": "", "Player 2": ""}
    starting_player = ""
    
    # Choose who starts
    print("Let\'s see who starts...")
    choice = random.randint(1,2)
    if choice == 1:
        print("Player 1 starts!")
        starting_player = "Player 1"
    else:
        print("Player 2 starts!")
        starting_player = "Player 2"
        
    marker = ""
    if choice == 1:
        while marker != "X" and marker != "O":
            marker = input("Player 1: Please choose \'X\' or \'O\': ").upper()
    else:
        while marker != "X" and marker != "O":
            marker = input("Player 2: Please choose \'X\' or \'O\': ").upper()
    
    # Assign players 
    if (choice == 1 and marker == "X") or \
    (choice == 2) and (marker == "O"):
        players["Player 1"] = "X"
        players["Player 2"] = "O"
        print("Player 1 is \'{}\' and Player 2 is \'{}\'".format(players["Player 1"], players["Player 2"]))
        return players, starting_player
    elif (choice == 1 and marker == "O") or \
    (choice == 2) and (marker == "X"):
        players["Player 1"] = "O"
        players["Player 2"] = "X"
        print("Player 1 is \'{}\' and Player 2 is \'{}\'".format(players["Player 1"], players["Player 2"]))
        return players, starting_player

def win_check(board, mark):
    """ This function checks to see if there is a winning state.
        Returns:: True if there is a win and False otherwise.
    """
    
    # Check to see if there is a horizontal win
    if (board[1] == board[2] == board[3] == mark) \
    or (board[4] == board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark):
        return True

    # Check to see if there is a vertical win
    elif (board[1] == board[4] == board[7] == mark) \
    or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark):
        return True

    # Check to see if there is a diagonal win
    elif (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark):
        return True
    else:
        return False

def full_board_check(board):
    """ This function checks to see if there is an empty spot on the board.
        Returns:: True if the board is full and False otherwise.
    """
    
    if " " in board[1:]:
        return False
    else:
        return True

def make_move(mark):
    """ This function prompts for user input from the player,
    indicating which position in the board to move to.
    Returns:: an integer indicating the position on the board
    """
    
    global board, players
    
    if mark == players["Player 1"]:
        current_player = "Player 1"
    else:
        current_player = "Player 2"
    
    
    prompt = current_player + " (\'" + mark + "\')" + ", please choose your next move (1-9)."
    while True:
        try:
            choice = int(input(prompt))
        except ValueError:
            print("That's not a valid location. Please enter a number (1-9).")
            continue
        if choice == 0:
            print("That's not a valid location. Please enter a number (1-9).")
            continue
        elif board[choice] == " ":
            board[choice] = mark
            break
        else:
            print("That location is taken. Please choose another.")
            continue

def who_wins(mark):
    global board, players, game_state, game_result
    
    # Set a blank game announcement
    game_result = ""
    
    # Get player input
    mark = str(mark)
    
    if mark == players["Player 1"]:
        winner = "Player 1"
    else:
        winner = "Player 2"
        
    # Validate position chosen
    make_move(mark)
    
    # Check for a winning condition
    if win_check(board, mark):
        clear_output()
        display_board()
        game_result = "Congratulations, {} wins!".format(winner)
        game_state = False
        
    # Show board
    clear_output()
    display_board()
    
    # Check for tie
    if full_board_check(board):
        game_result = "There's a tie!"
        game_state = False
        
    return game_state, game_result

def play_game():
    reset_board()
    global players, starting_player, game_result
    
    print("Welcome to Tic-Tac-Toe!")
    
    # Define players and who plays first
    players, starting_player = initialize_game()
   
    while True:
        # Display board
        clear_output()
        display_board()
        
        if starting_player == "Player 1":
            second_player = "Player 2"
        else:
            second_player = "Player 1"
        
        # Starting player's turn
        game_state, game_result = who_wins(players[starting_player])
        print(game_result)
        if game_state == False:
            break
            
        # Second player's turn
        game_state, game_result = who_wins(players[second_player])
        print(game_result)
        if game_state == False:
            break
            
    # Ask players to replay
    replay = input("Do you want to play again? Enter \'Yes\' or \'No\'")
    if replay.lower() == "yes":
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
	play_game()
    