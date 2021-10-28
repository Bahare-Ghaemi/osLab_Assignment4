import random
import datetime

a = datetime.datetime.now()
game = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]

class Color:
    red = '\033[91m'
    green = '\033[92m'
    END = '\033[0m'

x = 0
y = 0

def show_game_board():
    for i in range(3):
        for j in range(3):
            if game[i][j] == 'X':
                print(Color.green + game[i][j] + Color.END ,end=" ")
            elif game[i][j] == 'O':
                print(Color.red + game[i][j] + Color.END ,end=" ")
            else:
                print(game[i][j],end=" ")

        print()
    print("--------------")

def check_game_X():
    if game[0][0] == 'X' and game[0][1] == 'X' and  game[0][2] == 'X':
        print("Player1 wins!")
        x = 1
        b = datetime.datetime.now()
        c = b - a
        print("TIME : ", int(c.total_seconds()))
        exit()
    elif game[1][0] == 'X' and game[1][1] == 'X' and  game[1][2] == 'X':
        print("Player1 wins!")
        x = 1
        b = datetime.datetime.now()
        c = b - a
        print("TIME(s) : ", int(c.total_seconds()))
        exit()
    elif game[2][0] == 'X' and game[2][1] == 'X' and  game[2][2] == 'X':
        print("Player1 wins!")
        x = 1
        b = datetime.datetime.now()
        c = b - a
        print("TIME(s) : ", int(c.total_seconds()))
        exit()
    elif game[0][0] == 'X' and game[1][0] == 'X' and  game[2][0] == 'X':
        print("Player1 wins!")
        x = 1
        b = datetime.datetime.now()
        c = b - a
        print("TIME(s) : ", int(c.total_seconds()))
        exit()
    elif game[0][1] == 'X' and game[1][1] == 'X' and  game[2][1] == 'X':
        print("Player1 wins!")
        x = 1
        b = datetime.datetime.now()
        c = b - a
        print("TIME(s) : ", int(c.total_seconds()))
        exit()
    elif game[0][2] == 'X' and game[1][2] == 'X' and  game[2][2] == 'X':
        print("Player1 wins!")
        x = 1
        b = datetime.datetime.now()
        c = b - a
        print("TIME(s) : ", int(c.total_seconds()))
        exit()
    elif game[0][0] == 'X' and game[1][1] == 'X' and  game[2][2] == 'X':
        print("Player1 wins!")
        x = 1
        b = datetime.datetime.now()
        c = b - a
        print("TIME(s) : ", int(c.total_seconds()))
        exit()
    elif game[0][2] == 'X' and game[1][1] == 'X' and  game[2][0] == 'X':
        print("Player1 wins!")
        x = 1
        b = datetime.datetime.now()
        c = b - a
        print("TIME(s) : ", int(c.total_seconds()))
        exit()
    


def check_game_Y():
    if game[0][0] == 'O' and game[0][1] == 'O' and  game[0][2] == 'O':
        print("Player2 wins!")
        y = 1
        b = datetime.datetime.now()
        c = b - a
        print("TIME(s) : ", int(c.total_seconds()))
        exit()
    elif game[1][0] == 'O' and game[1][1] == 'O' and  game[1][2] == 'O':
        print("Player2 wins!")
        y = 1
        b = datetime.datetime.now()
        c = b - a
        print("TIME(s) : ", int(c.total_seconds()))
        exit()
    elif game[2][0] == 'O' and game[2][1] == 'O' and  game[2][2] == 'O':
        print("Player2 wins!")
        y = 1
        b = datetime.datetime.now()
        c = b - a
        print("TIME(s) : ", int(c.total_seconds()))
        exit()
    elif game[0][0] == 'O' and game[1][0] == 'O' and  game[2][0] == 'O':
        print("Player2 wins!")
        y = 1
        b = datetime.datetime.now()
        c = b - a
        print("TIME(s) : ", int(c.total_seconds()))
        exit()
    elif game[0][1] == 'O' and game[1][1] == 'O' and  game[2][1] == 'O':
        print("Player2 wins!")
        y = 1
        b = datetime.datetime.now()
        c = b - a
        print("TIME(s) : ", int(c.total_seconds()))
        exit()
    elif game[0][2] == 'O' and game[1][2] == 'O' and  game[2][2] == 'O':
        print("Player2 wins!")
        y = 1
        b = datetime.datetime.now()
        c = b - a
        print("TIME(s) : ", int(c.total_seconds()))
        exit()
    elif game[0][0] == 'O' and game[1][1] == 'O' and  game[2][2] == 'O':
        print("Player2 wins!")
        y = 1
        b = datetime.datetime.now()
        c = b - a
        print("TIME(s) : ", int(c.total_seconds()))
        exit()
    elif game[0][2] == 'O' and game[1][1] == 'O' and  game[2][0] == 'O':
        print("Player2 wins!")
        y = 1
        b = datetime.datetime.now()
        c = b - a
        print("TIME(s) : ", int(c.total_seconds()))
        exit()


def choose_side(side):
    counter = 0
    while True:
        while True:
            if side == 1:
                print(Color.green + "XXX" + Color.END + "Computer" + Color.green + "XXX" + Color.END +"\n")
                row = random.randint(0,2)
                col = random.randint(0,2)
            else:
                print(Color.green + "XXX" + Color.END + "Player1" + Color.green + "XXX" + Color.END +"\n")
                row = int(input("row : "))
                col = int(input("col : "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                if game[row][col] == '-':
                    counter += 1
                    game[row][col] = 'X'
                    if counter == 9 and x == 0 and y == 0:
                        show_game_board()
                        print("The two sides are Equal !")
                        print("The END...")
                        exit()
                    break
                else:
                    print("it is FILL!")
            else:
                print("INVALID input!")

        show_game_board()
        check_game_X()

        while True:
            print(Color.red + "OOO" + Color.END + "Player2" + Color.red + "OOO" + Color.END +"\n")
            row = int(input("row : "))
            col = int(input("col : "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                if game[row][col] == '-':
                    counter += 1
                    game[row][col] = 'O'
                    if counter == 9 and x == 0 and y == 0:
                        show_game_board()
                        print("The two sides are Equal !")
                        print("The END...")
                        b = datetime.datetime.now()
                        c = b - a
                        print("TIME : ", int(c.total_seconds()))
                        exit()
                    break
                else:
                    print("it is FILL!")
            else:
                print("INVALID input!")
        
        show_game_board()
        check_game_Y()


#------------------------------------------

print("---WELCOME TO THE GAME---")
print("1- computer vs user1")
print("2- user1 vs user2\n")
choice = int(input("enter number of ypur choice : "))
print()
show_game_board()


if choice == 1:
    choose_side(1)
else:
    choose_side(2)


