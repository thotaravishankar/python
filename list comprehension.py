#list comprehension
#Every list comprehension can be rewritten as a for loop but every for loop cannot be rewritten in list comprehension.

'''a = ["vjy","kkd","vzg"]
b = [i.upper() for i in a]
print(b)'''

'''a=["python","java","ml"]
b = [i.capitalize() for i in a]
print(b)'''

'''a = [1,2,3,5,6,8,12,13]
b = [i**2 for i in a]
print(b)'''

#if usage in list comprehension
'''b = [i for i in range(16) if i%2==0]
print(b)'''
'''fruits = ["apple","grapes","kiwi","mango","banana","berry"]
b = [i for i in fruits if "a" in i]
print(b)'''


#no elif usage in list comprehension

#if-else usage in list comprehension
'''b = [i**2 if i%2==0 else i*5 for i in range(21)]
print(b)'''

'''a = [1,2,3,4,5]
b = [5,4,3,2,1]
c = [a[i]+b[i] for i in range(len(a))]
print(c)'''

'''a = [list(map(int,input("enter list").split())) for i in range(2)]
print(a)'''

n = 3
a = [[i*j for j in range(1,n+1) if i!=j] for i in range(1,n+1)]
print(a)


