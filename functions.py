#functions:
#A functions is a block of organized, reusable code and that is used to perform a single or multiple tasks.
#python gives inbuilt functions like print(), you can make your own function also and these are called user defined functions.
#function blocks begin with the keyword def followed by function name and parenthesis()
'''def calculate(a,b):
    print("sum:",a+b)
    print("diff:",a-b)
    print("product:",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''



'''def calci(a,b):
    print("division:",a//b)
    print("Remainder:",a%b)
    print("power:",a**b)

calci(10,2)'''

'''while True:
    def add():
        a = int(input("enter a value:"))
        b = int(input("enter b value:"))
        print(a+b)
    add()'''

'''def add():
    a = int(input("enter a value:"))
    b = int(input("enter b value:"))
    print(a+b)
    add()
    
add()'''

'''def fullname():
    fname=input()
    lname=input()
    print(fname+" "+lname).title()

fullname()'''


#return vs print
#print just shows the human user output in a console
#return will terminate the function and give back a value from the function
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(d)
cal(10,2)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e
print(cal(10,2))'''



'''def split_bill(bill,members):
    each = bill/members
    print("per head:",each)
    
split_bill(2000,4)'''


'''def split_bill():
    bill = int(input("enter the bill:\n"))
    members = int(input("enter members:\n"))
    each = bill/members
    print(f"per head: {each}")
    
split_bill()'''

'''def split_bill():
    bill = int(input("enter the bill:\n"))
    members = int(input("enter members:\n"))
    each = bill/members
    print("per head:{}".format(each))
    
split_bill()'''

#keywords and positional arguments

'''def Details(id,name,mailid):
    id=10
    name="ravi"
    mailid="ravi@gmail.com"
Details(id="id",name="name",mailid="mailid")'''


'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=10,name="ravi",mailid="ravi@gmail.com")
Details(id=20,name="ben",mailid="ben@gmail.com")
Details(40,"tony","tony@gmail.com")
Details("spiderman","spidy@gmail.com",50)
Details(name="naruto",mailid="naruto@gmail.com",id=60)'''

'''def emp_details(name,salary,dept):
    print(name,salary,dept)
emp_details(name="name",salary="salary",dept="dept")
emp_details(name="ravi",salary=100000,dept="cyber")
emp_details("ben",300000,"science")
emp_details(dept="bio chemistry",salary=200000,name="spidy")'''


'''def emp_details(name,salary,dept):
    name = "ravi"
    salary = 400000
    dept = "cyber"
    print(name,salary,dept)
emp_details(name="name",salary="salary",dept="dept")'''

#default arguments
'''def grocery(item,price):
    print("item is %s" %item)
    print("price is %f" %price)
grocery("sugar",100)'''

'''def grocery(item="ravi",price=1244):
    print("item is %s" %item)
    print("price is %f" %price)
grocery()'''

'''def grocery(item,price=2000):
    print("item is %s" %item)
    print("price is %f" %price)
grocery("candy")'''

'''def grocery(item="rice",price):
    #non default arguments follows default arguments
    print("item is %s" %item)
    print("price is %f" %price)
grocery(500)'''

##def cake_factory(cake,quantity,price):
##    print("cake is %s" %cake)
##    print("quqntity is %d" %quantity)
##    print("price is %f" %price)
##cake_factory("chocoloate",1,200)
##
##def cake_bakery(cake="vanilla",quantity=3,price=600):
##    print("cake is %s" %cake)
##    print("quantity is %d" %item)
##    print("price is %f" %price)
##cake_bakery()
##


#arguments->* is used to unpack the elements
##a=[2,3,4,5,6,7]
##print(a)
##print(*a)
##print(type(a))

'''b = (4,5,6,7,8)
print(b)
print(type(b))'''

'''c = {7,8,9,10,11,12,13}
print(c)
print(*c)'''

'''d = {"name":"ravi","course":"pfs"}
print(d)
print(*d)'''

'''a,b,c=2,3,4,5,6,7,8,9
print(a)
print(b)
print(c)#error'''

'''a,b,*c=2,3,4,5,6,7,8,9
print(a)
print(b)
print(*c)'''

'''a="codegnan"
print(a)
print(*a)'''

'''a,b,c="codegnan"
print(a)
print(b)
print(c)#error'''

'''a,b,*c = "codegnan"
print(a)
print(b)
print(*c)'''



#variable length arguments
#variable length arguments are autmatically stores in tuple and we use *arguments.

def check(*a):
    print(a)
    print(type(a))
check()
b = [4,5,6,7,8]
check(*b)
c = (4,5,6,7,8)
check(*c)
d = {11,23,45,67}
check(*d)
e={"name":"ravi","year":2026}
check(*e)

'''def check1(*a):
    d=2
    print(a)
    print(type(a))
    for i in a:
        if isinstance(i,(int,float)):#type(i) in (int,float)
            d+=i
            print(d)
                      
check1()
check1(2,3,4,5,6,7)
check1(2,3.4,5.6,7.8)
check1(2,3.4,5.6,7.8,"ravi")'''



'''def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def mul(a,b):
    return a*b
    `
a = int(input("enter a value\n"))
b = int(input("enter b value\n"))
choice = int(input(select your operation:
    1.Add
    2.Subtraction
    3.multiplication\n))
if choice==1:
    print("sum is:",add(a,b))
elif choice==2:
    print("diff is:",sub(a,b))
elif choice==3:
    print("multiply is:",mul(a,b))
else:
    print("select valid input")'''



'''def calculate(a,b,choice):
    if choice==1:
        print("sum:",a+b)
    elif choice==2:
        print("diff:",a-b)
    elif choice==3:
        print("mul:",a*b)

a = int(input("enter a value"))
b=int(input("enter b vlue"))
choice = int(input(select your operation:
    1.Add
    2.Subtraction
    3.multiplication\n))
calculate(a,b,choice)'''



#**(kwargs)
'''def details(**a):
    print(a)
    print(type(a))
details()
d = {"id":[10,20,30],"name":["ravi","ben","spidy"],"status":["p","a","p"]}
details(**d)'''

'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d = {"id":[10,20,30],"name":["ravi","ben","spidy"],"status":["p","a","p"]}
details(**d)'''


'''def ravi(*a,**b):
    d=2
    print(a)
    print(b)
    for i in a:
        d+=i
    print(d)
    for i,j in b.items():
        print(i,j)
d=[1,2,3,4]
e={"name":["ravi","ben","spidy"],"dept":["cs","ps","bio"]}
ravi(*d,**e)'''


'''def r(*a,**b):
    print(a)
    print(b)
r(1,2,3,4,name="ravi",course="python")'''



###max,min,sum
##print(max(1,2,3,4,5,6,7))
##print(min(1,2,3,4,5,6,7))
##a=[4,5,6,7,8]
##print(sum(a))
##








    



























































































































































