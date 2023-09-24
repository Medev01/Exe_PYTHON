import os
'''
# print(dir(os))
# get  The Current Working Directory
print(os.getcwd())

# CREATE A NEW FOLDER
#os.mkdir('C:\\Users\\Lenovo\\MOHAMED')

# GET SIZe OF FOLDER
print(os.path.getsize('C:\\Users\\Lenovo\\MOHAMED'),' ko')

# list of folders
print(os.listdir('C:\\Users\\Lenovo'))
'''
# create a file
path = 'C:\\Users\\Lenovo\\MOHAMED\\medo_infos.txt'

'''
f = open(path,'w')
f.write('Myname is Mohamed ,i\'m from Morocco ,\ni am 21 yo, I still Studying In the Faculty of Science in Rabat.\nThis is my first year in the Faculty in the IPS\'s Master ')
f.close()'''
med = open(path)
print(os.path.getsize(path))
print(os.path.isfile(path))
med.close()


