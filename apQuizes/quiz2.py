# PYTHON QUIZ # 2

# This is an open book test. You may use the internet to assist with your answers- NO PHONES ALLOWED!
# You will have the entire class time to complete your quiz. It must be submitted before class is over to recieve a grade.
# Take your time, read the questions thoroughly, find context clues and keywords to help you. 

# GOOD LUCK!
#-----------------------------------------------------------------------------------------------------------#

# 1. Create a function that will multiply two (2) values that are passed into the function as arguments. 
# Your function should print out the result of the two numbers that have been multiplied.

# 2. Creat a function that will do the following calculation. Your function should take in three argument. it should add the first
# two arguments and then the sum of the first two (2) should be divided by the third argument. 
# You function should then print the result. 


# 3. Create a elevator function that will run specific lines of code based on the conditions provided by a user. If the user types in 101,
# the function should print out they are going to the boys latin office, if they type in 203, they are going to the gym, 
# and if they type in the letter g, the lobby. else, if the input doesnt match any of the values provided, tell the user that floor doesn't exist and to please
# enter a valid floor number.

# hint you will need to look into using conditional statements

def location(user_destination):
 user_destination == input('Where are you going')




# 4. Write a simple conditional statement that uses a boolean that will print if it is daytime or nighttime.
 
def time_of_day(day):
  if day == 'true':
   print('It is day time')
  else:
   print('It is night time')

time_of_day()

# 5. What function would you use if you wanted to add and element/ value to a list data type? Explain why you would use it.
'I would use append method.It adds anything you want to the end of any list'
# 6. Do some research and find the correct built-in python function that will reverse the order of the following list.
# then print your list in the reverse order.

random_number_list = [0,1,2,3,4,5,6,7,8]

random_number_list.reverse()
print(random_number_list)
# 7.Do some research and find the correcrt built-in python function that will allow you to find the largest number in the following list.
# then print the largest number
ranom_number_list2 = [100,230,40,39403,19]
a = (100,230,40,39403,19)
x = max(a)
print(x)
# 8. A security company has hired you as an engineer to help them develop a program that will only let users into the building 
# if they enter a specific password. They given you the following information to use to build this program.
# - they want users to be able to enter a series of codes to get access
# - they want the user to enter an initial password value which is 0001
# - if they get this correct, they then want them to enter another value, which is 3039
# - if this is correct they will get access to the building
# - if they have the wrong answer in either scenario they will get a message saying access denied. 

def building_code(user_code):
 user_code == input('code') 
 if user_code == '0001':
  print('You have to enter one more code')
 elif 'user_code' == '3039':
  print('You may enter')
 else:
  print('You may not enter')

#building_code()

# 9. What does it mean to call a function? Why do we call functions. 
# you can use the variable below to enter you ansewer. 

answer9= 'We are basically telling the program to execute the function. If we dont call it then it won't run'

# 10. Find and print each value at the specific indexes provided in the list.
# find and print the values/words at index 3, 4, and 6 

shopping_cart = ['apples','water','chicken','ice cream','ground beef','string beans','oranges']
 
print(shopping_cart[3])
print(shopping_cart[4])
print(shopping_cart[6])