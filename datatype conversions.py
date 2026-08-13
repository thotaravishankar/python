Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #DataType Conversion
>>> #int
>>> int(5)
5
>>> int(9.5)
9
>>> int("ravi")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("ravi")
ValueError: invalid literal for int() with base 10: 'ravi'
>>> int(5+6j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(5+6j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
>>> 
>>> #float
>>> float(5)
5.0
>>> float(5.6)
5.6
>>> float("ravi")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float("ravi")
ValueError: could not convert string to float: 'ravi'
>>> float(2+6j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(2+6j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> flaot(True)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    flaot(True)
NameError: name 'flaot' is not defined. Did you mean: 'float'?
>>> float(True)
1.0
>>> float(False)
0.0

#string
str(5)
'5'
str(5.2)
'5.2'
str("ravi")
'ravi'
str(5+6j)
'(5+6j)'
str(True)
'True'
str(Flase)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    str(Flase)
NameError: name 'Flase' is not defined. Did you mean: 'False'?

#complex
complex(5)
(5+0j)
complex(5+6j)
(5+6j)
complex(5.6)
(5.6+0j)
complex(True)
(1+0j)
complex(False)
0j
complex("ravi")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    complex("ravi")
ValueError: complex() arg is a malformed string

#Boolean
bool(5)
True
bool(4.5)
True
bool("ravi"
)
True
bool("ravi)
     
SyntaxError: unterminated string literal (detected at line 1)
bool("ravi")
     
True
bool(True)
     
True
bool(False)
     
False
bool(0)
     
False
bool(-9)
     
True
