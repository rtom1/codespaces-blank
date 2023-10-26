# 1. In your own words, describe what a for loop is?
used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# 2. What is the difference between a FOR loop and a WHILE loop?
# Provide two (2) examples of each. 
for loop is used when the number of iterations is known, whereas execution is done in a while loop until the statement in the program is proved wrong.

i=0
while i<9:
    print(i)
    i+=1



# 3. Create a FOR loop that will go through a list of names 
# and print all the names that start with the letter "R".

names=['Michael','Rebecca','William','Kareem','Robert','Rose','Jason']
for letter in names:
    if letter[0]=='R':
        print(letter)