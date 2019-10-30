import time
import random

def main():
    def prompter():
        print("==================================GUESS THE WORD===============================")
        print()
        print('''
                                  *************
                                | 1. ANIMALS   |
                                | 2. FLOWERS   |
                                | 3. VEGETABLES|
                                | 4. FRUITS    |
                                | 5. VEHICLES  |
                                | 6. BIRDS     |
                                  *************
                                  
                         (TYPE THE NUMBERS NOT WORDS)
                             
        ''')
        print()
        choice = int(input("Which Genre you wanna play the game? "))
        print()
        print("Generating Words....")
        time.sleep(3)
        print()
        print("Generated! You got 3 chances, Guess wisely!")
        print()
        return choice

    animals = ['cat','bear','dog','lion','tiger','girrafe','zebra','crocodile','gorilla','monkey','dragon','dinosaur']
    flowers = ['lily','lotus','hibiscus','sunflower','jasmine','rose','orchid','tulasi']
    vegetables = ['onion','cauliflower','tomato','brinjal','capsicum','ladysfinger',]
    fruits = ['apple','bannana','mango','pomegranate','strawberry','orange','watermelon','pineapple','custodapple','pea']
    vehicles = ['lori','bike','bus','motorcycle','cycle','car','aeroplane','auto','train','ship','rocket']
    birds = ['peacock','pigeon','parrot','crow','owl','mosquito']

    choice = prompter()

    def choice_analyser(choice):
        guess_count = 0
        guess_limit = 3
        out_of_guesses = False
        if choice == 1:
            secret_word = random.choice(animals)
            while not out_of_guesses:
                if guess_count < guess_limit:
                    guess = input("Your Guess: ")
                    guess_count += 1
                    if guess == secret_word:
                        print("Congrats! You Guessed it right!!")
                        break
                    else:
                        if guess_count == 3:
                            continue
                        else:
                            print("Try again!")
                            print()
                            continue
                else:
                    out_of_guesses = True
                    print("Sorry! Your Out Of Guesses")
                    print()
                    print(f"Secret Word: {secret_word}")
                    
        elif choice == 2:
            secret_word = random.choice(flowers)
            while not out_of_guesses:
                if guess_count < guess_limit:
                    guess = input("Your Guess: ")
                    guess_count += 1
                    if guess == secret_word:
                        print("Congrats! You Guessed it right!!")
                        break
                    else:
                        if guess_count == 3:
                            break
                        else:
                            if guess_count == 3:
                                continue
                            else:
                                print("Try again!")
                                print()
                                continue
                else:
                    out_of_guesses = True
                    print("Sorry! Your Out Of Guesses")
                    print()
                    print(f"Secret Word: {secret_word}")
                    
        elif choice == 3:
            secret_word = random.choice(vegetables)
            while not out_of_guesses:
                if guess_count < guess_limit:
                    guess = input("Your Guess: ")
                    if guess == secret_word:
                        print("Congrats! You Guessed it right!!")
                        break
                    else:
                       if guess_count == 2:
                            break
                       else:
                           if guess_count == 3:
                               continue
                           else:
                               print("Try again!")
                               print()
                               continue
                else:
                    out_of_guesses = True
                    print("Sorry! Your Out Of Guesses")
                    print()
                    print(f"Secret Word: {secret_word}")
                    
        if choice == 4:
            secret_word = random.choice(fruits)
            while not out_of_guesses:
                if guess_count < guess_limit:
                    guess = input("Your Guess: ")
                    guess_count += 1
                    if guess == secret_word:
                        print("Congrats! You Guessed it right!!")
                        break
                    else:
                        if guess_count == 2:
                            break
                        else:
                            if guess_count == 3:
                                continue
                            else:
                                print("Try again!")
                                print()
                                continue
                else:
                    out_of_guesses = True
                    print("Sorry! Your Out Of Guesses")
                    print()
                    print(f"Secret Word: {secret_word}")
                    
        if choice == 5:
            secret_word = random.choice(vehicles)
            while not out_of_guesses:
                if guess_count < guess_limit:
                    guess = input("Your Guess: ")
                    guess_count += 1
                    if guess == secret_word:
                        print("Congrats! You Guessed it right!!")
                        break
                    else:
                        if guess_count == 2:
                            break
                        else:
                            if guess_count == 3:
                                continue
                            else:
                                print("Try again!")
                                print()
                                continue
                else:
                    out_of_guesses = True
                    print("Sorry! Your Out Of Guesses")
                    print()
                    print(f"Secret Word: {secret_word}")
                    
        if choice == 6:
            secret_word = random.choice(birds)
            while not out_of_guesses:
                if guess_count < guess_limit:
                    guess = input("Your Guess: ")
                    guess_count += 1
                    if guess == secret_word:
                        print("Congrats! You Guessed it right!!")
                        break
                    else:
                        if guess_count == 2:
                            break
                        else:
                            if guess_count == 3:
                                continue
                            else:
                                print("Try again!")
                                print()
                                continue
                else:
                    out_of_guesses = True
                    print("Sorry! Your Out Of Guesses")
                    print()
                    print(f"Secret Word: {secret_word}")
                    
    choice_analyser(choice)


main()     
