import random
import time

board = [["[ ]", "[ ]", "[ ]"]
        ["[ ]", "[ ]", "[ ]"]
        ["[ ]", "[ ]", "[ ]"]]


def who_goes_first():
    n = random.randint(0, 1)
    return 'x' if n == 1 else 'o'


def user_make_guess():
    print("Enter your coordinates.")
    c1 = input()
    c2 = input()
    print_new_user_board(c1, c2)


def computer_make_guess():
    for i in board:
        for j in board[i]:
            if board[i][j] == " ":
                possible = random.randint(0, 1)
                if possible == 1:
                    print_new_computer_board(i, j)
                    break


def print_new_user_board(c1, c2):
    board[c1][c2] = userLetter
    print(board)


def print_new_computer_board(i, j):
    board[i][j] = computerLetter
    print(board)


userLetter = input("Welcome to Tic-Tac-Toe! Would you like to be x or o?")
computerLetter = 'x' if userLetter == 'o' else 'o'
print("Great! When it's your turn, enter the coordinates of where you want to mark your letter.")
print("The values (0,0) refer to the top-left box.")
time.sleep(2)
wgf = who_goes_first()
print("By random chance, " + wgf + "goes first.")


print("Let the game begin!")
print(board)


while board[0] != userLetter and board[0] != computerLetter:
    if userLetter == wgf:
        user_make_guess()
    else:
        computer_make_guess()