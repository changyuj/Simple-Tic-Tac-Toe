# --- Function to Print the board ---
def print_board(board):
    print("\n")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
    print("------------------")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
    print("------------------")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")
    print("\n")

# --- Function to check for winner ---
def check_winner(board, player):
    # check rows
    for i in range(0,9,3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # check diagnoals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# --- Function to check for draw ---
def check_draw(board):
    return " " not in board

# --- Main game logic ---
def play_game():
    board = [" " for _ in range(9)] #create a empty board
    current_player = "X"
    game_over = False
    
    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered 1-9 from left to right, top to bottom.")
    
    while not game_over:
        print_board(board)
        try:
            move = int(input(f"Play {current_player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = current_player
                
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Play {current_player} wins! Congratulations!")
                    game_over = True
                elif check_draw(board):
                    print_board(board)
                    print("It's a draw!")
                    game_over = True
                else:
                    current_player = "O" if current_player == "X" else "X"
            else:
                print("Invalid move. That position is taken or invalid, try again.")
            
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# --- Start the game ---
if __name__ == "__main__":
    play_game()