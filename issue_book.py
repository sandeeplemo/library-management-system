from utils import books, issued_books

def issue_book():
    book_name = input("Enter book name to issue: ")

    if book_name in books:
        books.remove(book_name)
        issued_books.append(book_name)
        print("Book issued successfully!")
    else:
        print("Book not available.")