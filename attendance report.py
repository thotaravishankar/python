import datetime
n = int(input("number of students:\n"))
present=0
absent=0
for i in range(1,n+1):
    print("Student"+str(i))
    while True:
        students = input("enter 'P' for Present or 'A' for Absent:").lower()
        print()
        if students=='p':
            present+=1
            break
        elif students=="a":
            absent+=1
            break
        else:
            print("please enter valid input")
print("===============================================================================================")
print("                             Class Attendance Report")
print("===============================================================================================")
print("Attendance Posted:",datetime.datetime.now())
print("Total Number of students in class:",n)
print("Total Students attendend Today:",present)
print("Total Students absent Today:",absent)
print("===============================================================================================")

