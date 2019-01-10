## Dictionary file

class BookList:
    books = {
        'Name' : '',
        'Pages' : ''
        }
    
    def __init__ (self,name,pages):
        self.books['Name'] = name
        self.books['Pages'] = pages
        
    def getBooks(self)
        return list(self.books.values())