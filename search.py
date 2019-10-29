import time
import random

def searcher():
    print("||||||||||||||||||||||WELCOOME TO NUMBER SEARCH ACADEMY|||||||||||||||||||||")
    print()
    print("                     || We Provide 2 Searches here:- ||")
    print('''
                             *****************
                            |1. BINARY SEARCH |
                            |2. LINEAR SEARCH |
                             *****************
    ''')
    search_type = int(input("Search Type? "))
    if search_type == 1:
        print("============================WELCOME TO BINARY SEARCH==========================")
        rnge = int(input("How many numbers do you want? "))
        print()
        step = int(input("How many steps between nums? "))
        print()
        print("Generating....")
        if rnge > 100:
            time.sleep(2)
        else:
            time.sleep(1)
        print()

        def binary_search(num):
            lst = list(range(0,num+1,step))
            count = len(lst)
            search_num = int(input("Which Number do you want? "))
            low = 0
            high = count
            loc = -1
            while low <= high:
                mid = (low+high)//2
                if lst[mid] == search_num:
                    loc = mid
                    break
                elif search_num < lst[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            print("The Location of the element is: {}.".format(loc))

        binary_search(rnge)

    else:
        print("==============================WELCOME TO LINEAR SEARCH=======================")
        rnge = int(input("How many numbers do you want? "))
        print()
        print("Generating....")
        time.sleep(2)
        print()
        nums = list(range(0,rnge+1))
        random.shuffle(nums)
        loc = -1
        def linear_search(numbers):
            search_ele = int(input("Which Number do you want? "))
            i = 0
            while i <= len(numbers):
                if numbers[i] == search_ele:
                    loc = i
                    break
                i += 1
            print(numbers)
            print(f"The Location of the element is: {loc}")
        linear_search(nums)      

searcher()
