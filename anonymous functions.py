#Anonymous Functions
#Anonymous Functions are nameless functions and we use a keyword called as Lambda to create anonymous functions
'''def f(x):
    print(2*x+5)
f(5)'''

'''def f():
    x=int(input("enter x value:"))
    print(2*x+5)
f()'''

#syntax
#a=lambda arg:expr

'''a=lambda x:2*x+5
print(a(5))'''


'''a=int(input("enter a value:"))
b=lambda x:2*x+5
print(b(a))'''


'''a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=lambda a,b:a*b
print(c(a,b))'''

'''a="python"
b=lambda a:a.upper()
print(b(a))'''

'''a="hello world"
b=lambda a:a.title()
print(b(a))'''

'''fname=input("enter fname:")
lname=input("enter lname:")
full=lambda a,b:a+b
print(full(fname,lname))'''

'''a,b=[x for x in input("enter the values:").split(",")]
full=lambda a,b:a+" "+b
print(full(a,b))'''


'''a,b=map(str,input("enter values separted by space:").split())
full=lambda a,b:a+b
print(full(a,b))'''


#filter()
'''a=[1,2,3,4,5,6]
if a%2==0:
    print(a)#error
for i in a:
    if a%2==0:
        print(a)'''


'''a=[1,2,3,4,5,6]
b=list(filter(lambda x:x%2==0,a))
print(b)'''

'''a=[[],(),{},set(),"",None,3,4.5,"python",4+6j]
b=list(filter(None,a))
print(b)'''

#map()-->  each object from a collection and forms
#a new collection
a=[2,3,5,7,9,12,19]
b=[1,4,6,15,20,35,40]
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)







