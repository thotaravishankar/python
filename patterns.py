#reverse right angle
'''n = int(input("enter n value"))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*",end="")
    print()'''


#right angle
'''n = int(input("enter n value"))
for i in range(1,n+1):
    for j in range(0,i):
        print("*",end="")
    print()'''

#square
'''n = int(input("enter n value"))
for i in range(0,n):
    for j in range(0,n):
        print("*",end="")
    print()'''

#pyramid
'''n = int(input("enter n value"))
for i in range(n+1):
    print(" "*(n-i) + "* "*i)'''


#diamond
n = int(input("enter n value"))
for i in range(1,n+1):
    print(" "*(n-i) + "* "*i)
for j in range(n-1 ,0,-1):
    print(" "*(n-j) + "* "*j)
