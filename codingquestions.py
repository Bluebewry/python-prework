
# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_user(user_name):
    user_name = input("\nPlease Enter Your Username: ")
    print("\nHello " + user_name + "!")
    
hello_user(None)

# B's Comment: I'm not sure if you wanted the underscore printed????? I hope this is right
#--------------------------------------------------------------------------------------------------

# Question 2 
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds(): 
    for first_odds in range(1, 100):
        if first_odds % 2 == 0:
            print()
        else:
            print(first_odds)

first_odds()

# B's Comment: I hope this is a decent way to do this 
#--------------------------------------------------------------------------------------------------

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.

a_list = [1, 9, 6, 55, 40, 19, 99]
def max_num_in_list(a_list):
    number = max(a_list)
    print(number)

max_num_in_list(a_list)

# B's Comment: I first put the list inside the function and got very confused when it didn't work... 
# hopefully this is a decent way to fulfil this task 
#--------------------------------------------------------------------------------------------------

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

a_year = int(input("\nEnter a year and I'll tell you if its a leap year: "))
def is_leap_year(a_year):
    if (a_year % 4 == 0) and (a_year % 100 != 0):
       print(True)
    elif a_year % 400 == 0:
        print(True)
    else:
        print(False)

##is_leap_year(a_year)

# B's Comment: ?????? it works but is it correct?????
#--------------------------------------------------------------------------------------------------

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

a_list = [1,2,4,5]
def is_consecutive(a_list):
    for x in a_list:
        if x + 1:
            return True
        else:
            return False

print(is_consecutive(a_list))

# B's Comment: I could not figure this out at all





        

