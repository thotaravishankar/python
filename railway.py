import datetime
def railway(gen,ticket,age):
    if gen==1:
        if age>=60:
            dis=0.3*ticket
            total=ticket-dis
        else:
            total=ticket
    elif gen==2:
        if age>=60:
            dis=0.5*ticket
            total=ticket-dis
        else:
            dis=0.3*ticket
            total=ticket-dis
    return total

def e_ticket(name,gen,age):
    print("======================================================================")
    print("                      Railway E-Ticket")
    print("======================================================================")
    print("Booking Time:",datetime.datetime.now())
    print("Name:",name)
    if gen==1:
        a="Male"
    else:
        a="Female"
    print("Gender:",a)
    print("Age:",age)
    print("Ticket Price:",railway(gen,ticket,age))
    print("======================================================================")

ticket=1000
name=input("enter your name:")
gen=int(input('''options:
1.Male
2.Female\n'''))
age=int(input("enter your age:"))
e_ticket(name,gen,age)
