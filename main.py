from add_book import add_book
from view_books import view_books
from issue_book import issue_book
from return_book import return_book

def menu():
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

while True:
    menu()

    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 1:
        add_book()
    elif choice == 2:
        view_books()
    elif choice == 3:
        issue_book()
    elif choice == 4:
        return_book()
    elif choice == 5:
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice! Try again.")