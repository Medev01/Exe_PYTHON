"""
f=open("exemple01.txt","w")

f.write(str(20))
f.close()
"""
"""
f=open("exemple01.txt","r")
x=f.read()
print(x)
f.close()
"""
from pickle import *
"""
f=open("exemple02.txt","wb")
dump(20,f)
f.close()
"""
"""
f=open("exemple02.txt","rb")
x=load(f)
print(x)
f.close()
"""




