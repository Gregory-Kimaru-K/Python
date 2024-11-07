class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        
        elif key == 'author':
            return self.author
        
        elif key == 'num_pages':
            return self.num_pages
        
        else:
            return f"Key {key} not found"


book1 = Book("The Hobbit", "J.R.R Tolkein", 310)
book2 = Book("The Hobbit", "J.R.R Tolkein", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S Lewis", 172)

print(book1)
print(book2)
print(book3)
#eq
print(book1 == book2)
#lt
print("Book 1 Smaller" if book1 < book2 else "Book 1 Bigger")

#add
print(book1 + book2)

#contains

print("Lion" in book3)

#getitem
print(book1['num_pages'])