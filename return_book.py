from utils import books, issued_books

def return_book():
    book_name = input("Enter book name to return: ")

    if book_name in issued_books:
        issued_books.remove(book_name)
        books.append(book_name)
        print("Book returned successfully!")
    else:
        print("This book was not issued.")