"""
decorators are functions that take function as an argument and 
it behaviors as function 
"""
import functools as f


def myDec(func):
    @f.wraps(func)
    def Name(*args, **kgwars):
        print('start Working ')
        result = func(*args, **kgwars)
        print('The result is : ')
        return result
    return Name


@myDec
def SayHiSir(x):
    return x**2



print(SayHiSir(10))