Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple
a=(2,4.5,"Ravi",4+5j,True)
type(a)
<class 'tuple'>
len(a)
5
a.count(True)
1
a.index("Ravi")
2


#sets
a={3,4.5,"Ravi",3+4j,True}
print(a)
{True, 3, 4.5, 'Ravi', (3+4j)}
type(a)
<class 'set'>
b = {2,4,5,3,2,4,7,8,8}
b
{2, 3, 4, 5, 7, 8}

a={4,5,6,7,8,9,10}
b={7,8,9,10}
a.issubset(b)
False
b.issubset(a)
True
a.issuperset(b)
True
b.issuperset(a)
False

#union
a={1,2,3,4,5,6,7,8}
b={5,6,7,8,9,10,11,12}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

#intersection
a={1,2,3,4,5,6,7,8}

b={5,6,7,8,9,10,11,12}
a.intersection(b)
{8, 5, 6, 7}

#update
a={1,2,3,4,5,6,7,8}
b={5,6,7,8,9,10,11,12}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
b.upadte(a)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    b.upadte(a)
AttributeError: 'set' object has no attribute 'upadte'. Did you mean: 'update'?
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

#differnce
a={1,2,3,4,5,6,7,8}
b={5,6,7,8,9,10,11,12}
a.differnece(b)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.differnece(b)
AttributeError: 'set' object has no attribute 'differnece'. Did you mean: 'difference'?
a.difference(b)
{1, 2, 3, 4}
b.difference(a)
{9, 10, 11, 12}

#symmentric_differnece
b={5,6,7,8,9,10,11,12}
a={1,2,3,4,5,6,7,8}
a.symmetric_difference(b)
{1, 2, 3, 4, 9, 10, 11, 12}

a={1,2,3,4,5,6,7,8}
b={5,6,7,8,9,10,11,12}
a.diifernece_update(b)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.diifernece_update(b)
AttributeError: 'set' object has no attribute 'diifernece_update'. Did you mean: 'difference_update'?
a.difference_update(b)
a
{1, 2, 3, 4}
b.difference(a)
{5, 6, 7, 8, 9, 10, 11, 12}
b
{5, 6, 7, 8, 9, 10, 11, 12}
b.difference_update(a)
b
{5, 6, 7, 8, 9, 10, 11, 12}


b={5,6,7,8,9,10,11,12}
a={1,2,3,4,5,6,7,8}
a.intersection_update(b)
a
{8, 5, 6, 7}
b.intersection_update(a)
b
{8, 5, 6, 7}

a={1,2,3,4,5,6,7,8}
b={5,6,7,8,9,10,11,12}
a.symmetric_difference_update(b)
a
{1, 2, 3, 4, 9, 10, 11, 12}
b.symmetric_difference_update(a)
a
{1, 2, 3, 4, 9, 10, 11, 12}
b
{1, 2, 3, 4, 5, 6, 7, 8}
 #pop
a={1,2,3,4,5}
a.pop()
1
a.pop(5)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    a.pop(5)
TypeError: set.pop() takes no arguments (1 given)
>>> a.remove(2)
>>> a
{3, 4, 5}
>>> 
>>> a={7,8,9,2}
>>> a.copy()
{8, 9, 2, 7}
>>> b = a.copy()
>>> b
{8, 9, 2, 7}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(1)
>>> b
{1}
>>> 
...  
>>> a={1,2,3,4}
>>> b= {4,5,6,7}
>>> a.isdisjoint(b)
False
>>> a={1,2,3}
>>> b={4,5,6}
>>> a.isdisjoint(b)
True
>>> a = {5,6,7}
>>> a.discard(7)
>>> a
{5, 6}
