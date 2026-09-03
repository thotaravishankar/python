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


#cake,price,quantity


    


    








    



























































































































































