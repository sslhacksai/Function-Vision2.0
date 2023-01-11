from init_function import *
def lcm(a,b):
    return a*b/gcd(a,b)
def sum(*a):
    res=0
    for i in a:
        res+=i
    return res
def prod(*a):
    res=1
    for i in a:
        res*=i
    return res

#  求函数function在x的导数值
def dy_dx(function,x):
    function0=function.replace("x",str(x))
    dx = 0.0000000001
    function1=function.replace("x",str(x+dx))
    return (eval(function1)-eval(function0))/dx

if __name__=='__main__':
    strr="hellow world"
    print(strr.insert(1,str(1)))
    print(dy_dx(pi,"sin(x)"))
