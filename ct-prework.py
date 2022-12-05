# Question 1
# Write a function to print "hello_USERNAME!"
# USERNAME is the input of the function.
# The first line of the code has been defined as below:

def hello_name(username):
    print(f"Hello {username}!")

hello_name("Eitan")


# Question 2
# Write a python function called first_odds that prints
# the odd numbers from 1-100 and returns nothing:

def first_odds():
    odd_numbers = []
    for num in range(100):
        if num % 2 == 1:
            odd_numbers.append(num)
        else:
            continue
    print(odd_numbers)

first_odds()


# Question 3
# Please write a Python function called max_num_in_list
# to return the max number of a given list.
# The first line of the code has been defined as below:
   
def max_num_in_list(a_list):
    for num in a_list:
        if num > a_list[0]:
            a_list[0] = num
        else:
            continue

    max_num = a_list[0]
    print(max_num)

num_list = [4, 77, 343, 2, 33, 37, 499, 396, 22, 4899, 4, 2278]
max_num_in_list(num_list)


# Question 4
# Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100,
# unless it is also divisible by 400. The return should be boolean Type (true/false):

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print("This is a leap year.")
    elif a_year % 4 == 0 and a_year % 400 == 0: 
        print("This is a leap year.")
    else:
        print("This is not a leap year")

chosen_year = int(input("Choose a year: "))
is_leap_year(chosen_year)

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers,
# but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    for num in a_list:
        if a_list[0] + 1 == a_list[1]:
            a_list.remove(a_list[0])
        else:
            print("This is not a consecutive list.")
            a_list = False
            break
    if a_list != False:
        print("This is a consecutive list.")

my_list = [2,3,4,5,6,7]
is_consecutive(my_list)
