Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #DataTypes
>>> a=10
>>> type(a)
<class 'int'>
>>> isinstance(a,int)
True
>>> b=6.8
>>> type(b)
<class 'float'>
>>> c="code"
>>> type(c)
<class 'str'>
>>> d="codegnan"
>>> type(d)
<class 'str'>
>>> e= 5j+1
>>> type(e)
<class 'complex'>
>>> e=j
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    e=j
NameError: name 'j' is not defined
>>> e=3+5i
SyntaxError: invalid decimal literal
>>> f = True
>>> type(f)
<class 'bool'>
>>> g = False
>>> type(g)
<class 'bool'>
>>> h=true
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    h=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> i=5j
>>> type(i)
<class 'complex'>
