# assignements practices
# Practice Exercises:
# Write a program that checks if a number is positive, negative, or zero.
# Create a program that determines the largest of three numbers input by the user.
# Develop a simple calculator that performs addition, subtraction, multiplication, or division based on user input.

# Solution:
# 1. Write a program that checks if a number is positive, negative, or zero.
number = int(input("Enter a number:"))
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

 # Create a program that determines the largest of three numbers input by the user.
num1 =int(input("Enter the first Number: "))
num2 =int(input("Enter the second Number: "))
num3 =int(input("Enter the third Number: "))
if num1 > num2 and num1 > num3:
        print(f"{num1} is the largest number")
elif num2 > num1 and num2 > num3:
        print(f"{num2} is the largest number")
else:
        print(f"{num3} is the largest number")

# Develop a simple calculator that performs addition, subtraction, multiplication, or division based on user input.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation you want to perform: ")
if operation == "+":
    print(f"The sum of the two numbers is {num1 + num2}")
elif operation == "-":
    print(f"The difference of the two numbers is {num1 - num2}")
elif operation == "*":
    print(f"The product of the two numbers is {num1 * num2}")
elif operation == "/":
    print(f"The division of the two numbers is {num1 / num2}")
else:
     
    print("Invalid operation")
# End of the code22
#find the smallest number
num1 =int(input("Enter the first Number: "))
num2 =int(input("Enter the second Number: "))
num3 =int(input("Enter the third Number: "))
if num1 <num2 and num1 <num3:
    print(f"{num1} is the smallest number")
elif num2 <num1 and num2 <num3:
    print(f"{num2} is the smallest number")
else:
    print(f"{num3} is the smallest number") 