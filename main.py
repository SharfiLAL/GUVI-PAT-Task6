"""
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from typing import Any
"""
import string

from numpy.ma.core import minimum

'''
"Guess the Number"

import random
x = random.randint(1, 10)
#I have used the random module to select a number between 1 and 10.
Guess = int(input("Guess the number : "))
#I define Guess as an integer to be able to guess the number between 1 and 10.
while x != Guess:
 if Guess > x:
  print("Too High")
  print("Guess again")
  Guess = int(input("Guess the number : "))
#I have set up a loop for when the player guesses a number which is too high.
 elif Guess < x:
  print("Too Low")
  print("Guess again")
  Guess = int(input("Guess the number : "))
#the loop continues for when the player guesses a number which is too low.
 else: Guess = x
print("Correct guess")
#finally when the player guesses the correct number, this is printed.
'''

'''
"Words scramble"

import random
x = random.choice(['python', 'java', 'javascript', 'automation', 'pytest', 'guvi', 'selenium'])
#I have used the random module to randomly select a word from the list I have created
Selected_word = list(x)
#I have made list of the characters of the word which Python randomly selected
random.shuffle(Selected_word)
#The above line will let Python scramble the selected word which will then be displayed
print(Selected_word)
Guess_the_scrambled_word = str(input("Guess the scrambled word : "))
#I define a string for the player to know that they can start guessing the word
Scrambled_word = "".join(x)
#with this function I ask of Python to put the characters of the word back to its original state
#a loop is then initiated so the player can start playing or guessing
while Scrambled_word != Guess_the_scrambled_word:
  print("Incorrect guess")
  print("Guess again")
  Guess_the_scrambled_word = str(input("Guess the scrambled word : "))
#I have created a loop in order for the player to guess the scrambled word
else: Guess_the_scrambled_word = Scrambled_word
print("Correct guess")
#Finally when the guess is correct, "Correct guess" is displayed
'''

