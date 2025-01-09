#data types in python
num1 = 3
num2 = 3.4
name = "Prem"
is_student = True
print(num1, num2, name, is_student)
print(type(num1),type(num2),type(name),type(is_student))

# define temperature 
temp = 98.23
is_hot = True
print(type(temp), type(is_hot))

#output
#3 3.4 Prem True
# <class 'int'> <class 'float'> <class 'str'> <class 'bool'>

# ask the user for their name and age and print the output 
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print("Hello", user_name, "you are", user_age, "years old !")