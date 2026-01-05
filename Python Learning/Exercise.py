#Exercise0
#Name = "Zulfikhar"
#City = "Para"

#Exercise
#Mark1 = 189
#Mark2 = 189
#Mark3 = 123
#Total = Mark1 + Mark2 + Mark3
#Average = Total/3


#print("Total is " , Total)
#print("Average is " , Average)
#print("My favourite sport,Soccer")
#print("My favourite player, Messi" )
#print("My favourite actor, Gerard Butler")

#Exercise1
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))

#total = num2-num1
#print("The sub is" , total)

'''
Exercise2
billing calculator


print("------BILL-------")
item = input("Enter the item name : ")
price = float(input("Enter the price of the item : "))
quantity = int(input("Enter the quantity : "))

total = price * quantity
gst = price * 0.5 #gst = goods and service tax

print("item" , item)
print("Price" , price)
print("Quantity" , quantity)
print("Total" , total)
print("GST" , gst)
'''


'''
Rules for variable names
1. Must start with a letter or underscore
    name, _count - allowed
    1name - not allowed
2. Can contain only letters (A-Z)(a-z), number and underscore
   student1, total_amount allowed
   student name, not allowed because of space
3. Case Sensitive (CAPS vs small)
   age and Age and AGE are completely different variables
4. No keywords are allowed
   value, class_number - allowed
   class, for , while - not allowed
5. Name should be meaningful
   item, price and quantity
   x, y, z >

variableName=
            

Reserved words
True, False, None
and, or, not
if, else elif
try, except, finally
while, import, from
'''

'''
Exercise
1.Take two numbers from user and print their
   Sum
   Product
   Difference
   Division
2.Convert Celsius to Fahrenheit
   Convert temperature from Celsius to Fahrenheit '
   Formula : °F = °C * 1.8 + 32.
3.Area of a circle :
   Formula = pi * r square
   pi = 3.14

'''

'''exercise
#user has two numbers
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

sum = num1 + num2
product = num1 * num2
difference = num1 - num2
division = num1 / num2

print(sum, product, difference, division)
'''

'''exercise of temperature conversion from celsius to fahrenheit
Temp1 = float(input("Enter the temperature : "))
Temp2 = Temp1*1.8+32


print(Temp2)
'''

'''exercise of how to add string and calculation in code
r = float(input("Enter the circle radius : "))
pi = 3.14
Circle_area = pi * r ** 2

print("Area of the circle =" , Circle_area)
'''

'''
#example
x=10
x='Welcome Python'

print(x)
'''

'''example => data types will be printed when running code
x=str(10)
y=100

print(type(x))
print(type(y))
'''

'''example of how Python prints various outputs
x,y,z= 10,"Zulfikhar",5.1

print(x,y,z)
'''


#example of indentation and how it influences the code
#the section print("5 is greater") is part of the first block of code
# print("Hello") is another piece
'''
a=int(input("Enter the value a"))
if (a>5):
    print("5 is greater")

print("Hello")
'''

#example, if num is greater than 5, all 3 strings will be printed
# if not, only last string will be printed
'''
num=6

if (num>5):
    print("Number is Big")
    print("Inside the if block")
print("Outside the if block")
'''

#example of conditions
'''
age = int(input("Enter the age : "))
if age >= 18:
    print("Eligible to vote")
else: print("Not eligible to vote")
'''

#example of if + ELIF + else
'''
mark1 = 100
mark2 = 89
mark3 = 90

total = mark1 + mark2 + mark3

if total > 250:
    print("Grade A")
elif total >= 250:
    print("Grade B")
else:
    print("Grade C")


password = input("Enter the password : ")
if password == "python123"
    print("Login successful")
else:
    print("Incorrect password")
'''


'''
Perform these exercises with if elif else function
1. Largest of two numbers
2. Largest of three numbers
3. Even or odd
'''

'''
largest of two numbers and largest of three numbers
num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))
#num3 = float(input("Enter the third number : "))
if num1 > num2:
    print("num1 is largest")
elif num2 > num3:
    print("num2 is largest")
else:
    print("num3 is largest")
'''

"odd or even"
'''
num1 = int(input("Enter the number : "))

if (num1%2==0):
    print("num1 is even")
else:
    print("num1 is odd")
'''

'''
Loops, there are 2: for loops and while loops"
example
for i in range (5):
    print("Hello")
    
for = Start a loop
i = a variable that changes each time (Loop counter)
in range (5) -- repeat it 5 times (0,1,2,3,4)
: = End of condition line
print("Hello") = the actionable statement to repeat during execution
'''

'''
example
for i in range (5):
    print("Hello")
'''

'''
#exercise Mentor: Print only the even numbers from 1 to 50
for i in range (1,50):
  if (i % 2 == 0):
    print(i)
'''

'''
#exercise Mentor: print table of 36
num = int(input("Enter the number : "))

for i in range(1,11):
    print(num, "X", i, "=", num*i)
'''


'''example of the while loop
count=5

while count > 0:
    print("Count =", count)
    count=count-1
'''

'''
#example of while loop with password request

password = ""
while password!= "python123":
    password=input("Enter the correct password : ")
print ("Access granted!!")
'''

'''
#exercise from mentor (I need to correct it)
#1. print numbers from 1 to N
number = 1
while number >= 1:
    print("Number =", number)
    number=number+1
'''

'''
#2. Keep asking user for numbers stop only when user enters 0

number = 20
while number != 0:
     number=int(input("Enter the correct number : "))
print("Correct number!!")
'''

#Mini Project that has while loop and if statements

# ATM Transactions

'''
balance = 5000

while True:
   print("\n ---- ATM MENU ----")
   print("1.Check Balance ")
   print("2. Deposit Money ")
   print("3. Withdraw Money ")
   print("4. EXIT")


   choice = int(input("Select an option : "))


   if choice == 1 :
       print("Balance :",balance)


   elif choice ==2 :
       amount = float(input("Enter the amount to deposit:"))
       balance = balance+amount
       print("Deposited Successfully")
   elif choice == 3 :
       amount = float(input("Enter the amount to withdraw:"))
       if amount < balance:
           balance = balance - amount
           print("Withdraw Successful")
       else:
           print("in sufficient balance ")
   elif choice ==4:
       print("Thank You !!")
       break
   else:
       print("Invalid option Try again")
'''

"PAT task3"
'''
import random
x = random.randint(1, 10)
Guess = int(input("Guess the number : "))
while x != Guess:
 if Guess > x:
  print("Too High")
  print("Guess again")
  Guess = int(input("Guess the number : "))
 elif Guess < x:
  print("Too Low")
  print("Guess again")
  Guess = int(input("Guess the number : "))
 else: Guess = x
print("Correct guess")
'''
'''
"Unscramble the word"
words=['python', 'javascript', 'java', 'automation', 'pytest','guvi', 'selenium']
'''