import json
from datetime import date

BOOK_FILE = "books.json"
MEMBER_FILE = "members.json"
TRANSACTION_FILE = "transactions.json"


# ---------- File Functions ----------

def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except:
        return []


def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# ---------- Book Functions ----------

def add_book():
    books = load_data(BOOK_FILE)

    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "name": book_name,
        "author": author,
        "status": "Available"
    }

    books.append(book)
    save_data(BOOK_FILE, books)

    print("Book added successfully!")


def search_book():
    books = load_data(BOOK_FILE)

    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            print("\nBook Found")
            print("Book ID:", book["id"])
            print("Book Name:", book["name"])
            print("Author:", book["author"])
            print("Status:", book["status"])
            return

    print("Book not found.")


def update_book():
    books = load_data(BOOK_FILE)

    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            book["name"] = input("Enter New Book Name: ")
            book["author"] = input("Enter New Author Name: ")

            save_data(BOOK_FILE, books)
            print("Book updated successfully!")
            return

    print("Book not found.")


def remove_book():
    books = load_data(BOOK_FILE)

    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            save_data(BOOK_FILE, books)
            print("Book removed successfully!")
            return

    print("Book not found.")


# ---------- Member Function ----------

def register_member():
    members = load_data(MEMBER_FILE)

    member_id = input("Enter Member ID: ")
    name = input("Enter Member Name: ")

    member = {
        "id": member_id,
        "name": name
    }

    members.append(member)
    save_data(MEMBER_FILE, members)

    print("Member registered successfully!")


# ---------- Issue Book ----------

def issue_book():
    books = load_data(BOOK_FILE)
    members = load_data(MEMBER_FILE)
    transactions = load_data(TRANSACTION_FILE)

    book_id = input("Enter Book ID: ")
    member_id = input("Enter Member ID: ")

    book_found = False
    member_found = False

    for book in books:
        if book["id"] == book_id:
            book_found = True

            if book["status"] == "Issued":
                print("Book is already issued.")
                return

            book["status"] = "Issued"

    for member in members:
        if member["id"] == member_id:
            member_found = True

    if not book_found:
        print("Book not found.")
        return

    if not member_found:
        print("Member not found.")
        return

    transaction = {
        "book_id": book_id,
        "member_id": member_id,
        "issue_date": str(date.today()),
        "return_date": ""
    }

    transactions.append(transaction)

    save_data(BOOK_FILE, books)
    save_data(TRANSACTION_FILE, transactions)

    print("Book issued successfully!")


# ---------- Return Book ----------

def return_book():
    books = load_data(BOOK_FILE)
    transactions = load_data(TRANSACTION_FILE)

    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            book["status"] = "Available"

            for transaction in transactions:
                if transaction["book_id"] == book_id and transaction["return_date"] == "":
                    transaction["return_date"] = str(date.today())

            save_data(BOOK_FILE, books)
            save_data(TRANSACTION_FILE, transactions)

            print("Book returned successfully!")
            return

    print("Book not found.")


# ---------- Calculate Fine ----------

def calculate_fine():
    days = int(input("Enter number of overdue days: "))

    fine_per_day = 5
    fine = days * fine_per_day

    print("Overdue Fine = Rs.", fine)


# ---------- View Transactions ----------

def view_transactions():
    transactions = load_data(TRANSACTION_FILE)

    if len(transactions) == 0:
        print("No transactions found.")
    else:
        for transaction in transactions:
            print("\nBook ID:", transaction["book_id"])
            print("Member ID:", transaction["member_id"])
            print("Issue Date:", transaction["issue_date"])
            print("Return Date:", transaction["return_date"])


# ---------- Main Menu ----------

while True:

    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Update Book")
    print("4. Remove Book")
    print("5. Register Member")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Calculate Fine")
    print("9. View Transactions")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        search_book()

    elif choice == "3":
        update_book()

    elif choice == "4":
        remove_book()

    elif choice == "5":
        register_member()

    elif choice == "6":
        issue_book()

    elif choice == "7":
        return_book()

    elif choice == "8":
        calculate_fine()

    elif choice == "9":
        view_transactions()

    elif choice == "10":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")


Output
========== LIBRARY MANAGEMENT SYSTEM ==========

1. Add Book
2. Search Book
3. Update Book
4. Remove Book
5. Register Member
6. Issue Book
7. Return Book
8. Calculate Fine
9. View Transactions
10. Exit

Enter your choice: 1

Enter Book ID: B101
Enter Book Name: Python Programming
Enter Author Name: ABC

Book added successfully!

Enter your choice: 5

Enter Member ID: M001
Enter Member Name: Rahul

Member registered successfully!

Enter your choice: 6

Enter Book ID: B101
Enter Member ID: M001

Book issued successfully!

Enter your choice: 7

Enter Book ID: B101

Book returned successfully!

Enter your choice: 8

Enter number of overdue days: 5
Overdue Fine = Rs. 25

Enter your choice: 9

Book ID: B101
Member ID: M001
Issue Date: 2026-10-06
Return Date: 2026-10-06