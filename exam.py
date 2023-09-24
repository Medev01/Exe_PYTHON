# ex 1

def lire():
    nbr_facteur = int(input('enter the number of facteur: '))
    client_name = input('Client\'s name: ')
    prix_hors_tax = float(input('Enter the prix hors tax: '))
    limit_yr = int(input('enter limit year: '))
    facteur = [nbr_facteur,client_name,prix_hors_tax,limit_yr]
    return facteur

Facteurs = []   
def lire_tous(n):
    cnt = 0 
    while True:
        facteur = lire()
        Facteurs.append(facteur)
        cnt += 1
        if cnt == n:
            break

    return Facteurs

# print(lire_tous(3))

#

def sort_facteurs(facteurs):
    size = len(facteurs)

    for i in range(size):
        for j in range(0,size-i-1):
            if facteurs[i][1] > facteurs[j+1][1]:
                facteurs[j][1],facteurs[j+1][1] = facteurs[j+1][1],facteurs[j][1]



ar = [[1, 'ahmed naciri ', 345.0, 2019], [2, 'elghomary ', 378.0, 2020], [3, 'soukaina ', 456.0, 2024]]
sort_facteurs(ar)
# print(ar)


def recherch_dichotomique(nom):
    for item in Facteurs:
        if nom in item: # == if nom == item[1]
            return item
        else:
            return None
    return -1

def maj_factures(facteurs):
    for item in facteurs:
        x=2020-item[3]
        if x>=1:
            while x!=0:
                x=x-1
                item[2]+=item[2]*0.1
    return facteurs

# facteurs(ar)
# print(ar)

def sauvgarder(facteurs, file_name):
    f = open(file_name, 'w')
    for item in facteurs:
        f.write(f'la facteur numero :{item[0]}\nnome de client: {item[1]}\nle prix hors tax : {item[2]}\nannee limite :{item[3]}\n\n')

    if f :
        print('it\'s done !!')
    f.close()

# sauvgarder(ar,'facteurs.txt')

def read_facteurs(file_name):
    f = open(file_name, 'r')
    for line in f.readlines():
        print(line)

    f.close()


read_facteurs('facteurs.txt')

        
# print('   fackerrrrrrrr   '.lstrip())   

def Test():
    prompt ='''
    Hi there pls would you tell me what do u want to do : 
    
    1) - create a list of facteurs 
    2) - show all facteurs 
    3) - 
    '''
    if prompt == '1' :
       pass



# ex 2
def Hamming(mot1,mot2):
    cnt = 0
    if len(mot1) == len(mot2):
        for i in range(len(mot1)):
            if mot1[i] != mot2[i]:
                cnt += 1
    print(f'la distance de hamming enter les deux mots est: {cnt}')

Hamming('shut','shit')

def LanguageHammingDistance(list1):
    for element in range(len(list1)):
        Hamming(list1[element],list1[element+1])
        



import sqlite3 

conn = sqlite3.connect('path...')
cur = conn.cursor()


query = 'SELECT * FROM testfin'
cur.execute(query)
rows = cur.fetchall()
# cur.fetchmany(6)
# cur.fetchone()

for row in rows:
    print(row)














