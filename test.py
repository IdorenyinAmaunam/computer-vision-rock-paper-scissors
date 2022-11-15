class Book:
    def __init__(self):
        pass

    def read_book(self):
        pages = 5

        print(pages)

    def check_book_read(self, pages):
        print(pages)


book = Book()
read_book = book.read_book()
print(type(read_book))
book.check_book_read(read_book)
#print(read_book * 10)