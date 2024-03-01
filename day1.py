number=int(input("enter number between 20:50 "))

if number <= 50 and number >= 20:
    print("number is between 20 and 50")
else:
    print("out of range")



def calculate(length,width):
    area=length*width
    perimeter = 2 * (length + width)
    return area,perimeter
area, perimeter = calculate(10, 20)
print("Area:", area)
print("Perimeter:", perimeter)

def concat(str1, str2):
    concatstr = str1 + str2
    return concatstr

print(concat("esraa","magdy"))

def concat(str1, str2):
    concatstr=f"{str1}{str2}"
    return concatstr
print(concat("esraa","magdy"))

# 4- Write a function receive list of values , square each element in a given list and return the squared list


def sq(list):
    for i in range(len(list)):
        list[i]=list[i]**2
    return list

print(sq([1,2,3,4,5,6,7,8,9,10]))


# 5- Implement a program to merge two dictionaries and return the result

def merge_dict(dict1, dict2):
    merged={**dict1,**dict2}
    return merged

print(merge_dict({"a":1, "b":2}, {"c":3, "d":4}))

# 6- Write a function receive two lists and merge them.

def merge_list(list1, list2):
    merged=list1+list2
    return merged

print(merge_list([1,2,3,4],[5,6,7,8]))

# 7- Write a function to check if these keys (job, card_number) exists in this dictionary 
dict={"name": "jone", "email": "jane@outlook.com", "age": 25,"job": "engineer", "address": "cairo, Egypt"}

def check_extists(dict,keys):
    for key in keys:
        if key not in dict:
            return False
        else:
            return True


print(check_extists(dict,["job","card_number"]))


# 8- Write a program that calculates the sum of numbers from 1 to 100 using a loop and print the result

def calculate_sum():
    sum=0
    for i in range(101):
        sum=sum+i
    return sum

print(calculate_sum())

# 9- Write a function to check if a given number is even or odd.

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(10))

# 10- Write a function to reverse a given string.


def reverse_string(string):
    reversed=""
    for i in range(len(string)-1,-1,-1):
        reversed+=string[i]
    return reversed

print(reverse_string("hello"))    


# 11- Write a function to check if a given string is a palindrome (reads the same backward as forward).

def palindrome(string):
    for i in range(len(string)):
        if string[i]!= string[len(string)-i-1]:
            return False
    return True

print(palindrome("mom"))

# 12- Write a function that removes even numbers from a list and squares the remaining odd numbers.

def filter_function(list):
    square = []
    for i in range(len(list)):
        if i % 2 != 0:
            square.append(i**2)
    return square

print(filter_function([1,2,3,4,5,6,7,8,9]))

# 13- Implement a function to check if a number is prime or not.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7)) 

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5)) 

# 15- Create a Python function that takes a list of numbers, performs various operations (sum, minimum, maximum, squared list), and returns a new list containing the results.

def calculator(numbers):
    return {
        'sum': sum(numbers),
        'minimum': min(numbers),
        'maximum': max(numbers),
        'squared_list': [num**2 for num in numbers]
    }

numbers_list = [1, 2, 3, 4, 5]
print(calculator(numbers_list))









                   


