Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arthematic
a=3
b=4
print(a+b)
7
print(a-b)
-1
print(a*b)
12
print(a/b)
0.75
print(a//b)
0
print(a**b)
81
print(a%b)
3

#assignment
a=3
b=4
b+=2
b
6
b-=4
b
2
b*=2
b
4
b**=2
b
16
b/=4
b
4.0
b//=2
b
2.0
b%=1
b
0.0

#comparision
a=5
b=2
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True

#logical
a=3
b=4
a<b and b>a
True
a<b or b>a
True
not True
False
not False
True
a<=b and b>=a
True
a<=b or b>=a
True

>>> #identify
>>> a=5
>>> type(a) is int
True
>>> type(a) is not int
False
>>> a=9.6
>>> type(a) is int
False
>>> type(a) is not int
True
>>> 
>>> #memebership
>>> a=1,2,3,4,5,6,7
>>> 7 in a
True
>>> 10 in a
False
>>> 10 not in a
True
>>> 
>>> #bitwise
>>> a=6
>>> b=7
>>> a|b
7
>>> a=4
>>> b=5
>>> a|b
5
>>> a=2
>>> b=5
>>> a&b
0
>>> a=3
>>> b=9
>>> a^b
10
>>> ~a
-4
>>> a=3
>>> a<<3
24
>>> a=9
>>> a>>2
2
