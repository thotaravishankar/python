#oops syntax
'''class classname():
    #attributes
    name="ravi"
    place="kkd"
    age=21
    def fname(method_name):
        print("statementss.......")
a=classname()
a.fname()'''


###class declaration
##class Details():
##    name="ravi"
##    age=21
##    place="kkd"
##    def display(self):
##        print(self.name,self.age,self.place)
##a=Details()
##print(dir(a))
##a.display()

'''class Employee():
    id=10
    name="ravi"
    mailid="ravi@gmail.com"
    salary=100000000000
    designation="soc"

    def emp_details(self):
        print(f"{self.id}\n{self.name}\n{self.mailid}\n{self.salary}\n{self.designation}")
e=Employee()
e.emp_details()'''

#object-instatiation
'''class Details:
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("ravi",21,"vjy")
a.display()
b=Details()
b.data("ravi",22,"kkd")
b.display()'''

'''class Details:
    #creating constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("ravi",21,"kkd")
print(dir(a))
a.display()'''



'''class Details:
    #creating constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)

a=Details(input("enter name"),int(input("enter age")),input("place"))

print(dir(a))
a.display()'''



'''class Details:
    #creating constructor
    def __init__(self):
        self.name=input("name")
        self.age=int(input("enter age"))
        self.place=input("place")
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''

#diff b/w _ and __
#when user wants to create a variable with double leading unedrscore __ our python interpreter treats it as special variable to avoid name confilcts with methods and inner classes

'''class Employee1:
    def __init__(self):
        self.name="ravi"
        self.mail="ravi@gmail.com"
        self.__salary=10000000#private
class Employee2:
    def __init__(self):
        self.name="spidy"
        self.mail="spidy@gmail.com"
        self.__salary=20000000#private
a=Employee1()
print(a.name)
print(a.mail)
print(a._Employee1__salary)
b=Employee2()
print(b.name)
print(b.mail)
print(b._Employee2__salary)'''


#polymorphism
#operator overloading
'''a=2;b=3
print(a+b)
print(a.__add__(b))
print(a.__sub__(b))
print(a.__mul__(b))
#print(a.__div__(b))
print(a.__pow__(b))
print(a.__ge__(b))
print(a.__le__(b))

a=[1,2,3,4,5,6];b=[3,4,57,8,9]
print(a+b)
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(2))
a="spider";b="man"
print(a.__add__(b))
print("eren".__add__("yeager"))
c="naruto";d="uzumaki"
print(c.__add__(" "+d).title())'''

#operator overriding
'''class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B:
    def __init__(self,b):
        self.b=b
x=A(10)
y=B(20)
print(x+y)'''


#method overloading
'''class new:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is:",a+b+c)
        elif a!=None and b!=None:
            print("the product is:",a*b)
        else:
            print("program ends")
x=new()
x.sum()
x.sum(2,4)
x.sum(2,4,6)'''

'''class new:
    def sum(self,a=4,b=5,c=6):
        if a!=3 and b!=7 and c!=2:
            print("the sum is:",a+b+c)
        elif a!=5 and b!=4:
            print("the product is:",a*b)
        else:
            print("program ends")
x=new()
x.sum()
x.sum(2,4)
x.sum(2,4,6)'''


#method overriding
'''class Animal:
    def speak(self):
        print("animals can make sounds")
class dog:
    def speak(self):
        print("dog can bark")
a=Animal()
b=dog()
a.speak()
b.speak()'''

'''class car:
    def vehicle(self):
        print("BMW")
class bike:
    def vehicle(self):
        print("RE")
a=car()
b=bike()
a.vehicle()
b.vehicle()'''

#Inheritance
#single-inheritance
'''class RBI:#parent-class
    cash=100000
    def available_cash(self):
        print("available_cash is:",self.cash)
        #print("available_cash is:",RBI.cash)
class SBI(RBI):#child-1
    pass
class HDFC(RBI):#child-2
    cash=50000
    def new_cash(self):
        print("new_cash is:",self.cash+self.cash)
        print("new_cash is:",self.cash+self.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''


#multiple-inheritance
'''class Father:
    height=5.5
    def ht(self):
        print("height:",self.height)
class Mother:
    weight=70
    def wt(self):
        print("weight:",self.weight)
class Kid(Father,Mother):
    dob="30-12-2004"
    def dt(self):
        print("date of birth:",self.dob)
k=Kid()
k.ht()
k.wt()
k.dt()'''



#multi-level
'''class GrandParent:
    def land(self):
        print("2 acres of land")
class Parent(GrandParent):
    def house(self):
        print("100 sqft of land")
class Child(Parent):
    def bike(self):
        print("4L worth BMW Bike")
c=Child()
c.land()
c.house()
c.bike()'''


#hierarchical inheritance is where one parent class is inherited by multiple child classes
'''class Employee:
    def com(self):
        print("company name : Codegnan")
class trainer(Employee):
    def teach(self):
        print("Teach: python")
class student(Employee):
    def learn(self):
        print("learning: pfs")

t=trainer()
t.com()
t.teach()

s=student()
s.com()
s.learn()'''

#hybrid-inheritance-->Hybrid inheritance is a combination of two or more types of inheritance in a single program.
#For example, we can combine multilevel inheritance and multiple inheritance.
'''class Employee:
    def compny(self):
        print("codegnan it solutions")
class trainer(Employee):
    def teach(self):
        print("teaches the code")
class student(Employee):
    def study(self):
        print("prepare fro exams")
class program_manager(trainer,student):
    def work(self):
        print("manage the work")
a=program_manager()
a.compny()
a.teach()
a.study()
a.work()'''

#super()-->the super() function is used in inheritance to access the methods and attributes of the parent (super class) 
'''class Parent:
    def __init__(self,name):
        self.name=name
        print("parent constructor")

class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print("child constructor")
a=Child("ravi",21)
print(a.age)
print(a.name)'''


#encapsulation

#encapsulation
#publicdata()
'''class Parent():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class Child(Parent):
    def method2(self):
        print(self.publicdata)
a=Child()
a.method1()
a.method2()'''

#_protecteddata
'''class Parent():
    _publicdata=100
    def method1(self):
        print(self._publicdata)
class Child(Parent):
    def method2(self):
        print(self._publicdata)
a=Child()
a.method1()
a.method2()
print(a._publicdata)'''

#__privatedata
'''class Parent:
    __privatedata = "python"

    def method1(self):
        print(self.__privatedata)


class Child(Parent):
    def method2(self):
        print(self.Parent_privatedata)


a = Child()
a.method1()
a.method2()'''

#abstraction--->hiding unneccessary information from user is called abstraction
#abstraction has two types abstract class and abstract method
#one or more abstracts methods is called abstract class
#without implementation we can use abstract method

'''class A:
    def method1(self):
        pass
obj=A()
obj.method1()'''

'''class A:
    def method1(self):
        print("data")
obj=A()
obj.method1()'''

'''from abc import ABC,abstractmethod
class A:
    @abstractmethod
    def method1(self):
        print("python")
obj=A()
obj.method1()''' 

'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("python")
obj=A()
obj.method1()'''

'''from abc import ABC,abstractmethod
class A(ABC):#parent class
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("method2 implemented")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("method1 implemented")
    def method3(self):
        print("method3 implemented")
obj=B()
obj.method1()
obj.method2()
obj.method3()'''


