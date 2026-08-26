#swapping of two variables
'''a = 10
b = 20
a,b = b,a
print(a,b)'''

'''a = 10
b = 20
temp = a
a = b
b = temp
print(a,b)'''

'''a = 10
b = 20
a = a+b
b = a-b
a = a-b
print("a value is ", a)
print("b value is ", b)'''

a = 10
b = 20
a = a+b
b = a-b
a = a-b
print("after swapping a=%d, b=%d" %(a,b))


a = "ravi"
b = "shankar"
a,b=b,a
print("after swapping a=%s, b=%s" %(a,b))

