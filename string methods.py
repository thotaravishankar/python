Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a = "hello"
len(a)
5
b = "python course"
len(b)
13
c = ""
len(c)
0
d = " "
len(d)
1

#count
a = "twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("a")
1
a.count("t")
5
a.count(" ")
3

#find
a="python"
a[2]
't'
a.find("t")
2
a.find("n")
5
b="hello"
b.find("l")
2

#escaping sequence
#\n - new line
#\t - tab space
a = "name\nmobileno\tmailid\ncity
SyntaxError: unterminated string literal (detected at line 1)
a = "name\nmobileno\tmailid\ncity"
print(a)
name
mobileno	mailid
city
a = '''name
mobileno\tmailid
city'''
print(a)
name
mobileno	mailid
city
a='name:ravi\nmobileno: 1234567890\tmailid:ravi@gamil.com\ncity:vizag'
print(a)
name:ravi
mobileno: 1234567890	mailid:ravi@gamil.com
city:vizag


#replace
b = "wait untill succeed"
b.replace("wait","work")
'work untill succeed'
b = "india, pakisthan"
b.repalce("pakisthan", "japan")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    b.repalce("pakisthan", "japan")
AttributeError: 'str' object has no attribute 'repalce'. Did you mean: 'replace'?
b.replace("pakisthan", "japan")
'india, japan'

#upper
a="ravi"
a.upper()
'RAVI'

#lower
a = "RAVI"
a.lower()
'ravi'
a.upper(0)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.upper(0)
TypeError: str.upper() takes no arguments (1 given)
#capitalize
a="ravi"
a.capitalize()
'Ravi'

#title
a="ravi shankar"
a.title()
'Ravi Shankar'


a="data"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
b = "data science"
b.isalpha()
False
c="datascience"
c.isalpha()
True
d=345678
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
e="456"
e.isdigit()
True
a= "hello world"
a.startswith
<built-in method startswith of str object at 0x000001EE34DB45B0>
a.startswith()
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    a.startswith()
TypeError: startswith expected at least 1 argument, got 0
a.startswith("h")
True
a.endswith("d")
True

#concatentaion
a="python"
b="course:
SyntaxError: unterminated string literal (detected at line 1)
b= "course"
print(a+b)
pythoncourse
a.concat(b)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    a.concat(b)
AttributeError: 'str' object has no attribute 'concat'
e="ravi"
f="shankar"
print(e+f"
      
SyntaxError: unterminated f-string literal (detected at line 1)
print(e+f)
      
ravishankar
fname="ravi"
      
lname="shankar"
      
print(fname.title()+" "+lname.title())
      
Ravi Shankar
print((fname+" "+lname).title())
      
Ravi Shankar

#strip
      
a='          ravi'
      
a.strip()
      
'ravi'
a.lstrip()
      
'ravi'
a='             ravi               '
      
a.lstrip()
      
'ravi               '
a.rstrip()
      
'             ravi'

 

#split()
      
a= "python java c c#"
      
a.split()
      
['python', 'java', 'c', 'c#']
+
      
SyntaxError: invalid syntax

#join
      
a = "vja","hyd","kkd"
      
''.join(a)
...       
'vjahydkkd'
>>> ' '.join(a)
...       
'vja hyd kkd'
>>> 
>>> #formating
...       
>>> a=4
...       
>>> b=3
...       
>>> print("the sum is", a+b)
...       
the sum is 7
>>> 
>>> #format method
...       
>>> a="motu"
...       
>>> b="patlu"
...       
>>> print("hello {} {}",.format(a,b))
...       
SyntaxError: invalid syntax
>>> print("hello {} {}".format(a,b))
...       
hello motu patlu
>>> print("hello {} hello {}".format(a,b))
...       
hello motu hello patlu
>>> print("hello {} \nhello {}".format(a,b))
...       
hello motu 
hello patlu
>>> 
>>> 
>>> #fstring
...       
>>> a="sweety"
...       
>>> b="cuty"
...       
>>> print(f"hello {a} {b}")
...       
hello sweety cuty
