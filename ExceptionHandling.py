'''
#Syntax error example, bracket not closed
print("hello"

'''


'''
#Runtime Errors > Exceptions

#Exception: is an unexpected event that stops the program execution

print(10/0)

print("Welcome")
print("Awsome Learning")
'''


'''
#Example


print(10/2)

print("Welcome")
print("Awsome Learning")

#instead of 123 input is abs, python crashes
#num = int("123")
num = int("abc")

print(num-23)
'''

'''
Examples of errors (real world)

Code is expecting a number > (user input)  Hello > Error (Python crashes)

A file > File is missing > FileNotFoundError

hit website > Internet is down > Connection error

Divide by zero > Number div by zero > error

'''


'''
#Blocks
#Try....except blok

try:
    print(10/0)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!!")

print("Welcome")
print("Awsome Learning")


try:
    number = int("abc")
except ValueError:
    print("This is not a valid number")
print("Code continues")


try:
    num = int(input("Enter the number:"))
    result=10/num

except ValueError:
    print("Enter a number only!!")

except ZeroDivisionError:
    print("Cannot divide by zero!!")
'''

#finally block : example

try:
    f = open("data.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Cleaning up")
