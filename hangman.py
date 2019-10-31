import time
import sys
import random

def main():
    
    def prompter():
        print("=============================WELCOME TO THE HANGMAN GAME=====================")
        print()
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
        print("Generating...")
        time.sleep(2)
        print()
        return choice
        
    choice = prompter()

    def choice_analyser(choice):
        
        animals = ['cat','bear','dog','lion','tiger','girrafe','zebra','crocodile','gorilla','monkey','dragon','dinosaur']
        flowers = ['lily','lotus','hibiscus','sunflower','jasmine','rose','orchid','tulasi']
        vegetables = ['onion','cauliflower','tomato','brinjal','capsicum','ladysfinger',]
        fruits = ['apple','bannana','mango','pomegranate','strawberry','orange','watermelon','pineapple','custodapple','pea']
        vehicles = ['lori','bike','bus','motorcycle','cycle','car','aeroplane','auto','train','ship','rocket']
        birds = ['peacock','pigeon','parrot','crow','owl','mosquito']

        secret_animal = random.choice(animals)
        secret_flower = random.choice(flowers)
        secret_vegetable = random.choice(vegetables)
        secret_fruit = random.choice(fruits)
        secret_vehicle = random.choice(vehicles)
        secret_bird = random.choice(birds)

        def duplicates(lst,item):
            return [i for i,x in enumerate(lst) if x == item]
        
        guess_count = 0
        guess_limit = 10
        out_of_guesses = False
        
        if choice == 1:
            word = secret_animal
            print("Generated!! Guess the animal by typing letters! ")
            print()
            words = list(word)
            length = len(words)
            dashed = []
            finale = []
            finale1 = finale.copy()
            finale.append(words[0])
            for i in range(1,len(words)-1):
                finale.append('_')
            finale.append(words[-1])
            print("You got 10 chances! Let's Go!!!!")
            print()
            print(finale)
            print()
            chances = 10
            while not out_of_guesses:
                if guess_count < guess_limit:
                    guess = input("Guess the letter: ")
                    print()
                    guess_count += 1
                    chances -= 1
                    if guess in words:
                        count = words.count(guess)
                        if count > 1:
                            lst_of_index = duplicates(words,guess)
                            index1 = lst_of_index[0]
                            index2 = lst_of_index[1]
                            finale[index1] = guess
                            finale[index2] = guess
                        else:
                            index = words.index(guess)
                            finale[index] = guess
                            
                        if finale == words:
                            print("Well Done! You guessed it right!")
                            print(word)
                            break
                        else:
                            print(f"         ==========================>                          Chances left: {chances}")
                            print("Good..")
                            print(finale)
                            print()
                            continue
                    else:
                        print(f"         ==========================>                          Chances left: {chances}")
                        print("Try Again!")
                        print(finale)
                        print()
                        continue
                else:
                    out_of_guesses = True
                    print("GAME OVER")
                    print(f"Secret Word: {word}")
                    break

        elif choice == 2:
            word = secret_flower
            print("Generated!! Guess the flower by typing letters! ")
            print()
            words = list(word)
            length = len(words)
            dashed = []
            finale = []
            finale1 = finale.copy()
            finale.append(words[0])
            for i in range(1,len(words)-1):
                finale.append('_')
            finale.append(words[-1])
            print("You got 10 chances! Let's Go!!!!")
            print()
            print(finale)
            print()
            chances = 10
            while not out_of_guesses:
                if guess_count < guess_limit:
                    guess = input("Guess the letter: ")
                    print()
                    guess_count += 1
                    chances -= 1
                    if guess in words:
                        count = words.count(guess)
                        if count > 1:
                            lst_of_index = duplicates(words,guess)
                            index1 = lst_of_index[0]
                            index2 = lst_of_index[1]
                            finale[index1] = guess
                            finale[index2] = guess
                        else:
                            index = words.index(guess)
                            finale[index] = guess
                            
                        if finale == words:
                            print("Well Done! You guessed it right!")
                            print(word)
                            break
                        else:
                            print(f"         ==========================>                          Chances left: {chances}")
                            print("Good..")
                            print(finale)
                            print()
                            continue
                    else:
                        print(f"         ==========================>                          Chances left: {chances}")
                        print("Try Again!")
                        print(finale)
                        print()
                        continue
                else:
                    out_of_guesses = True
                    print("GAME OVER")
                    print(f"Secret Word: {word}")
                    break

        elif choice == 3:
            word = secret_vegetable
            print("Generated!! Guess the vegetable by typing letters! ")
            print()
            words = list(word)
            length = len(words)
            dashed = []
            finale = []
            finale1 = finale.copy()
            finale.append(words[0])
            for i in range(1,len(words)-1):
                finale.append('_')
            finale.append(words[-1])
            print("You got 10 chances! Let's Go!!!!")
            print()
            print(finale)
            print()
            chances = 10
            while not out_of_guesses:
                if guess_count < guess_limit:
                    guess = input("Guess the letter: ")
                    print()
                    guess_count += 1
                    chances -= 1
                    if guess in words:
                        count = words.count(guess)
                        if count > 1:
                            lst_of_index = duplicates(words,guess)
                            index1 = lst_of_index[0]
                            index2 = lst_of_index[1]
                            finale[index1] = guess
                            finale[index2] = guess
                        else:
                            index = words.index(guess)
                            finale[index] = guess
                            
                        if finale == words:
                            print("Well Done! You guessed it right!")
                            print(word)
                            break
                        else:
                            print(f"         ==========================>                          Chances left: {chances}")
                            print("Good..")
                            print(finale)
                            print()
                            continue
                    else:
                        print(f"         ==========================>                          Chances left: {chances}")
                        print("Try Again!")
                        print(finale)
                        print()
                        continue
                else:
                    out_of_guesses = True
                    print("GAME OVER")
                    print(f"Secret Word: {word}")
                    break

        elif choice == 4:
            word = secret_fruit
            print("Generated!! Guess the fruit by typing letters! ")
            print()
            words = list(word)
            length = len(words)
            dashed = []
            finale = []
            finale1 = finale.copy()
            finale.append(words[0])
            for i in range(1,len(words)-1):
                finale.append('_')
            finale.append(words[-1])
            print("You got 10 chances! Let's Go!!!!")
            print()
            print(finale)
            print()
            chances = 10
            while not out_of_guesses:
                if guess_count < guess_limit:
                    guess = input("Guess the letter: ")
                    print()
                    guess_count += 1
                    chances -= 1
                    if guess in words:
                        count = words.count(guess)
                        if count > 1:
                            lst_of_index = duplicates(words,guess)
                            index1 = lst_of_index[0]
                            index2 = lst_of_index[1]
                            finale[index1] = guess
                            finale[index2] = guess
                        else:
                            index = words.index(guess)
                            finale[index] = guess
                            
                        if finale == words:
                            print("Well Done! You guessed it right!")
                            print(word)
                            break
                        else:
                            print(f"         ==========================>                          Chances left: {chances}")
                            print("Good..")
                            print(finale)
                            print()
                            continue
                    else:
                        print(f"         ==========================>                          Chances left: {chances}")
                        print("Try Again!")
                        print(finale)
                        print()
                        continue
                else:
                    out_of_guesses = True
                    print("GAME OVER")
                    print(f"Secret Word: {word}")
                    break

        elif choice == 5:
            word = secret_vehicle
            print("Generated!! Guess the vehicle by typing letters! ")
            print()
            words = list(word)
            length = len(words)
            dashed = []
            finale = []
            finale1 = finale.copy()
            finale.append(words[0])
            for i in range(1,len(words)-1):
                finale.append('_')
            finale.append(words[-1])
            print("You got 10 chances! Let's Go!!!!")
            print()
            print(finale)
            print()
            chances = 10
            while not out_of_guesses:
                if guess_count < guess_limit:
                    guess = input("Guess the letter: ")
                    print()
                    guess_count += 1
                    chances -= 1                    
                    if guess in words:
                        count = words.count(guess)
                        if count > 1:
                            lst_of_index = duplicates(words,guess)
                            index1 = lst_of_index[0]
                            index2 = lst_of_index[1]
                            finale[index1] = guess
                            finale[index2] = guess
                        else:
                            index = words.index(guess)
                            finale[index] = guess
                            
                        if finale == words:
                            print("Well Done! You guessed it right!")
                            print(word)
                            break
                        else:
                            print(f"         ==========================>                          Chances left: {chances}")
                            print("Good..")
                            print(finale)
                            print()
                            continue
                    else:
                        print(f"         ==========================>                          Chances left: {chances}")
                        print("Try Again!")
                        print(finale)
                        print()
                        continue
                else:
                    out_of_guesses = True
                    print("GAME OVER")
                    print(f"Secret Word: {word}")
                    break

        elif choice == 6:
            word = secret_bird
            print("Generated!! Guess the bird by typing letters! ")
            print()
            words = list(word)
            length = len(words)
            dashed = []
            finale = []
            finale1 = finale.copy()
            finale.append(words[0])
            for i in range(1,len(words)-1):
                finale.append('_')
            finale.append(words[-1])
            print("You got 10 chances! Let's Go!!!!")
            print()
            print(finale)
            print()
            chances = 10
            while not out_of_guesses:
                if guess_count < guess_limit:
                    guess = input("Guess the letter: ")
                    print()
                    guess_count += 1
                    chances -= 1
                    if guess in words:
                        count = words.count(guess)
                        if count > 1:
                            lst_of_index = duplicates(words,guess)
                            index1 = lst_of_index[0]
                            index2 = lst_of_index[1]
                            finale[index1] = guess
                            finale[index2] = guess
                        else:
                            index = words.index(guess)
                            finale[index] = guess
                            
                        if finale == words:
                            print("Well Done! You guessed it right!")
                            print(word)
                            break
                        else:
                            print(f"         ==========================>                          Chances left: {chances}")
                            print("Good..")
                            print(finale)
                            print()
                            continue
                    else:
                        print(f"         ==========================>                          Chances left: {chances}")
                        print("Try Again!")
                        print(finale)
                        print()
                        continue
                else:
                    out_of_guesses = True
                    print("GAME OVER")
                    print(f"Secret Word: {word}")
                    break
        else:
            print("Sorry! I don't understand this...")
            sys.exit("Game Exited.")
            
    choice_analyser(choice)

main()




















