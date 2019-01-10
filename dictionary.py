## Dictionary file

class BookList:
    books= {}
    def __init__(self,bookName,pages):
        self.books[bookName]=pages
        #self.books[pages]= pages
        print('Initialed a Booklist with one book!')
    def getBooks(self):
        return list(self.books.keys())
    def addBook(self, bookName, pages):
        self.books[bookName] = pages
        print("you've added a new book!")
