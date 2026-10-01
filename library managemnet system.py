import datetime
class Library:
    def __init__(self):
        self.a=[]
        self.issue=[]
    def add_book(self,book):
        self.a.extend(book)
        print(f"{book} books successfully added to library store")
    def display(self):
        print()
        print("========================================================================")
        print("                   Displaying Available Books")
        print("========================================================================")
        for j in self.a:
            print(j)
        print("========================================================================")
    def issue_book(self,book1):
        if book1 in self.a:
            name = input("Enter your Name:")
            print()
            print("========================================================================")
            print("                    Book issuing receipt")
            print("========================================================================")
            print(f"Date of issuing: {datetime.datetime.now()}")
            print(f"Book issued to: {name}")
            print(f"Book Issued: {book1} ")
            print("**NOTE: Please return before 7 days from date of issuing**")
            print("========================================================================")
            self.issue.append(book1)
            self.a.remove(book1)
        else:
            print(f"{book1} not available")
            self.display()
    def return_book(self,book2):
        if book2 in self.issue:
            self.a.append(book2)
            self.issue.remove(book2)
            print(f"{book2} book successfully returned")
        else:
            print(f"{book2} not available")
            
c = Library()
print("=======================================================================================================")
print("                             Library Management System")
print("=======================================================================================================")

while True:
    options=input('''Choose Options:
    1.Add Book
    2.Display Books
    3.Issue Book
    4.Return Book
    5.Exit\n''')
    if options=="1":
        c.add_book(book=list(map(str,input("Enter Book Name:").split(","))))
    elif options=="2":
        c.display()
    elif options=="3":
        c.issue_book(book1=input("Enter Book Name:"))
    elif options=="4":
        c.return_book(book2=input("Enter Book Name:"))
    elif options=="5":
        print("***************Visit Again*******************")
        break
    else:
        print("Invalid option")

