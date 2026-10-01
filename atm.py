#ATM Application
import datetime
print("============================================ATM===================================================================")
amount = 100000
exit = "1"
card = input("Insert the Card:\n")
if card == "c":
    print("Welcome, Ravi\n")
    pwd = input("Enter Password:\n")
    if pwd == "123456":
        while exit=="1":
            print('''options:
    1. Balance Enquiry
    2. Withdraw\n''')

            options = int(input())
            if options == 1:
                print("==========================================================================================\n")
                print("Account Holder: Ravi")
                print(f"Your Balance amount is: {amount}\n")
                print("==========================================================================================\n")
                exit = input('''Want to Check another Query:
    Enter 1 to check another query
    Enter 2 exit\n''')
                if exit == "2":
                    print("Thank you, Visit again")
            elif options == 2:
                withdraw = int(input("enter withdrawl money:\n"))
                if withdraw>amount:
                    print("Insufficient amount\n")
                else:
                    print("==========================================================================================\n")
                    print("Date:", datetime.datetime.now())
                    print("Account Holder: Ravi")
                    print(f"Money Withdrawed: {withdraw}")
                    amount-=withdraw
                    print(f"Remaining balance in account: {amount}\n")
                    print("==========================================================================================\n")
                exit = input('''Want to Check another Query:
    Enter 1 to check another query
    Enter 2 exit\n''')
                if exit == "2":
                    print("Thank you, Visit again")
            else:
                print("select valid option")
                               
    else:
        print("Invalid password")

else:
    print("Invalid card")
