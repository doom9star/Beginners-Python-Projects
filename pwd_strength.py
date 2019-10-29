import random
print("========================WELCOME TO PASSWORD STRENGTH CHECKER===================")
print()
print("Enter your password below to check its strength!")
name = input("Name: ").upper()
print(f"Hey {name}! Check Your password strength below...")
print()
user_pwd = input("Enter Your Password: ")
print()

def pwd_strength_checker(user_password):

    numbers = str(list(range(1, 10)))
    alphas = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'abcdefghijklmnopqrstuvwxyz'.upper()
    lower = 'abcdefghijklmnopqrstuvwxyz'.lower()
    uplw = "".join([upper, lower])
    smbls = "!@#$%&".split()
    symbols = "".join(smbls)
    combo = list([numbers, alphas, upper, lower, symbols])
    pwd_length = len(user_password)

    if pwd_length > 12:
        print("Excellent Length!" ,end="")
    else:
        print("Not a good Length!",end="")

    evaluation = []
    for i in user_password:
         if i in numbers:
            evaluation.append('nas')
            continue

         elif i in uplw:
            evaluation.append('as')
            continue
         elif i in symbols:
            evaluation.append('sas')
            continue
         else:
             evaluation.append('bad')
    strength = ""
    aas = evaluation.count('as')
    nas = evaluation.count('nas')
    sas = evaluation.count('sas')
    if aas > nas and aas > sas:
        strength = "".join("""
                   ***************** 
                  | Weak Password!! |
                   ***************** 
        Try adding extra numbers and symbols to 
           make it more effective and strong.""")
    elif nas > aas and nas > sas:
        strength = "".join("""
                    *****************
                  | Medium Password!! |
                    *****************
          Try adding some symbols, other than 
              that, it's a steady password.""")
    elif sas > aas and sas > nas:
        strength = "".join("""
                    ******************
                   | Strong Password!! |
                    ******************
               Dominating and fierce Password.
                      Keep the Same!!""")
    print(strength)


pwd_strength_checker(user_pwd)
