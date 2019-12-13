import random as rd
import keyboard as kb
board_height = 25
board_width = 50
game_Over = False
snake_X = board_height//2
snake_Y = board_width//2
score = 0
fruit_X = rd.randint(1,board_height-1)
fruit_Y = rd.randint(1,board_width-1)


def setup():
    for row in range(board_height):
        for col in range(board_width):
            if row == 0:
                print("#",end="")
            elif row == board_height-1:
                print("#",end="")
            elif row == fruit_X and col == fruit_Y:
                print("$",end="")
            elif col == 0:
                print('#',end="")
            elif col == board_width-1:
                print('#',end="")
            elif row == snake_X and col == snake_Y:
                print("@",end="")
            else:
                print(" ",end="")
        print()


def play():
    if kb.is_pressed('a'):
        globals()['snake_Y'] -= 1
    elif kb.is_pressed('w'):
        globals()['snake_X'] -= 1
    elif kb.is_pressed('d'):
        globals()['snake_Y'] += 1
    elif kb.is_pressed('s'):
        globals()['snake_X'] += 1
    else:
        print(f"Your Score: {score}")
        exit("Wrong Key! Game ended")


def logic():
    if snake_Y == 0 or snake_X == 0 or snake_Y == board_width-1 or snake_X == board_height-1:
        globals()['game_Over'] = True
        print("Your Score: ",score)
        exit("Game Over")
    else:
        if snake_X == fruit_X and snake_Y == fruit_Y:
            globals()['score'] += 1
        else:
            pass


def main():
    setup()
    while not game_Over:
        play()
        logic()


main()
