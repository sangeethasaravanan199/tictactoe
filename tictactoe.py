# --- Global Variables ---

# The game board is represented as a list. We use a list of 10 strings to represent the board,
# ignoring index 0. This makes it easier to map the user's 1-9 input directly to the list index.
board = [' '] * 10

# A flag to keep the main game loop running.
game_is_still_going = True

# Stores the winner ('X' or 'O') if there is one.
winner = None

# Stores the current player ('X' or 'O'). 'X' will go first.
current_player = 'X'


def display_board():
    """
    Prints out the game board.
    The board is mapped to the number pad for intuitive play.
    7 | 8 | 9
    --+---+--
    4 | 5 | 6
    --+---+--
    1 | 2 | 3
    """
    print("\n")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("---+---+---")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---+---+---")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("\n")


def handle_turn(player):
    """
    Manages a single turn for the given player.
    It prompts for input, validates it, and updates the board.
    """
    print(f"{player}'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        # Validate that the input is a number from 1-9
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input("Invalid input. Choose a position from 1-9: ")

        position = int(position)

        # Validate that the chosen spot is empty
        if board[position] == ' ':
            valid = True
        else:
            print("You can't go there. Go again.")
            position = input("Choose a position from 1-9: ")

    # Update the board with the player's move
    board[position] = player
    display_board()


def check_if_game_over():
    """
    Checks if the game has ended, either by a win or a tie.
    It calls the helper functions to check for each condition.
    """
    check_for_winner()
    check_if_tie()


def check_for_winner():
    """
    Checks all possible winning combinations (rows, columns, diagonals)
    and updates the global 'winner' and 'game_is_still_going' variables if a win is found.
    """
    global winner
    global game_is_still_going

    # Check rows
    row_1 = board[7] == board[8] == board[9] != ' '
    row_2 = board[4] == board[5] == board[6] != ' '
    row_3 = board[1] == board[2] == board[3] != ' '
    if row_1 or row_2 or row_3:
        game_is_still_going = False
        # The winner is the player who made the move in that row
        winner = board[7] if row_1 else (board[4] if row_2 else board[1])
        return

    # Check columns
    col_1 = board[7] == board[4] == board[1] != ' '
    col_2 = board[8] == board[5] == board[2] != ' '
    col_3 = board[9] == board[6] == board[3] != ' '
    if col_1 or col_2 or col_3:
        game_is_still_going = False
        winner = board[7] if col_1 else (board[8] if col_2 else board[9])
        return

    # Check diagonals
    diag_1 = board[7] == board[5] == board[3] != ' '
    diag_2 = board[1] == board[5] == board[9] != ' '
    if diag_1 or diag_2:
        game_is_still_going = False
        winner = board[5]  # The middle element is common to both diagonals
        return


def check_if_tie():
    """
    Checks if the board is full. If it is, and there is no winner,
    it's a tie. Updates the 'game_is_still_going' variable.
    """
    global game_is_still_going
    # If there are no more empty spaces ' ' on the board, it's a tie
    if ' ' not in board[1:]:
        game_is_still_going = False


def flip_player():
    """
    Switches the current player from 'X' to 'O' or vice-versa.
    """
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def play_game():
    """
    The main function that orchestrates the entire game.
    """
    # Reset game state for a new game
    global board, current_player, winner, game_is_still_going
    board = [' '] * 10
    current_player = 'X'
    winner = None
    game_is_still_going = True

    print("Welcome to Tic Tac Toe!")
    display_board()

    # Main game loop
    while game_is_still_going:
        # Handle a single turn for the current player
        handle_turn(current_player)

        # Check if the game has ended
        check_if_game_over()

        # Switch to the other player
        flip_player()

    # The game has ended, so print the result
    if winner:
        print(f"Congratulations, {winner}! You won!")
    else:
        print("It's a tie!")


# --- Main Execution ---
if __name__ == "__main__":
    while True:
        play_game()
        # Ask the player if they want to play again
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break