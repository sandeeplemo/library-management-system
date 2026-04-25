from utils import books

def add_book():
    book_name = input("Enter book name: ")
    
    if book_name in books:
        print("Book already exists!")
    else:
        books.append(book_name)
        print("Book added successfully!")