#while-loop
'''a=10
while a>1:
    print(a)'''

'''a=5
while a<5:
    print(a)'''

    
'''a=10
while a>1:
    print(a)
    a=a-1'''

'''a=10
while a>=1:
    print(a)
    a=a-1'''

'''a=10
while a>1:
    a=a-1
    print(a)'''


'''a=10
while a<30:
    print(a)
    a=a+1'''

'''a=10
while a>2:
    print(a)
    a-=1'''

'''a=20
while a>2:
    print(a)
    a+=1'''

'''a=5
while a<30:
    print(a)
    a=a+1'''


'''while True:
    age=int(input("enter your age:\n"))
    if age>=18:
        print("eligible for voting\n")
    else:
        print("not eligible for voting\n")'''

#range()
#the range function returns a seqeunce of numbers, starting from 0 by default and increments by one by one and stops before specify number.
'''for i in range(10):
    print(i)'''

'''for in range(5,50):
    print(i)'''

'''for i in range(0,20,2):
    print(i,end=",")'''


'''for i in range(3,30,3):
    print(i,end=",")'''

'''for i in range(5,50,5):
    print(i,end=",")'''

'''while True:
    n = int(input("enter your marks:\n"))
    if n in range(91,101):
        print("Grade A\n")
    elif n in range(81,91):
        print("Grade B\n")
    elif n in range(71,81):
        print("Grade C\n")
    elif n in range(51,71):
        print("Grade D\n")
    else:
        print("Fail\n")'''


#Differnce between break,continue and pass
#the break is used to terminate entire loop
#continue is used to skips the current iteration and rest of the code will continue
#pass is an null statement it does nothing but syntatically we need

#break
'''a=30
while a>10:
    print(a)
    a=a-1
    if a==20:
        break'''


'''for i in range(35):
    if i==30:
        break
    print(i)'''


'''a="python"
for i in a:
    if a=="h":
        break
    print(a)'''

#continue
'''a=40
while a>20:
    if a==35:
        continue
    print(a)
    a=a-1'''

'''for i in range(40):
    if a==26:
        continue
    print(a)'''

'''a="python"
for i in a:
    if a=="t":
        continue
    print(a)'''

#pass
'''a=40
while a>20:
    if a==35:
        pass
    print(a)
    a=a-1'''


'''for i in range(40):
    if i==25:
        pass
    print(a)'''


                
