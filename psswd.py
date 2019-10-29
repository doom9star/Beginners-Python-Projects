import random
print("***************************WELCOME TO PASSWORD GENERATOR************************")
print("Type YES/NO for the following questions.")
print("These Questions determine the strength of your PASSWORD!")
print()
def pwd_startup():
    pwd_length = int(input("Password Length: "))
    print()
    print("Getting things ready....")
    print()
    sym = input("Symbols? ")
    print()
    if sym == 'yes':
        print("Allright!")
        print("Strengthening....")
        print()
    else:
        print("OK")
        print()
    alphanum = input("Mixture of upper-case & lower-case alphanumeric characters? ")
    print()
    if alphanum == 'yes':
        print("Fine!")
        print("Hackers ain't gonna have a chance!...")
        print()
    else:
        print("Compressing and joining.....!")
        print()
    return pwd_length,sym,alphanum

dicto = {
        'numbers' : list(range(1,10)),
        'alphas' : 'abcdefghijklmnopqrstuvwxyz',
        'alphabets' : 'abcdefghijklmnopqrstuvwxyz'.split(','),
        'upper' : 'abcdefghijklmnopqrstuvwxyz'.upper(),
        'lower' : 'abcdefghijklmnopqrstuvwxyz'.lower(),
        'symbols' : "!@#$%&"
        }
def pwd_generator(password_length,numbers,alphabets,alphas,upper,lower,symbols):
    if globals()['s'] == 'yes' and globals()['an'] == 'yes': 
        emp_lst = []
        for i in range(password_length):
            n = str(random.choice(numbers))
            a = random.choice(alphas)
            u = random.choice(upper)
            l = random.choice(lower)
            s = random.choice(symbols)
            lst = [n,a,u,l,s]
            choice = random.choice(lst)
            emp_lst.append(choice)
    elif globals()['s'] == 'no' and globals()['an'] == 'yes':
        emp_lst = []
        for i in range(password_length):
            n = str(random.choice(numbers))
            a = random.choice(alphas)
            u = random.choice(upper)
            l = random.choice(lower)
            lst = [n,a,u,l]
            choice = random.choice(lst)
            emp_lst.append(choice)
    elif globals()['s'] == 'yes' and globals()['an'] == 'no':
        emp_lst = []
        for i in range(password_length):
            n = str(random.choice(numbers))
            a = random.choice(alphas)
            s = random.choice(symbols)
            l = random.choice(lower)
            lst = [n,a,l,s]
            choice = random.choice(lst)
            emp_lst.append(choice)
    else:
        emp_lst = []
        for i in range(password_length):
            n = str(random.choice(numbers))
            a = random.choice(alphas)
            l = random.choice(lower)
            lst = [n,a,l]
            choice = random.choice(lst)
            emp_lst.append(choice)
        
    password = "".join(emp_lst)
    print()
    print(f"Your Final Password: {password}")

pwdlen,s,an = pwd_startup()
pwd_generator(pwdlen,dicto['numbers'],dicto['alphabets'],dicto['alphas'],dicto['upper'],dicto['lower'],dicto['symbols'])

