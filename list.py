Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list
a=[2,5.6,"ravi",2+7j,True,False]
type(a)
<class 'list'>
c=[8.5]
type(c)
<class 'list'>
b=5.6
type(b)
<class 'float'>

#append()
a=["python","java","c","c++"]
a.append("dsa")
a
['python', 'java', 'c', 'c++', 'dsa']
a.append("ai","ml")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append("ai","ml")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ai","ml"])
a
['python', 'java', 'c', 'c++', 'dsa', ['ai', 'ml']]

#extend
b = ["python","cyber","soc","pentesting"]
b.extend(["hacking","SIEM'])
          
SyntaxError: unterminated string literal (detected at line 1)
b.extend(["hacking","SIEM"])
          
b
          
['python', 'cyber', 'soc', 'pentesting', 'hacking', 'SIEM']

#insert
          
a=["apple","samsung","poco"]
          
a.insert(1,"mi")
          
a
          
['apple', 'mi', 'samsung', 'poco']

#index
          
a=["kali","linux","ios"]
          
a.index(1)
          
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.index(1)
ValueError: list.index(x): x not in list
a.index("kali")
          
0

#copy
          
a=["ios","windows","linux"]
          
a.copy()
          
['ios', 'windows', 'linux']
b=a.copy()
          
b
          
['ios', 'windows', 'linux']

#clear
          
b.clear()
          
b
          
[]
a.clear()
          
a
          
[]

#sort
          
a=["soc","red","blue","purple","ciso"]
          
a.sort()
          
a
          
['blue', 'ciso', 'purple', 'red', 'soc']
b = sorted(a,key=len)
          
b
          
['red', 'soc', 'blue', 'ciso', 'purple']
b = sorted(a,rev=True)
          
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    b = sorted(a,rev=True)
TypeError: sort() got an unexpected keyword argument 'rev'
b = sorted(a,reverse=True)
          
b
          
['soc', 'red', 'purple', 'ciso', 'blue']

#reverse
          
a=[3,6,2,1,8]
          
a.reverse()
          
a
          
[8, 1, 2, 6, 3]

#pop
          
a=["spider","iron","thor","moon"]
          
a.pop()
          
'moon'
>>> a.pop("thor")
...           
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.pop("thor")
TypeError: 'str' object cannot be interpreted as an integer
>>> a.pop(2)
...           
'thor'
>>> 
>>> #remove
...           
>>> a.remove("iron")
...           
>>> a
...           
['spider']
>>> 
>>> #len
...           
>>> a=["naruto","eren","obito","luffy"]
...           
>>> len(a)
...           
4
>>> 
>>> a.count("naruto")
...           
1
>>> 
