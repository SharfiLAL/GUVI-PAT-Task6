#Returning multiple values(class 12 exercises)
#exercise1
'''
def calculation(a,b): #define statement can be named anything, but stick to Python rules
    return a+b,a-b,a*b #return statement is used for manipulation

add,sub,mul=calculation(10,20)
print(add,sub,mul)
'''
#exercise 2

def check(n):
    if n > 0:
        if n % 2 == 0:
         print("This is a positive even number")
        else :
         print("This is an odd number")
    else:
        print("This is not a positive number")
number=int(input("Enter a number to check: "))
check(number)

#exercise3
'''
def welcome_message():
    print("Welcome to Python!")
welcome_message()
'''
'''
def number():
    print("The cube of the number is:")

n = int(input("Enter a number: "))
cube=n*n*n
print(cube)
'''

#exercise4
'''
def school_name():
    print("The name of the school is: Mulo Onverdacht")
    return input()
school_name=school_name()
'''

'''
#exercise5
def area_of_rectangle(a,b):
    print("The area of the rectangle is:", a*b)
    return input()
area_of_rectangle=area_of_rectangle(1,2)
'''

'''
a=int(input("Enter length of a rectangle: "))
b=int(input("Enter width of a rectangle: "))
area_of_rectangle=a*b
print(area_of_rectangle)
'''