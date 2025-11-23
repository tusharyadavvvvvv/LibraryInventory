# -----------------------------------------------------------
# Dummy Library Inventory Dataset
# This is a list of dictionaries, simulating a simple database.
# 'available_copies' tracks current stock.
# 'return_date' is only set if 'available_copies' is 0 (fully checked out).
# -----------------------------------------------------------

library_inventory = [
    {
        "book_id": "CS101",
        "title": "Introduction to Computer Science",
        "author": "J. Smith",
        "total_copies": 5,
        "available_copies": 2,
        "is_available": True,
        "return_date": None  # Available, so return_date is None
    },
    {
        "book_id": "MATH305",
        "title": "Advanced Calculus: Methods",
        "author": "E. Taylor",
        "total_copies": 3,
        "available_copies": 0,
        "is_available": False,
        "return_date": "2025-12-01"  # Fully checked out, expected return date
    },
    {
        "book_id": "PHYS202",
        "title": "Classical Mechanics",
        "author": "D. Halliday",
        "total_copies": 7,
        "available_copies": 7,
        "is_available": True,
        "return_date": None
    },
    {
        "book_id": "HIST105",
        "title": "World History: 1900-Present",
        "author": "M. Johnson",
        "total_copies": 4,
        "available_copies": 1,
        "is_available": True,
        "return_date": None
    }
]

# -----------------------------------------------------------
# Librarian Functionality
# -----------------------------------------------------------

def update_book_availability(inventory, book_id, new_available_copies, return_date=None):
    """
    Function for the librarian to update the available copy count and set 
    the expected return date if the book is fully checked out.
    """
    print(f"\n--- LIBRARIAN ACTION: Updating Book ID {book_id} ---")
    
    # Input validation (basic check)
    if new_available_copies < 0:
        print(" Error: Available copies cannot be negative.")
        return

    for book in inventory:
        if book["book_id"] == book_id:
            # Ensure new count does not exceed total copies
            if new_available_copies > book["total_copies"]:
                print(f" Warning: New available count ({new_available_copies}) exceeds total copies ({book['total_copies']}). Setting to max.")
                new_available_copies = book["total_copies"]
            
            book["available_copies"] = new_available_copies
            
            if new_available_copies > 0:
                # Book is available
                book["is_available"] = True
                book["return_date"] = None
                print(f" Success: Updated '{book['title']}'. {new_available_copies} copies are now available.")
            else:
                # Book is fully checked out
                book["is_available"] = False
                book["return_date"] = return_date
                print(f"Success: Updated '{book['title']}'. Currently unavailable.")
                if return_date:
                    print(f"Expected return date updated to: {return_date}")
                else:
                    print("No expected return date was provided.")
            return
            
    print(f" Error: Book with ID '{book_id}' not found in the inventory.")

# -----------------------------------------------------------
# Student Functionality
# -----------------------------------------------------------

def check_book_status(inventory, title_query):
    """
    Function for students to check the availability status of a book.
    Performs a case-insensitive, partial-match search on the title.
    """
    
    # Normalize query for case-insensitive search
    query = title_query.lower()
    
    found_book = None
    for book in inventory:
        # Check if the search query is part of the book title
        if query in book["title"].lower():
            found_book = book
            break # Stop after finding the first match
            
    if found_book:
        print(f"\n--- STUDENT VIEW: Status for '{found_book['title']}' ---")
        if found_book["is_available"]:
            print(f" **AVAILABLE NOW!**")
            print(f"Copies in stock: {found_book['available_copies']} out of {found_book['total_copies']}.")
        else:
            print(f" **NOT AVAILABLE.** All copies are currently checked out.")
            if found_book["return_date"]:
                print(f"Expected return date: **{found_book['return_date']}**")
            else:
                print("No expected return date available. Please check with the circulation desk.")
    else:
        print(f"\n Search failed: Book with title matching '{title_query}' not found.")


# -----------------------------------------------------------
# Interactive Command Line Interface (CLI)
# -----------------------------------------------------------

if __name__ == "__main__":
    print("***** Welcome to the College Library Availability System *****")
    
    while True:
        print("\nPlease select your role:")
        print("1: Student (Check Book Availability)")
        print("2: Librarian (Update Book Records)")
        print("3: Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        
        if choice == '1':
            title = input("Enter the title or keywords of the book: ").strip()
            if title:
                check_book_status(library_inventory, title)
            else:
                print(" Please enter a search query.")
            
        elif choice == '2':
            print("\n--- Librarian Interface ---")
            book_id = input("Enter the Book ID to update (e.g., CS101): ").strip().upper()
            
            if not book_id:
                print(" Book ID cannot be empty.")
                continue

            try:
                new_copies_input = input("Enter the new number of available copies: ").strip()
                if not new_copies_input:
                    print(" Available copies cannot be empty.")
                    continue
                    
                new_copies = int(new_copies_input)
                
                return_date = None
                if new_copies == 0:
                    return_date = input("Enter expected return date (YYYY-MM-DD), or leave blank: ").strip()
                    if not return_date:
                        return_date = None
                
                update_book_availability(library_inventory, book_id, new_copies, return_date)
            except ValueError:
                print(" Error: Invalid number entered for available copies. Please enter a whole number.")

        elif choice == '3':
            print("Thank you for using the system. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")