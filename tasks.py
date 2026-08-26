#even or odd
'''n = int(input("enter n value:\n"))
if n%2==0:
    print("even")

else:
    print("odd")


#voting  system

age = int(input("enter your age:\n"))

if age>=18:
    print("eligible for voting")

else:
    print("not eligible for voting")


#leap year

year = int(input("enter year:\n"))

if year%4==0:
    print("leap year")
    
else:
    print("not a leap year")'''



'''#guest code
name = input("enter name:\n").lower()
l = ["spiderman","tony","jhonny","batman","ben"]
if name in l:
    print(f"Welcome {name}")

else:
    print("Welcome Guest")'''


'''#vowels
char = input("enter char:\n")
if char.lower() in "aeiou":
    print("vowel")

else:
    print("consonent")'''


'''#bakery
price = int(input("enter cake price:\n"))
if isinstance(price,int):
    if price==1200:
        print("red velvet cake")
    elif price==1000:
        print("Almond cake")
    elif price==800:
        print("chocolate cake")
    elif price==600:
        print("butterscotch cake")
    else:
        print("sorry cake not available")
else:
    print("price should integer")'''
'''#pizza
pizza = input("enter pizza:\n").lower()
if pizza=="crispy chicken pizza":
    print("Total bill is 800")
elif pizza=="bbq pizza":
    print("Total bill is 600")
elif pizza=="paneer pizza":
    print("Total bill is 400")
elif pizza=="cheesse and corn":
    print("Total bill is 300")
elif pizza=="frenchfries and coke":
    print("Total bill is 200")
else:
    print("no such item available")'''

'''#multiple-if
age = int(input("enter age:\n"))
attendence = eval(input("enter your attendence:\n"))
marks = eval(input("enter your marks:\n"))
if age>=18:
    print("eligible for scholarship")
if attendence>=90:
    print("allow to write exams")
if marks>=80:
    print("eligible for higher studies")'''


#nested-if
username = input("enter username:\n")
password = input("enter password:\n")
if username=="ravi":
    if password=="123456":
        print("login successful")
    else:
        print("login failed")
else:
    print("username not found")



#if -else
username = input("enter username:\n")
password = input("enter password:\n")
if username=="ravi" and password=="1234567":
    print("login success")
else:
    print("login failed")




