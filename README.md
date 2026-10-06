Library Management System

Project Description

The Library Management System is a Python-based application developed to manage library books, members, and book transactions.

In Assessment-III, the project is completed with the required functionality, testing, permanent data storage, and a menu-driven interface.

The system allows the librarian to:

Add books
Search books
Update books
Remove books
Register members
Issue books
Return books
Calculate overdue fines
View transaction records
Store data permanently
Objectives

The main objectives of Assessment-III are:

To complete the implementation of the Library Management System.
To test the functionality of all major modules.
To manage books and members efficiently.
To maintain book issue and return records.
To calculate overdue fines.
To store data permanently using file handling.
To maintain a clean and organized GitHub repository.
To demonstrate the final working project.
Final Features
1. Book Management

The system provides the following book management operations:

Add Book
Search Book
Update Book
Remove Book

Each book contains:

Book ID
Book Name
Author Name
Status
2. Member Management

The system allows the librarian to register library members.

Member details include:

Member ID
Member Name
Phone Number
3. Book Issue

A book can be issued to a registered member.

Before issuing a book, the system checks:

Whether the book exists
Whether the member exists
Whether the book is already issued

If all conditions are satisfied, the book is issued successfully.

4. Book Return

The system allows issued books to be returned.

When a book is returned:

Book status is changed to Available.
Return date is stored.
Overdue days can be entered.
Fine amount is calculated.
Transaction record is updated.
5. Fine Calculation

The system calculates the fine according to the number of overdue days.

The project uses:

Fine = Overdue Days × ₹5
Example
Overdue Days = 3

Fine = 3 × 5
     = ₹15

Note: ₹5 per day is used as a project assumption.

6. Transaction Management

The system maintains transaction records containing:

Book ID
Member ID
Issue Date
Return Date
Fine Amount

Example:

Book ID: B101
Member ID: M101
Issue Date: 2026-09-20
Return Date: 2026-09-25
Fine: 15
7. Permanent Data Storage

The project uses JSON files for permanent storage.

The following files are used:

books.json
members.json
transactions.json

This allows the data to remain available even after the Python program is closed.

Technologies Used
Python
JSON
File Handling
Date Handling
Python Concepts Used
Variables
Input and Output
Conditional Statements
Loops
Functions
Lists
Dictionaries
File Handling
JSON
Exception Handling

Sample Output
Add Book
Enter your choice: 1

Enter Book ID: B101
Enter Book Name: Python Programming
Enter Author Name: ABC

Book added successfully!
Register Member
Enter your choice: 5

Enter Member ID: M101
Enter Member Name: Rahul
Enter Phone Number: 9876543210

Member registered successfully!
Issue Book
Enter your choice: 6

Enter Book ID: B101
Enter Member ID: M101

Book issued successfully!
Return Book
Enter your choice: 7

Enter Book ID to return: B101
Enter overdue days: 3

Fine: 15
Book returned successfully!
View Transactions
Enter your choice: 9

----- TRANSACTION RECORDS -----

Book ID: B101
Member ID: M101
Issue Date: 2026-09-20
Return Date: 2026-09-25
Fine: 15