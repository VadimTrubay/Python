import random
import os


def board():
    print(' 1' + ' | ' + '2' + ' | ' + '3 ')
    print('---+---+---')
    print(' 4' + ' | ' + '5' + ' | ' + '6 ')
    print('---+---+---')
    print(' 7' + ' | ' + '8' + ' | ' + '9 ')


def draw_board(board):

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---+---+---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---+---+---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def play_again():
    print('Do you want to play again?(y/n)')
    return input().lower().startswith('y')


def make_move(board, letter, move):
    board[move] = letter


def winner(board, letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[1] == letter and board[4] == letter and board[7] == letter) or
            (board[2] == letter and board[5] == letter and board[8] == letter) or
            (board[3] == letter and board[6] == letter and board[9] == letter) or
            (board[1] == letter and board[5] == letter and board[9] == letter) or
            (board[3] == letter and board[5] == letter and board[7] == letter))


def get_board_copy(board):
    dupe_board = []

    for i in board:
        dupe_board.append(i)

    return dupe_board


def space_free(board, move):
    return board[move] == ' '


def get_player_move(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not space_free(board, int(move)):
        print('your turn (1-9): ')
        move = input()
    return int(move)


def choose_random_move_from_list(board, moves_list):
    possible_moves = []
    for i in moves_list:
        if space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_letter):
    if computer_letter == 'x':
        player_letter = '0'
    else:
        player_letter = 'x'

    for i in range(1, 10):
        copy = get_board_copy(board)
        if space_free(copy, i):
            make_move(copy, computer_letter, i)
            if winner(copy, computer_letter):
                return i
    for i in range(1, 10):
        copy = get_board_copy(board)
        if space_free(copy, i):
            make_move(copy, player_letter, i)
            if winner(copy, player_letter):
                return i
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move
    if space_free(board, 5):
        return 5
    return choose_random_move_from_list(board, [2, 4, 6, 8])


def board_full(board):
    for i in range(1, 9):
        if space_free(board, i):
            return False
    return True


while True:
    the_board = [' '] * 10
    player_Letter = 'x'
    computer_letter = '0'
    turn = who_goes_first()
    game_playing = True
    while game_playing:
        os.system('cls')
        print("Let's play x or 0!")
        print('Will be the first to walk ' + turn)
        board()
        print('===========\n')
        if turn == 'player':
            draw_board(the_board)
            move = get_player_move(the_board)
            make_move(the_board, player_Letter, move)
            if winner(the_board, player_Letter):
                draw_board(the_board)
                print('Congratulations!!! You have won the game!')
                game_playing = False
            else:
                if board_full(the_board):
                    draw_board(the_board)
                    print('Draw!')
                    break
                else:
                    turn = 'computer'
        else:
            move = get_computer_move(the_board, computer_letter)
            make_move(the_board, computer_letter, move)
            if winner(the_board, computer_letter):
                draw_board(the_board)
                print('The computer won!')
                game_playing = False
            else:
                if board_full(the_board):
                    draw_board(the_board)
                    print('Draw!')
                    break
                else:
                    turn = 'player'

    if not play_again():
        break
