#single inheritence program for library system
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display_book_details(self):
        print("The book ",self.title," is written by ",self.author,end=" ")
class IssuedBook(Book):
    def __init__(self,title,author,issued_to,issued_date):
        super().__init__(title,author)
        self.issued_to=issued_to
        self.issued_date=issued_date
    
    def issued_book_details(self):
        self.display_book_details()
        print(" is issued to ",self.issued_to," on ",self.issued_date,".")
mybook=IssuedBook("python programming","Guido","Roja","03-02-2026")
mybook.issued_book_details()
