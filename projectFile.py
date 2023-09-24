# create a file
path = 'C:\\Users\\Lenovo\\MOHAMED\\MadLibs.txt'
File = open(path, 'a')
cond = True

while cond:
    print('Hi dear we have here some questions Just for know more about You ')
    answer = input('Can u answer them (yes/No): ').lower()
    full_name = input('enter Your Full name ? ')
    phone = input('what is your phone ? ')
    age = input('How old are you ? ')
    favourite_food = input('What is your favourite food ?')
    Hobbies = input('what is Your favourite Hobbies ? ')
    if answer == 'no':
        break
    else:
        File.write(
            f'Full name : {full_name}\nPhone : {phone}\nage : {age}\nfavourite food is : {favourite_food}\nHobbies are:{Hobbies}.\n')
        if File != ' ':
            print('Done!! Have a nice day ')
        else:
            print('opps there is an error ')


File.close()

