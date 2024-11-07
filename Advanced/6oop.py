class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        return [f"{book.title} | {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


library = Library("Nairobi Library")
book1 = Book("Harry Potter", "J.K Rowling")
book2 = Book("The Hobbit", "J.R.R Tolkein")
book3 = Book("The Colour of Magic", "Terry Pratchet")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)
print(library.list_books())