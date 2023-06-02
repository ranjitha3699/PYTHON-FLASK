
"""                              #DECORATOR


                        Decorators are a very powerful and useful tool in Python since
                        it allows programmers to modify the behaviour of a function or class.
                        Decorators allow us to wrap another function in order to extend the
                        behaviour of the wrapped function, without permanently modifying it."""
                       







##def sins(t):
##    return t.upper()
## 
##print(sins('Hello'))                  #------------>storing the fun in a object
## 
##y = sins
##g=y
## 
##print(y('check'))
##print(g('open'))

##
##def adder(x,y):
##    def sub():
##        return x+y         #-------->return fun to anoter fun
## 
##    return sub
## 
###a= adder(15)
## 
##print(adder(15,10)())




##def shout(a):
##    return a.upper()
## 
##def sper(b,a,c):              #------>passing the fun as arg
##    return b.lower(),a.upper(),c
## 
##def greet(f):
##    #s=f('HI','hello','well')
##    d=f('python')
##    print (d)
## 
##
###greet(sper)
##greet(shout)


                             #MAIN CONCEPT

'''


@ first
    def hello():
        print("Gfg")

     "Above code is equivalent to -"       #creat a obj(newdec) to store the function same values are asind both 

    def insertdecorator():
        print("Gfg")
    
    insertdecorator = first(insertdecorator)


##
##def hi(func):
##     def inner1():
##        print("Hello, this is before function execution")
##        func()
## 
##        print("This is after function execution")
##         
##    return inner1
## 
##def function():
##    print("This is inside the function !!")
##function = hi(funtion)
##function() 



#1.Basic decorator without arguments?

def dec(func):
    def wrapper():
        print("PYTHON")
        func()
        print("After JAVA")
    return wrapper

@dec
def hello():
    print("Hello")

hello()


##2)Decorator with arguments?
def dec(a,b):
    def tells(s):
        def wrapper(*c,**d):
            print(f"Decorator arguments: {a}, {b}")
            s(*c,**d)
        return wrapper
    return tells

@dec("raffi", "tamil")
def greet(name):
    print(f"Hello, {name}")

greet("deecorator")
##
##




##def out(s,t,u):
##    def inn(a):
##        def nest(*b):
##            d='ranjitha'
##            print('hi'+s+u)
##            print('hellow',b,t)
##            a(d)
##                
##            
##        return nest
##    return inn
##@out('ran','san','vin')
##def helps(d):
##    print('well')
##    print('my nameis'+d)
##helps('connr',5)
##
##'''



'''def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))'''


##def greet(func):
##    print("hello")
##    def hey():
##        func()
##        print("bye")
##    return hey
##    
##
##
##
##
##@greet
##def fine():
##    print('welcome')
##fine()


##single decorator with argument

##def upperstr(str):
##    def myfunc(ref):
##        def process():
##            data = ref()
##            print(data.upper())
##            return str.upper()
##        return process
##    return myfunc
##
##@upperstr("welcome to the string in python")
##def myfunc2():
##    return "hello world"
##
##print(myfunc2())


##def upperstr(ref):
####    def myfunc(ref):
##        def process():
##            data = ref()
##            print(data.upper())
####            return str.upper()
##        return process
####    return myfunc
##
##@upperstr
##def myfunc2():
##    return "hello world"
##
####print(myfunc2())'''

'''# DOUBLE DECORATOR


def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner
 
def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner
 
@decor1
@decor
def num():
    return 10
 
@decor
@decor1
def num2():
    return 10
   
print(num())
print(num2())'''






            