'''
#Pat Task-4

#1 Create two lists out of one, one with even numbers and one with odd numbers
def is_even(even_numbers):
    return even_numbers % 2 == 0
#define a function for the even numbers
def is_odd(odd_numbers):
    return odd_numbers % 2 == 1
#define a function for the odd numbers
Python_list = [10, 501, 22, 37,100, 999, 87, 351]
even_numbers = list(filter(is_even, Python_list))
odd_numbers = list(filter(is_odd, Python_list))
#filter out the even numbers and odd numbers
print(even_numbers)
print(odd_numbers)



#2 Count all the prime numbers
import math
#import math to perform a mathematical task
def is_prime(prime_numbers):
        if prime_numbers <= 1:
            return False
        for i in range(2, int(math.sqrt(prime_numbers)) + 1):
            if prime_numbers % i == 0:
             return False
        return True
#define the mathematical solution to detect prime numbers
Python_list = [10, 501, 22, 37,100, 999, 87, 351]
filter_prime_numbers = list(filter(is_prime, Python_list))
print(f"The prime numbers are : {filter_prime_numbers}")
#filter out the prime numbers
prime_numbers_count = len(filter_prime_numbers)
print(f"The prime numbers count is : {prime_numbers_count}")



#3 How many numbers are Happy Numbers
def is_happy(happy_num):
    seen = set()
    while happy_num != 1 and happy_num not in seen:
        seen.add(happy_num)
        sum_sq = 0
        for digit in str(happy_num):
            sum_sq += int(digit) ** 2
        happy_num = sum_sq
    return happy_num == 1
Python_list = [10, 501, 22, 37,100, 999, 87, 351]
filter_happy_num = list(filter(is_happy, Python_list))
#print(f"The happy numbers are : {filter_happy_num}")
happy_numbers_count = len(filter_happy_num)
print(f"The happy numbers count is : {happy_numbers_count}")



#4 Sum of 1st and last digit of a given integer
number = int(input("Given a number: "))
number = str(number)
#transform integer to string to find first and last digit of integer
first_digit = int(number[0])
last_digit = int(number[-1])
#first and last digit are defined and sum is presented
sum_f_l = first_digit + last_digit
print(sum_f_l)
#sum is displayed



#5 Use Python to find all the ways to make Rs. 10
import itertools
#I import itertools to be able to work with iterations and combinations
Rs_amount = [1, 2, 5, 10]
total_Rs = 10
all_possibilities = []

#Create a loop for all combination possibilities between 1 and 10 of given list
for Rs in range(1, total_Rs // min(Rs_amount) + 1):
    # Create a loop with combinations with replacement for the current length
    for combo in itertools.combinations_with_replacement(Rs_amount, Rs):
        if sum(combo) == total_Rs:
            all_possibilities.append(list(combo))

# Print all the possibilities to form Rs 10
for combo in all_possibilities:
    print(combo)



#6 Find the duplicates in three lists
my_list1=[1, 2, 3, 4, 5, 6]
my_list2=[1, 3, 4, 5, 7]
my_list3=[1, 4, 5, 8]

set1 = set(my_list1)
set2 = set(my_list2)
set3 = set(my_list3)

# Find the intersection of all three sets
duplicate_elements = set1.intersection(set2, set3)

print(f"Elements common to all three lists: {duplicate_elements}")
#Duplicate elements are displayed



#7 Find the first non-repeating elements in a given list of integers
#Define a function to find the first non-repeated element in a list
def first_none_repeated_el(list):
    # Create a dictionary 'ctr' to count the occurrences of each element
    occ_el = {}
    # Iterate through the elements in the list
    for i in list:
        # If the element is already in the dictionary, increment its count
        if i in occ_el:
            occ_el[i] += 1
        # If the element is not in the dictionary, add it with a count of 1
        else:
            occ_el[i] = 1
    # Iterate through the elements in the list again
    for i in list:
        # Find the first element with a count of 1 (non-repeated)
        if occ_el[i] == 1:
            return i
    return None
    # If no non-repeated element is found, return None

# Create a list of numbers
nums =  [1, 1, 1, 1, 0, 1, 1, 1]

# Print the original list of numbers
print("Original list:")
print(nums)

# Call the first_non_repeated_el function with the list and store the result in 'result'
result = first_none_repeated_el(nums)

# Print the result, which is the first non-repeated element in the list
print("First none-repeated element in the given list:")
print(result)



#8 Minimum element in a rated and sorted list
my_rs_list = [("a",1), ("b",2), ("c",3), ("d",4), ("e",5) ]
minimum_element = min(my_rs_list)
#define minimum element in a rated and sorted list
print(f"The minimum element is: {minimum_element}")
#Minimum element is displayed



#9 Find triplet in list with sum 59
my_list = [10, 20, 30, 9]
sum_three_elements = 59

n = len(my_list)
#count elements in list
for i in range(n):
    #create loop for 1st element selected
    for j in range(i+1, n):
        #loop for 2nd element selected
        for k in range(j+1, n):
            #loop for 3rd element selected
            if my_list[i] + my_list[j] + my_list[k] == sum_three_elements:
                print("Found three elements:", my_list[i], my_list[j], my_list[k])
                #The found elements are printed



#10 Python program to find if there is a sublist with sum is equal to zero
def find_zero_sum_sublist_simple(numbers):
#define a sublist of which sum of the elements is zero
    for i in range(len(numbers)):
        total = 0
        for j in range(i, len(numbers)):
            total += numbers[j]
            if total == 0:
                return numbers[i:j+1]
    return None
#created a loop to find and return elements of which the sum is zero
my_list = [4,1,-3,2,6]
result = find_zero_sum_sublist_simple(my_list)
#method to print the found sublist which equals to zero
print("Found a sublist with sum equal to zero:", result)
'''



