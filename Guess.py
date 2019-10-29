import random

def num_generator():
    num = random.randint(0,50)
    return num

def alpha_generator():
    alph = random.choice("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z")
    return alph

print("======================Welcome to the Guessing Game!==========================")
home = ('''
                         1. |===START==|
                            |          |
                         2. |===STOP===| 
                            |          |
                         3. |===HELP===|
                            |          |
                         4. |===QUIT===|
''')
print(home)
while True:
    guess_count = 0
    guess_limit = 3
    Out_of_guesses = False
    started = False
    choice = input('>>>').lower()
    if choice == 'start':
        print('''                                1. GENERATE A NUMBER(1-50)
                                2. GENERATE AN ALPHABET(a-z)
''')
        preference = int(input(">>>"))
        if preference == 1:
                num = num_generator()
                print("Number Has Been Generated!! You Got 3 Guesses! Can You Guess That Number? ")
                while not Out_of_guesses:
                    if guess_count < guess_limit:
                        guess_count += 1
                        num_guess = int(input("Enter the Number: "))
                        if num_guess == num:
                            print("Congratulations! You Guessed It Right!!")
                            break
                        elif num_guess > num:
                            print("[HINT] You Guessed it Too High!")
                        else:
                            print("[HINT] You Guessed it Too Low!")
                    else:
                        Out_of_gusses = True
                        print("Sorry! Your Out of Guesses!!")
                        print("Number is {}".format(num))
                        break
        else:
            alphabet = alpha_generator()
            print("An Alphabet has been generated! You Got 3 Guesses! Can You Guess that alphabet? ")
            while not Out_of_guesses:
                    if guess_count < guess_limit:
                        guess_count += 1
                        alpha_guess = input("Enter the Alphabet: ")
                        guess_count += 1
                        if alpha_guess == alphabet:
                            print("Congratulations! You Guessed It Right!!")
                            break
                        elif alpha_guess > alphabet:
                            print("[HINT] Your Guess is too high!")
                        else:
                            print("[HINT] Your Guess is too low")
                    else:
                        Out_of_guesses = True
                        print("Sorry! Your Out of Guesses!!")
                        print("Alphabet is {}".format(alphabet)) 
                        break
                
    elif choice == 'stop':
        if not started:
            print("Game is already stopped!")
        else:
            started = False
            print("Game Stopped!")
            print()
            print(home)
    elif choice == 'help':
        print('''
This is a guessing game. Enjoy and peace!!!
''')
    elif choice == 'quit':
        print("STAY SAFE! GOODBYE!")
        break
    else:
        print("Sorry! I don't understand this...")


                
