import random
import sys
print("====================WELCOME TO ROCK,PAPER AND SCISSORS GAME====================")
user = input("Player Name: ")
print(f"*****************************WELCOME {user}!!*******************************")
rund = 0
def computer():
    choice = random.choice(['rock','paper','scissor'])
    return choice

print('''
                              ____________
                             |  1. START  |
                             |  2. STOP   |
                             |  3. HELP   |
                             |  4. QUIT   |
                              ************
''')

home = ('''
                               _____________
                              |  1. Rock    |
                              |  2. Paper   |          
                              |  3. Scissor |
                               *************
        ''')

user_point = 0
comp_point = 0
while True:
        choice = input("<<<").lower()
        if choice == 'start':
            no_of_sets = int(input("No Of Sets You Wanna Play:  "))
            ready = input("Are You Ready? ").lower()
            if ready == 'yes':
                print(f"                            {user}   VS    COMPUTER")
                print(f"{user} Points : {user_point}")
                print(f"Computer Points : {comp_point}")
                print(home)
                
                while True:
                    if rund < no_of_sets:
                        rund += 1
                        user_pref = input("Your Choice: ").lower()
                        comp_pref = computer() 
                        if user_pref == 'rock' and comp_pref == 'rock':
                            print(f'''
                        COMPUTER : {comp_pref}  |  {user} : {user_pref}
               ''')
                            print("TIE")
                            print(f"{user} Points : {user_point}")
                            print(f"Computer Points : {comp_point}")
                            print(home)
                        elif user_pref == 'rock' and comp_pref == 'scissor':
                            user_point += 1
                            print(f'''
                        COMPUTER : {comp_pref}  |  {user} : {user_pref}
                ''')
                            print(f"{user} Points : {user_point}")
                            print(f"Computer Points : {comp_point}")
                            print(home)
                            
                        elif user_pref == 'paper' and comp_pref == 'rock':
                            user_point += 1
                            print(f'''
                        COMPUTER : {comp_pref}  |  {user} : {user_pref}
                ''')
                            print(f"{user} Points : {user_point}")
                            print(f"Computer Points : {comp_point}")
                            print(home)

                        elif user_pref == 'scissor' and comp_pref == 'rock':
                            comp_point += 1
                            print(f'''
                        COMPUTER : {comp_pref}  |  {user} : {user_pref}
                ''')
                            print(f"{user} Points : {user_point}")
                            print(f"Computer Points : {comp_point}")
                            print(home)
                            
                        elif user_pref == 'paper' and comp_pref == 'scissor':
                            comp_point += 1
                            print(f'''
                        COMPUTER : {comp_pref}  |  {user} : {user_pref}
                ''')
                            print(f"{user} Points : {user_point}")
                            print(f"Computer Points : {comp_point}")
                            print(home)
                            
                        elif user_pref == 'paper' and comp_pref == 'paper':
                            print(f'''
                        COMPUTER : {comp_pref}  |  {user} : {user_pref}
                ''')
                            print("TIE")
                            print(f"{user} Points : {user_point}")
                            print(f"Computer Points : {comp_point}")
                            print(home)
                            
                        elif user_pref == 'rock' and comp_pref == 'paper':
                            comp_point += 1
                            print(f'''
                        COMPUTER : {comp_pref}  |  {user} : {user_pref}
                ''')
                            print(f"{user} Points : {user_point}")
                            print(f"Computer Points : {comp_point}")
                            print(home)
                            
                        elif user_pref == 'scissor' and comp_pref == 'scissor':
                            print(f'''
                        COMPUTER : {comp_pref}  |  {user} : {user_pref}
                ''')
                            print("TIE")
                            print(f"{user} Points : {user_point}")
                            print(f"Computer Points : {comp_point}")
                            print(home)
                            
                        elif user_pref == 'scissor' and comp_pref == 'paper':
                            print(f'''     
                         COMPUTER : {comp_pref}  |  {user} : {user_pref}                        
                ''')
                            user_point += 1
                            print(f"{user} Points : {user_point}")
                            print(f"Computer Points : {comp_point}")
                            print(home)
                            
                    else:
                            print(f"{user} Points : {user_point}")
                            print(f"Computer Points : {comp_point}")
                            if user_point == comp_point:
                                print("TIE")
                            elif user_point < comp_point:
                                print("|*|*|*|*|*Computer Wins|*|*|*|*|**")
                            else:
                                print(f"|*|*|*|*|*{user} Wins|*|*|*|*|*|*")
                            break
            else:
                sys.exit()
                        
        elif choice == 'stop':
            print(f"                    {user} Points : {user_point}")
            print(f"                    Computer Points : {comp_point}")
            if user_point == comp_point:
                print("TIE")
            elif user_point < comp_point:
                print("|*|*|*|*|*Computer Wins|*|*|*|*|**")
            else:
                print(f"|*|*|*|*|*{user} Wins|*|*|*|*|*|*")
            break
        elif choice == 'help':
            print("This is a Rock,Paper,Scissor Game. Stay happy And Enjoy")
        elif choice == 'quit':
            print("GOODBYE!")
            break
        else:
            print("Sorry! I don't understand this...")

        
            
            
            
            
    
