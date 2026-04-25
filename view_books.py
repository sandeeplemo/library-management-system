from utils import books

def view_books():
    if not books:
        print("No books available.")
    else:
        print("\nAvailable Books:")
        for book in books:
            print("-", book)