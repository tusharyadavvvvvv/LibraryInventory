# LibraryInventory
The College Library Availability System is a lightweight, command-line interface (CLI) application built in Python to address common organizational issues in a college library's physical inventory system. 
Helping Students to check availiabilty of books without going to library

College Library Availability System

** Project Title**

College Library Availability System (CLI)

Overview of the Project
The College Library Availability System is a lightweight, command-line interface (CLI) application built in Python to address common organizational issues in a college library's physical inventory system. It establishes a digital, single source of truth for book availability, aiming to improve efficiency for librarians and reduce uncertainty for students.

The system operates on a role-based menu, directing users to dedicated functionality: Students can quickly search for book status, and Librarians can easily update records, including expected return dates.

Key Features
The application provides distinct interfaces and capabilities based on the user's role selection:

Student Interface (Option 1)

Keyword Search: Allows students to search the inventory using partial or full title keywords (e.g., "Calculus" or "History").

Instant Status Report: Provides a clear, real-time update on book availability.

Return Date Display: If a book is fully checked out, the student is shown the expected return date to facilitate better planning.

Librarian Interface (Option 2)

Record Update: Ability to update the exact number of available_copies for any book using its unique book_id.

Automated Status Change: The system automatically flags the book as is_available: False when the available copy count drops to zero.

Expected Return Date Input: The librarian is prompted to input an expected return date (YYYY-MM-DD format) when a book is fully checked out.

Input Validation: Includes basic checks to prevent negative copy counts and ensures the updated count does not exceed the total copies.

3. Technologies/Tools Used

Tool/Technology

Description

Python 3.x

The core programming language used for logic and the CLI.

List of Dictionaries

Used as a simple, in-memory dummy database for the inventory data.

Command Line Interface (CLI)

The primary user interface for interaction.

4. Steps to Install & Run the Project

This project requires Python 3.x to run. No external libraries are necessary.

Prerequisites

Python 3 installed on your system.

Installation

Clone the Repository:

git clone https://github.com/your-username/college-library-system.git cd college-library-system

Ensure the File Exists: Verify that the main application file, library_management.py, is present in the directory.

Running the Application

Execute the Python script directly from your terminal:

python library_management.py

Instructions for Testing
After running the script, the interactive CLI menu will appear. You can test both roles using the pre-loaded dummy data:

Scenario 1: Student Check (Option 1)

Select 1 (Student).

Enter the title query: Calculus

Expected Result: Shows "NOT AVAILABLE," with the expected return date of 2025-12-01.

Enter the title query: Mechanics

Expected Result: Shows "AVAILABLE NOW!" with 7 copies in stock.

**Scenario 2: Librarian Update (Option 2) ** Select 2 (Librarian).

Check-In (Making a book available):

Enter the Book ID: MATH305

Enter the new number of available copies: 1

Expected Result: Success message, status changes to AVAILABLE, and the return_date is cleared.

Check-Out (Making a book unavailable):

Enter the Book ID: CS101

Enter the new number of available copies: 0

Enter expected return date: 2025-11-28

Expected Result: Success message, status changes to NOT AVAILABLE, and the return date is set. Screenshots image
<img width="947" height="626" alt="image" src="https://github.com/user-attachments/assets/3e67613a-2e8c-4d5f-aae6-9eb8133f74a6" />
