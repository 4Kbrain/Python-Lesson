import random

def initialize_game(size=4):
    """ゲームボードを初期化し、2つのタイルをランダムに配置する"""
    board = [[0] * size for _ in range(size)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    """空いている位置に新しいタイル（2または4）をランダムに追加する"""
    row, col = random.choice([(r, c) for r in range(len(board)) for c in range(len(board[0])) if board[r][c] == 0])
    board[row][col] = 2 if random.random() < 0.9 else 4

def compress(board):
    """タイルを圧縮して、空のスペースをなくす（左方向に移動）"""
    new_board = [[0] * len(board) for _ in range(len(board))]
    for r in range(len(board)):
        fill_position = 0
        for c in range(len(board[0])):
            if board[r][c] != 0:
                new_board[r][fill_position] = board[r][c]
                fill_position += 1
    return new_board

def merge(board):
    
    for r in range(len(board)):
        for c in range(len(board[0])-1):
            if board[r][c] == board[r][c+1] and board[r][c] != 0:
                board[r][c] *= 2
                board[r][c+1] = 0
    return board

def reverse(board):
    """ボードを反転させる（左右反転）"""
    new_board = []
    for row in board:
        new_board.append(row[::-1])
    return new_board

def transpose(board):
    
    return [list(row) for row in zip(*board)]

def move_left(board):
    """ル左に"""
    board = compress(board)
    board = merge(board)
    board = compress(board)
    return board

def move_right(board):
    """を右に"""
    board = reverse(board)
    board = move_left(board)
    board = reverse(board)
    return board

def move_up(board):
    """タイルを上に移動させる"""
    board = transpose(board)
    board = move_left(board)
    board = transpose(board)
    return board

def move_down(board):
    """タイルを下に移動させる"""
    board = transpose(board)
    board = move_right(board)
    board = transpose(board)
    return board

def is_game_over(board):
    """終了した"""
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 0:
                return False
            if c < len(board[0])-1 and board[r][c] == board[r][c+1]:
                return False
            if r < len(board)-1 and board[r][c] == board[r+1][c]:
                return False
    return True

"""ボードをコンソールに表示する"""

def print_board(board):
    
    for row in board:
        print(' '.join([str(cell).rjust(4) for cell in row]))
    print()

# ゲームのメインループ
def main():
    size = 4  # 4x4のゲームボード
    board = initialize_game(size)

    while True:
        print_board(board)
        move = input("次の動きを入力してください (W: 上, A: 左, S: 下, D: 右): ").upper()
        if move == 'W':
            board = move_up(board)
        elif move == 'A':
            board = move_left(board)
        elif move == 'S':
            board = move_down(board)
        elif move == 'D':
            board = move_right(board)
        else:
            print("無効なキーです。もう一度入力してください。")
            continue

        add_new_tile(board)

        if is_game_over(board):
            print_board(board)
            print("ゲームオーバー！")
            break

if __name__ == "__main__":
    main()

