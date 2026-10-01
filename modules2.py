#math module
'''import math as m
print(m.pi)
print(m.pi+3)
print(m.sqrt(2))
print(m.tan(45))
print(m.log(20))
print(m.cos(60))
print(m.sin(30))
print(m.pow(2,4))
print(m.ceil(2.8))
print(m.ceil(2.5))
print(m.ceil(5))
print(m.floor(4.9))
print(m.floor(8))'''


'''from math import pi,sqrt,log
print(pi)
print(sqrt(2))
print(log(10))'''

#sys module
'''import sys
print(sys.path)

for i in sys.path:
    print(i)

print(sys.version)'''


#os
'''import os
print(os.path)
print(os.getcwd())

print(os.listdir())
print(os.mkdir("sep"))
print(os.listdir())
print(os.chdir("C:\\Users\\hp\\Downloads"))
print(os.listdir())'''
      

#random module
#-->random module is used to generate random numbers, randint function is used and this function defined in random module
#sample()
'''import random
a=random.sample(range(20,30),5)
print(a)

import random
print(random.randint(1,10))

import random
a=["ravi","spidy","naruto","eren"]
print(random.choice(a))'''



#dice code

'''import random as r
while True:
    n=int(input("enter th roll of the dice:\n"))
    a = r.randint(1,6)
    print(a)
    options = int(input(options:
1.Yes
2.No\n))
    if options==1:
        continue
    elif options==2:
        break
    else:
        print("Invalid input")'''



#calendar module
import calendar
'''year=2026
month=9
print(calendar.month(year,month))'''

'''year=2027
print(calendar.calendar(year))'''

'''a=int(input("enter a value:"))
b=int(input("enter b value:"))
print(calendar.month(a,b))'''


#datetime module
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

#epoch time
'''import time
a=time.time()
print(a)

b=time.localtime(a)
print(b)

print(f"today date is: {b.tm_year}-{b.tm_mon}-{b.tm_mday}")
print(f"{b.tm_hour}:{b.tm_min}:{b.tm_sec}")
print(f"{b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")'''


'''import time,random

for i in range(10):
    a=random.choice(range(1,100))
    print(a)
    time.sleep(2)'''


#regular expressions--> regex are powerfull tools(module)embedded in python which is mainly used to find a patternwith in a given strings
#or statements or files and we mainly used for text manipulation.

'''a="ravi shankar"
print(a)


a="ravi\nshankar\n"
print(a)

#rstring
a=r"ravi\nshankar"
print(a)'''


#regex
#compile(),serach(),findall(),split(),sub()
#sequence characters
##\w-->it matches alphanumeric
##\W-->it matches non alphanumeric
##\d-->it matches digits
##\D-->it matches non digits
##\s-->it matches white spaces
##\S-->it matches non white spaces

import re
#a="map cat maths money cash cap cup mat dog donkey"
'''b=re.compile(r"m\w")
print(b)

c=b.search(a)
print(c)

d=re.search(r"m\w+",a)
print(d)

#findall()
b=re.findall(r"m\w+",a)
print(b)'''

#split()
'''c=re.split(r"m",a)
print(c)

d=re.split(r"\s",a)
print(d)'''

#sub()
'''e=re.sub(r"m","k",a)
print(e)'''

import re
'''a= "wewknc;kehgrithrpoihrcpiogihrm oigherpicghero12345678934567893456789"
b=re.compile(r"\d\d")
print(b)

c=re.search(r"\d",a)
print(c)
print(c.span())

d=re.findall(r"\d+",a)
d=re.findall(r"\d{2}",a)
print(d)

e=re.split("\s",a)
print(e)

f=re.sub("\d","r",a)
print(f)''''





            



