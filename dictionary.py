Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary
a={"name":"Ravi", "year":2026,"month":8.0}
a
{'name': 'Ravi', 'year': 2026, 'month': 8.0}
type(a)
<class 'dict'>
b = {"name","year","month"}
type(b)
<class 'set'>
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['Ravi', 2026, 8.0])
a.items()
dict_items([('name', 'Ravi'), ('year', 2026), ('month', 8.0)])

a={"year":2026,"month":8.0}
a.upadte({"date":20})
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.upadte({"date":20})
AttributeError: 'dict' object has no attribute 'upadte'. Did you mean: 'update'?
a.update({"date":20})
a
{'year': 2026, 'month': 8.0, 'date': 20}
a.update({"name":"ravi","course":"python"})
a
{'year': 2026, 'month': 8.0, 'date': 20, 'name': 'ravi', 'course': 'python'}

#setdefault
a={"name":"pooja"}
a.setdefault("city","kkd")
'kkd'
a
{'name': 'pooja', 'city': 'kkd'}











KeyboardInterrupt
a.setdefault("city","vjy")
'kkd'
a
{'name': 'pooja', 'city': 'kkd'}

>>> a.pop("city")
'kkd'
>>> a
{'name': 'pooja'}
>>> a,popitem()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a,popitem()
NameError: name 'popitem' is not defined
>>> a.popitem()
('name', 'pooja')
>>> a
{}
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a = {"id":[10,20,30],"names":["ravi","naruto","eren"]}
>>> type(a)
<class 'dict'>
>>> a
{'id': [10, 20, 30], 'names': ['ravi', 'naruto', 'eren']}
>>> a.keys()
dict_keys(['id', 'names'])
a
>>> a.values()
dict_values([[10, 20, 30], ['ravi', 'naruto', 'eren']])
>>> a.items()
dict_items([('id', [10, 20, 30]), ('names', ['ravi', 'naruto', 'eren'])])
