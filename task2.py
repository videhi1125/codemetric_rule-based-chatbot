import math

PLAYER = 'X'
COMPUTER = 'O'
EMPTY = ' '

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None

def is_draw(board):
    return all(cell != EMPTY for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == COMPUTER:
        return 1
    if winner == PLAYER:
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = COMPUTER
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = COMPUTER
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    while True:
        board = [[EMPTY]*3 for _ in range(3)]
        print("You are X | Computer is O")

        while True:
            print_board(board)
            r, c = map(int, input("Enter row and column (0-2): ").split())
            if board[r][c] == EMPTY:
                board[r][c] = PLAYER
            else:
                print("Invalid move!")
                continue

            if check_winner(board) or is_draw(board):
                break

            i, j = best_move(board)
            board[i][j] = COMPUTER

            if check_winner(board) or is_draw(board):
                break

        print_board(board)
        winner = check_winner(board)
        if winner == PLAYER:
            print("You win!")
        elif winner == COMPUTER:
            print("Computer wins!")
        else:
            print("It's a draw!")

        again = input("Play again? (yes/no): ").lower()
        if again != 'yes':
            break

play_game()
