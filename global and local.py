#global and local variables
#a variable inside and outside function is called global and local variables
#a variabe is defined above the function and is accessible to the entire global space and is called global variable
#a variable is defined inside the function is called local value

#first case of global variable
'''a=5
def check1():
    print("Inside value is:",a)
check1()
print(a)'''

#second case of global variable
'''a=2
def check2():
    a=5
    a=a**2
    print(a)
check2()
print(a)'''


#third case of both glibal and local variables
'''a=2
def check3():
    a=7
    print(a)
    a=10
    print(a)
    b=12
    b=b+a
    print(a)
check3()
print(a)
print(b)'''


#usage of global keyword
#when a user wants to create a variable isode the funcion directly and carry forward the updated value outside the function then we need to use global keyword

'''a=3
def final():
    global a
    print("inside a value:",a)
    a=6
    print("upadted a value:",a)
    #global b
    b=13
    b=b+a
    print("b value is:",b)
final()
print(a)
print(b)'''


#genertors
#no tuple comprehension in above cases if we remove those braces and keep parenthesis then the outcome is generators
#a=[expr for var in collections/range]
'''a=[i for i in range(16)]
print(a)
print(type(a))'''

'''b=(i for i in range(16))
print(b)
print(*b)
print(type(b))
print(list(b))
print(tuple(b))
print(set(b))'''

#generator
#a generator is also a function which can be used as an iterator(loop) by producing group of values and where we can use yield keyword

#yield vs return
#return will terminate the function where as yield can pause the function and go on with every successive iteration 

'''a,b=[int(x) for x in input("enter the values:").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''

'''a,b=[int(x) for x in input("enter the values:").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        #return a
    return a
print(check(a,b))'''

'''def mygen():
    return "python"
    return "dsa"
    return "java"
    return "python","dsa","java"
print(*mygen())'''

'''def mygen():
    yield "python"
    yield "java"
    yield "dsa"
print(*mygen())

#next()
a = mygen()
print(next(a))
print(next(a))
print(next(a))'''






    

