# 1. In your own words, describe what a function is
Bundled re-usable piece of code instructions 
# 2. What is are function parameters and arguments and describe
# the difference between the 2.
A parameter is a variable in a function definition. It is a placeholder and hence does not have a concrete value. 
An argument is a value passed during function invocation. 
# 3. write a function that will print out a welcome message
# that includes a users name. You will need to use parameters and arguments
user_name = input("Enter your name:-")
print("Welcome to school,",user_name,"\b!")
# 4. Write a function that will do a calculation that takes 3 parameters.
# Your function can do any of the arithmatic operators (add, subtract, multiply, divide)
def addition():
if string == "+":
    a = num1 + num2
    print("addition was performed on the two numbers ", num1, ' and ', num2)
    return a

def subtraction():
if string == "-":
    s = num1 - num2
    print("subtraction was performed on the two numbers ", num1, ' and ', num2)
    return s

def multiplication():
if string == "*":
    t = num1 * num2
    print("multiplication was performed on the two numbers ", num1, ' and ', num2)
    return t

def division():
if string == "/":
    d = num1 / num2
    print("division was performed on the two numbers ", num1, ' and ', num2)
    return d

# 5. Write a function that will output a message to a user, telling them
# what class they have next after this one. this code should use a 
# variable to pass a value into the parameter of a function. The variable should
# be real, user data- not hard coded data.