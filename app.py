from pprint import *

Students = {}
Subjects = {}
Notes = {}


def addStudent(num, fname, lname, cne):
    if num in Students.keys():
        return "This Student Already exist "
    else:
        Students[num] = [fname, lname, cne]
    return Students


def studSubjects(cne, subNames, Class):
    if cne in Subjects:
        return 'Sorry this ID is taken'
    else:
        Subjects[cne] = [[subNames], Class]
    return Subjects


def studNotes(full_name, notes):
    if full_name in Notes:
        return 'Sorry choose an other name, this name is Taken'
    else:
        Notes[full_name] = [notes]
    return Notes


def CalculAVG(notes):
    s, moy = 0, 0
    size = len(notes)
    for note in notes:
        s += note

    moy = s / size
    return moy


def StrToList(str1):
    words = str1.split(' ')
    return words


# simple test
# print(StrToList('hello guys how are u doing'))


def appManagementStudent():
    print('''
          Hi dears Students Please Follow
          our Steps To enter Your Information ...
          and Get all Your Results okay Have a nice day\n 
          ''')

    while True:
        print('please Now enter Your  first name ,last name, your num in the list and CNE: ')
        fname = input('First name: ')
        lname = input('last name: ')
        num = int(input('Your Num in the list : '))
        cne = input('Your cne: ')
        Class = input('enter Your class: ')
        Subects = input('enter all Subjects that you studied separated by (espace): ')
        notes = input('Please enter your Notes separated by (,) : ')
        full_name = fname + ' ' + lname
        results = list(map(lambda x: float(x), notes.split(',')))
        # now add students
        if fname == '':
            break
        if not addStudent(num, fname, lname, cne):
            print('ops Something off !! ')
        else:
            if studSubjects(cne, Subects.split(' '), Class):
                if studNotes(full_name, results):
                    print('Your infos Stored Done ')
                else:
                    print('maybe Your Note aren\'t complete')
            else:
                print('ops there is an error !! ')
                break

    print('''
          To see your infos enter: infos
          To see Your avg enter :avg
          (press blanc to quit):
                ''')
    see = input().upper()

    if see == ' ':
        pass
    elif see == 'INFOS':
        pprint(Students)
    elif see == 'AVG':
        print(CalculAVG(results))


appManagementStudent()
