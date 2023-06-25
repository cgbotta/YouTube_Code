import random

def print_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('-----------')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('-----------')
    print(f' {board[6]} | {board[7]} | {board[8]} ')

def get_empty_positions(board):
    return [i for i, x in enumerate(board) if x == ' ']

def has_won(board, player):
    win_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(board[i] == board[j] == board[k] == player for i, j, k in win_positions)

def get_move_easy(board):
    return random.choice(get_empty_positions(board))

def get_move_medium(board):
    for i in get_empty_positions(board):
        if has_won(board[:i] + ['X'] + board[i+1:], 'X'):
            return i
    return get_move_easy(board)

def minimax(board, player):
    if has_won(board, 'O'):
        return {'score': 1}
    elif has_won(board, 'X'):
        return {'score': -1}
    elif ' ' not in board:
        return {'score': 0}

    if player == 'O':
        best = {'score': -float('inf')}
        for i in get_empty_positions(board):
            score = minimax(board[:i] + ['O'] + board[i+1:], 'X')['score']
            if score > best['score']:
                best = {'score': score, 'move': i}
    else:
        best = {'score': float('inf')}
        for i in get_empty_positions(board):
            score = minimax(board[:i] + ['X'] + board[i+1:], 'O')['score']
            if score < best['score']:
                best = {'score': score, 'move': i}

    return best

def get_move_hard(board):
    return minimax(board, 'O')['move']

def main():
    board = [' '] * 9
    user_marker = 'X'
    ai_marker = 'O'

    difficulty = input('Select difficulty (easy, medium, hard): ').lower()
    while difficulty not in ['easy', 'medium', 'hard']:
        print('Invalid difficulty. Please select easy, medium, or hard.')
        difficulty = input('Select difficulty (easy, medium, hard): ').lower()

    if random.choice([True, False]):
        print('You go first!')
    else:
        print('The computer goes first!')
        if difficulty == 'easy':
            board[get_move_easy(board)] = ai_marker
        elif difficulty == 'medium':
            board[get_move_medium(board)] = ai_marker
        else:
            board[get_move_hard(board)] = ai_marker

    while ' ' in board:
        print_board(board)

        move = int(input('Select move (0-8): '))
        while move not in get_empty_positions(board):
            print('Invalid move.')
            move = int(input('Select move (0-8): '))
        board[move] = user_marker

        if has_won(board, user_marker):
            print_board(board)
            print('You win!')
            return
        elif ' ' not in board:
            print_board(board)
            print('It\'s a draw.')
            return

        print('Computer\'s turn.')
        if difficulty == 'easy':
            board[get_move_easy(board)] = ai_marker
        elif difficulty == 'medium':
            board[get_move_medium(board)] = ai_marker
        else:
            board[get_move_hard(board)] = ai_marker

        if has_won(board, ai_marker):
            print_board(board)
            print('Computer wins.')
            return

    print_board(board)
    print('It\'s a draw.')

if __name__ == '__main__':
    main()
