def print_board(board):
    for row in board:
        print(" ".join(row))

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    rounds = [0, 0]
    while True:
        print_board(board)
        print(f"Player {players[current_player]}'s turn")
        row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
        if board[row][col] != " ":
            print("Cell already taken, try again")
            continue
        board[row][col] = players[current_player]
        if check_winner(board, players[current_player]):
            print(f"Player {players[current_player]} wins!")
            rounds[current_player] += 1
            if rounds[current_player] == 3:
                print(f"Player {players[current_player]} wins the game!")
                break
            board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = 1 - current_player

# Start the game
play_game()