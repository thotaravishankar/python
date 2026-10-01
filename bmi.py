##body mass index
##18.5 below underweight
##18.5 to 24.5 noraml weight
##24.5 to 29.5 overweight
##30 above obesity
##bmi = wt/ht**2

'''height = float(input("enter your height in cm:\n"))
hm = height*0.01
weight = float(input("enter your weight in kg:\n"))
bmi = weight/hm**2
if bmi<=18.5:
    print("UnderWeight")
elif bmi>18.5 and bmi<=24.5:
    print("Normal Weight")
elif bmi>24.5 and bmi<=29.5:
    print("OverWeight")
elif bmi>=30:
    print("Obesity")'''

def bmi(height, weight):
    height = height * 0.01
    bmi = weight / height ** 2
    if bmi <= 18.5:
        return "UnderWeight"
    elif bmi>18.5 and bmi<=24.5:
        return "Normal Weight"
    elif bmi>24.5 and bmi<=29.5:
        return "OverWeight"
    else:
        return "Obesity"

def report(height,weight):
    print("=============================================================================================================")
    print("                                            BMI Report")
    print("=============================================================================================================")
    print("Your Height:",height)
    print("Your Weight:",weight)
    print("Your Bmi:",bmi(height,weight))
    print("=============================================================================================================")
    

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
report(height,weight)
