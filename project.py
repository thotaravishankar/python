#EMAIL AUTOMATION
#OTP AUTHENTICATION
import random
import math
import smtplib

digits="0123456789"
OTP=""

for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+" is your otp"
msg=otp

s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("ravishankarthota30@gmail.com","novl nolb ryge efkp")
user="ravishankarthota30@gmail.com"
email=input("enter the mail:")
s.sendmail(user,email,msg)

while True:
    a=input("enter the otp:")
    if a==OTP:
        print("otp is correct")
    else:
        print("invalid otp")
