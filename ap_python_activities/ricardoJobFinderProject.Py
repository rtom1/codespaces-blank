def techJobApp():
    location = input('where are you from! ')
    name = input('whats your name?')
    picture = input('upload a picture')
    Hours = int(input('How many hours would you like to work'))
    Salary = float(input('How much would you like to make'))
    print('success! We will get back to you.')

def sciJobApp():
    location = input('where are you from! ')
    name = input('whats your name?')
    picture = input('upload a picture')
    Hours = int(input('How many hours would you like to work'))
    Salary = float(input('How much would you like to make'))
    print('success! We will get back to you.')


def mathJobApp():
    location = input('where are you from! ')
    name = input('whats your name?')
    picture = input('upload a picture')
    Hours = int(input('How many hours would you like to work'))
    Salary = float(input('How much would you like to make'))
    print('success! We will get back to you.')

def engJobApp():
    location = input('where are you from! ')
    name = input('whats your name?')
    picture = input('upload a picture')
    Hours = int(input('How many hours would you like to work'))
    Salary = float(input('How much would you like to make'))
    print('success! We will get back to you.')

def jobType():    
    userJob= input('Please select either s for science, t for tech, e for engineering, or m for math: ')
    s = ['Science Teacher','Lab Worker', 'Research Specialist']
    t = ['Coding', 'Networking', 'Cyber Security']
    e = ['Enviromental Engineer','Chemical Engineer','Systems Engineer']
    m = ['Math Teacher','Accountant','Financial Analyst']

    if userJob == "s":
        print(s)
        selectSpec= int(input('please select a  science job, press 0 for science teacher, 1 for lab worker, and 2 for research specialist: '))
        if selectSpec== 0:
            print('you are about to do the '+ s[0] + ' job application.')
            sciJobApp()
        elif selectSpec== 1:
            print('you are about to do the '+ s[1] + ' job application.')
            sciJobApp()
        elif selectSpec== 2:
            print('you are about to do the '+ s[2] + ' job application.')
            sciJobApp()


    elif userJob == "t":
        print(t)
        selectSpec= int(input('please select a tech job, press 0 for coding, 1 for networking, and 2 for cyber security: '))
        if selectSpec== 0:
            print('you are about to do the '+ t[0] + ' job application.')
            techJobApp()
        elif selectSpec == 1:
            print('you are about to do the '+ t[1] + ' job application.')
            techJobApp()
        elif selectSpec== 2:
            print('you are about to do the '+ t[2] + ' job application.')
            techJobApp()

    elif userJob == "e":
        print(e)
        selectSpec= int(input('please select a engineering job, press 0 for enviromental engineer, 1 for chemical engineer, and 2 for systems engineer: '))
        if selectSpec== 0:
            print('you are about to do the '+ e[0] + ' job application.')
            engJobApp()
        elif selectSpec == 1:
            print('you are about to do the '+ e[1] + ' job application.')
            engJobApp()
        elif selectSpec== 2:
            print('you are about to do the '+ e[2] + ' job application.')
            engJobApp()


    elif userJob == "m":
         print(m)
         selectSpec= int(input('please select a math job, press 0 for math teacher, 1 for accountant, and 2 for financial analyst: '))
         if selectSpec== 0:
            print('you are about to do the '+ m[0] + ' job application.')
            mathJobApp()
         elif selectSpec == 1:
            print('you are about to do the '+ m[1] + ' job application.')
            mathJobApp()
         elif selectSpec== 2:
            print('you are about to do the '+ m[2] + ' job application.')
            mathJobApp()

jobType()



