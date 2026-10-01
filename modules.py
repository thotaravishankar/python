#Differnece between module,library,package

#Module
#-->a module is a single python file consists python code
#a module contains functions, classes and variables
#examples of modules such as math.py,random.py and mymodule.py

#Library
#-->a library consists of both modules and packages
#examples of library such as numpy,requests

#Package
#-->it is a collection of modules
#examples of packages such as numpy,pandas,matplotlib

#Note--> a every python file is a module and import is a keyword and every python file is saved internally with variable name as __main__


'''def greetings(name):
    print("Welcome",name)'''

    
'''a=10
b=20
print("Sum:",a+b)'''

'''a=input("fname:")
b=input("lname:")
print(a+" "+b)'''

'''details={"id":[10,20,30],
         "names":["ravi","spidy","eren"],
         "city":["vjy","queens","paradi_island"]}'''

def dummy():
    if __name__=="__main__":
        print("ravi")
    else:
        print("spidy")
dummy()
        
