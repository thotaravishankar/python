n = int(input("number of students:\n"))
a=[]
for i in range(1,n+1):
    marks = int(input(f"Student{i} marks:"))
    a.append(marks)
avg = sum(a)/n
print("====================================================================================")
print("                    Marks Analysis Report")
print("====================================================================================")
print("Number of Students:",n)
print("Highest Mark:",max(a))
print("Lowest Mark:",min(a))
print("Total sum of marks:",sum(a))
print("Average marks:",avg)
print("====================================================================================")
