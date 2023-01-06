class Library:
    def __init__(self,list,name):
        self.bookList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have the following books in our :{self.name} library")
        for book in self.bookList:
            print(book)

    def lendBook(self,user,book):
        # if ('python','data structure','c-programming',"c#")!= (book) :
        #     print("Please Enter the correct name of the book which i being in display books")
        #     exit()
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("book is been updated! you can take the book now")
        else:
            print(f"book is already being used by {self.lendDict[book]}")

    def addBook(self,book):
        self.bookList.append(book)
        print("your book is been added to the list")

    def returnBook(self,book):
        self.lendDict.pop(book)
        print("Thank you so much for return the Book , Have A Nice Day !")


if __name__ == '__main__':
    hamza =Library(['1: pyhton','2: data structure','3: c-programming','4: C#'],"H-A Hamza")
    print(f"Welcome to the {hamza.name} liberary  Enter your choice to Continue")
    print("1. Display Books")
    print("2. Lend a Book")
    print("3. Add a book")
    print("4. Return a Book")
    while True:
        userchoice = input("please Enter the number (#e.g press :1)  of item you want : ")
        if userchoice not in ['1','2','3','4']:
            print("please Enter the valid (#e.g press :1) option")
            continue
        else:
            userchoice = int(userchoice)


        if userchoice ==1:
            hamza.displayBooks()

        elif userchoice == 2:
            book = input("Enter the name of the book you want to lend :")
            user = input("Enter your name")
            hamza.lendBook(user,book)

        elif userchoice == 3:
            book = input("Enter the name of the book you want to add :")
            hamza.addBook(book)

        elif userchoice == 4:
            book = input("Enter the name of the book you want to return :")
            hamza.returnBook(book)

        else:
            print("sorry we cant reach please enter the correct information")

        print("press q to quit and press c to continue the program")
        userchoice_2 = ""
        while (userchoice_2 != "c"and userchoice_2 != "q"):
            userchoice_2 = input()
            if userchoice_2 == "q":
                exit()
            elif userchoice_2 == "c":
                continue


