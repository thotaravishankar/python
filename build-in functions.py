#built-in Functions

'''print(dir())
print(dir("__builtins__"))'''



#fromkeys()
'''a="cybersecuity"
print(a)
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))#error

b = dict.fromkeys(a)
print(b)

b = dict.fromkeys(a,"ravi")
print(b)

b["b"]="python"
print(b)'''



#zip--> we can combine multiple collections into one collection

'''a=[1,2,3,4,5]
name=["ravi","spidy","tony","naruto","eren"]
print(a+name)

b=zip(a,name)
print(*b)

c=list(zip(a,name))
print(c)

d=tuple(zip(a,name))
print(d)

e=set(zip(a,name))
print(e)

f=dict(zip(a,name))
print(f)'''

#enumerate()--> we can add counter to the collection
'''names=["ravi","spidy","tony","naruto","eren"]
for i in range(len(names)):
    print(i,names[i])


b = dict(enumerate(names))
print(b)

b=dict(enumerate(names,10))
print(b)

b = list(enumerate(names))
print(b)

b = tuple(enumerate(names))
print(b)

b = set(enumerate(names))
print(b)'''

#ASCII
#chr,ord
'''print(chr(97))
print(chr(122))

print(type(ord("A")))
print(ord("Z"))'''

'''for i in range(26):
    print(chr(97+i),end="")
print()
for i in range(26):
    print(chr(65+i),end="")'''

n = input("enter name:\n")
for i in n:
    print(f"{i}: {ord(i)}")


