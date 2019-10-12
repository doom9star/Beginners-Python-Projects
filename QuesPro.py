#=======================SUPER CLASS===========================================#
class Fillups:
    def __init__(self,question,answer):
        self.question = question
        self.answer = answer

#=======================QUESTIONS AND ANSWERS==================================#
points = 0
print("Fill in the blanks!({})".format("5*1=5"))
print()
prompts = ["Q1: (__%s__) is the capital of india?","Q2: (__%s__) is the capital of Karnataka?","Q3: (__%s__) is the God's own state of India?","Q4: There are (__%u__) of states in India?","Q5: There are (__%u__) union territories in India?"]

question1 = Fillups(prompts[0],'New delhi')
question2 = Fillups(prompts[1],'Bangalore')
question3 = Fillups(prompts[2],'Kerala')
question4 = Fillups(prompts[3], 29)
question5 = Fillups(prompts[4], 6)


answer1 = question1.answer
answer2 = question2.answer
answer3 = question3.answer
answer4 = question4.answer
answer5 = question5.answer

#===========================QUESTION ANALYSIS===================================#
def ques1_checker(answer):
    if answer == answer1:
        print("You got it right!!")
        globals()
        globals()["points"] += 1
        print(prompts[0][4:len(prompts[0])-1] %(answer1))
    else:
        print(f"Sorry! It is wrong. \nAns is: {answer1}")

def ques2_checker(answer):
    if answer == answer2:
        print("You got it right!!")
        globals()
        globals()["points"] += 1
        print(prompts[1][4:len(prompts[1])-1] %(answer2))
    else:
        print(f"Sorry! It is wrong. \nAns is: {answer2}")

def ques3_checker(answer):
    if answer == answer3:
        print("You got it right!!")
        globals()
        globals()["points"] += 1
        print(prompts[2][4:len(prompts[2])-1] %(answer3))
    else:
        print(f"Sorry! It is wrong. \nAns is: {answer3}")

def ques4_checker(answer):
    if answer == answer4:
        print("You got it right!!")
        globals()
        globals()["points"] += 1
        print(prompts[3][4:len(prompts[3])-1] %(answer4))
    else:
        print(f"Sorry! It is wrong. \nAns is: {answer4}")

def ques5_checker(answer):
    if answer == answer5:
        print("You got it right!!")
        globals()
        globals()["points"] += 1
        print(prompts[4][4:len(prompts[2])-1] %(answer5))
    else:
        print(f"Sorry! It is wrong. \nAns is: {answer5}\n")
#=======================POINTS ANALYISIS=====================================#

def point_checker():
    if globals()["points"] == 0:
        print("Sorry! You need to improve!!!!")
        print("You got {}/{} correct!!!".format(points,5))
    elif globals()["points"] == 1:
        print("You are good! Keep it up!")
        print("You got {}/{} correct!!!".format(points,5))
    elif globals()["points"] == 2:
        print("You are very good !!!")
        print("You got {}/{} correct!!!".format(points,5))
    elif globals()["points"] == 3:
        print("You are smart! Keep it up!!")
        print("You got {}/{} correct!!!".format(points,5))
    elif globals()["points"] == 4:
        print("Incredible! You are very Smart!!!")
        print("You got {}/{} correct!!!".format(points,5))
    else:
        print("You are a Extraordinary Genius !!!")
        print("You got {}/{} correct!!!".format(points,5))
        
#=======================MAIN FUNCTION========================================#

def ques_prompter():

    print(question1.question)
    ans1 = input("Ans: ")
    ques1_checker(ans1.lower().capitalize())
    
    print()
    
    print(question2.question)
    ans2 = input("Ans: ")
    ques2_checker(ans2.lower().capitalize())

    print()
    
    print(question3.question)
    ans3 = input("Ans: ")
    ques3_checker(ans3.lower().capitalize())

    print()
    
    print(question4.question)
    ans4 = int(input("Ans: "))
    ques4_checker(ans4)

    print()
    
    print(question5.question)
    ans5 = int(input("Ans: "))
    ques5_checker(ans5)
    
    point_checker()
    
#=======================EXECUTION==============#
    
ques_prompter()
