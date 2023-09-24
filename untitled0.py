# define the function
 
def fun(x):
    return x**2 - 0.5*x
def dfun(x):
    return 2*x - 0.5
def d2fun(x):
    return 2

def newton1(dfun, d2fun,x_0=0, e=0.001, max_iter =100 ):
     x_n = x_0
     for n in range(0, max_iter):
         df_xn = d2fun(x_n)
         if abs(df_xn) < e:
             print("found solution after",n,"iteration")
             return  x_n
         d2f_xn = d2fun(x_n)
         if d2f_xn == 0 :
             print("zero derivative , no solution ")
             return None
         x_n = x_n -  df_xn/ d2f_xn
         
         print("No solution found")
     return None 
 
newton1(dfun, d2fun, x_0=0, e=0.001, max_iter =100 )