'''
#PAT Task 5
#Exercise1
List_names_ages=[
{'name': 'andres', 'age': 30},
{'name': 'jack', 'age': 12},
{'name': 'agnes', 'age': 17},
{'name': 'cassie', 'age': 13},
{'name': 'john', 'age': 18},
{'name': 'caroline', 'age': 19}
]
#filter out adults of age 18 and older
Adults=list(filter(lambda individual: individual["age"] >= 18 ,List_names_ages))

#Create new list with only adults, above 18
Adults_names=list(map(lambda individual: individual["name"],Adults))
print(Adults_names)



#Exercise2
#import reduce function
from functools import reduce
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# Calculate the product using reduce function and lambda expression
product = reduce(lambda x, y: x * y, numbers)

print(f"The product of all numbers in the list is: {product}")



#Exercise3
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#define even numbers using lambda function
even= lambda x: x % 2 == 0

#filter out even numbers
even_numbers = filter(even, numbers)

#square the even numbers
square = lambda x: x ** 2

#create new list with squared even numbers
squared_numbers = list(map(square, even_numbers))
print(squared_numbers)



#Exercise4
Given_string=input("Enter a string: ")
is_number = lambda s: True if isinstance(s, (int, float)) else (
    (s.replace('.', '', 1).isdigit() and s.count('.') <= 1) or
    (s.startswith('-') and s[1:].replace('.', '', 1).isdigit() and s.count('.') <= 1)
)
print(is_number(Given_string))



#Exercise5
#Import the 'datetime' function
import datetime

#Current date and time using 'datetime.datetime.now()' and store it in variable 'now'
now = datetime.datetime.now()

#Display current date and time stored in 'now'
print(now)

#Use lambda function 'year' to extract the year from a given datetime object 'x'
year = lambda x: x.year

#Use lambda function 'month' to extract the month from a given datetime object 'x'
month = lambda x: x.month

#Use lambda function 'day' to extract the day from a given datetime object 'x'
day = lambda x: x.day

# Print the year extracted from the current datetime object 'now'
print(year(now))

# Print the month extracted from the current datetime object 'now'
print(month(now))

# Print the day extracted from the current datetime object 'now'
print(day(now))


#Exercise6
#import the reduce function
from functools import reduce

#Define Fibonacci series up to n terms
fib_series = lambda n: [] if n <= 0 else [0] if n == 1 else reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
print(fib_series(0))
print(fib_series(1))
print(fib_series(2))
print(fib_series(3))
print(fib_series(4))
print(fib_series(5))
print(fib_series(6))
'''


#Pat task 6
# Problem 1 Bank Account


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.05):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return self.balance

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance=0, minimum_balance=100):
        super().__init__(account_number, balance)
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
         raise ValueError("Minimum balance exceeded")
        self.balance -= amount
        return self.balance




savings=SavingsAccount("Savings", 1000)
interest = savings.balance * savings.interest_rate

current=CurrentAccount("Current", 500, minimum_balance=100)
print("Savings before interest", savings.get_balance())
print("Interest",interest)
print("Savings after interest", savings.add_interest())
print("Current before withdraw", current.get_balance())

try:
    current.withdraw(500)
    print("Withdraw 500 successful")
except ValueError as e:
    print("Withdraw failed:", e)

print("Withdraw", 500)
print("Current after withdraw", current.get_balance())



class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def calculate_salary(self):
        raise NotImplementedError(
            "Subclasses must implement calculate_salary()"
        )

class RegularEmployee(Employee):
    def __init__(self, name, position, monthly_salary):
        super().__init__(name, position)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class ContractEmployee(Employee):
    def __init__(self, name, position, hourly_rate, hours_worked):
        super().__init__(name, position)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class Manager(Employee):
    def __init__(self, name, position, base_salary, bonus):
        super().__init__(name, position)
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus

employees = [
    RegularEmployee("John", "Regular Employee",3000),
    ContractEmployee("Peter", "Contract Employee", 16, 160),
    Manager("Anne", "Manager",5000, 1500)
]

for employee in employees:
    print(f"{employee.name} {employee.position} earns ${employee.calculate_salary():,.2f}")



class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self):
        raise NotImplementedError(
            "Subclasses must implement calculate_rental()"
        )

class Car(Vehicle):
    def __init__(self, model, rental_rate, days_rented):
        super().__init__(model, rental_rate)
        self.days_rented = days_rented

    def calculate_rental(self):
        return self.rental_rate * self.days_rented

class Bike(Vehicle):
    def __init__(self, model, rental_rate, days_rented):
        super().__init__(model, rental_rate)
        self.days_rented = days_rented

    def calculate_rental(self):
        return self.rental_rate * self.days_rented

class Truck(Vehicle):
    def __init__(self, model, rental_rate, days_rented):
        super().__init__(model, rental_rate)
        self.days_rented = days_rented

    def calculate_rental(self):
        return self.rental_rate * self.days_rented

vehicles = [
    Car("car: Mercedes, rented 1 day", 150,1),
    Bike("bike: MTB, rented 1 day", 15, 1),
    Truck("truck: IVECO, rented 2 days", 1500, 2),
]

for vehicle in vehicles:
    print(f"{vehicle.model} {vehicle.rental_rate} costs ${vehicle.calculate_rental():,.2f}")