class library:
    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lenddict = {}

        def displaybooks(self):
            print(f"we have foolowing books in our lirary:{self.name}")
            for book in self.bookslist:
                print(book)

        def lendbook(self, user, book):
            if book not in self.lenddict.keys():
                self.lenddict.update({book: user})
                print("lender-book database has been updated.you can take the book now")
            else:
                print(f"book is already being used by {self.lenddict[book]}")

        def addbook(self, book):
            self.booklist.append(book)
            print("book has been added to the book list")

        def returnbook(self, book):
            self.lenddict.pop(book)

        if __name__ == '__main__':
            harry = library(['python', 'rich daddy and poor daddy',
                             'harry potter', 'c++', 'algorithm by clrs'], "codewithharry")

    while(True):
        print(
            f"welcome to the {'harry.name'} library. enter your choice to continue")
        print("1. display a book")
        print("2. lend a book")
        print("3. add a book")
        print("4. reutrn a book")
        user_choices = input()
        if user_choices not in {'1', '2', '3', '4'}:
            print("please enter a valid option")
            continue
        else:
            user_choices = int(user_choices)

        if user_choices == 1:
            harry.displaybooks()

        elif user_choices == 2:
            book = input("enter the name of the book you want to lend:")
            user = input("enter your name")
            harry.lendbook(user, book)

        elif user_choices == 3:
            book = input("enter the name of the book you want to add:")
        elif user_choices == 4:
            book = input("enter the name of the book you want to return:")

        else:
            print("not a valid option")

            print("press q to quite and c to continue")
            userchoice2 = ""
            while(user_choice2 != "c" and user_choice2 != "q"):

                user_choice2 = input()
        if user_choice2 == "q":
            exit()
        if user_choice2 == "c":
            continue
