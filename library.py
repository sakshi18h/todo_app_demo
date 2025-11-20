class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return
        
        for i, book in enumerate(self.books, start=1):
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{i}. {book.title} by {book.author} ({status})")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                print("Book borrowed successfully!")
                return
        print("Book not available!")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.is_borrowed = False
                print("Book returned successfully!")
                return
        print("Book not found or not borrowed.")

def main():
    library = Library()
    
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)

        elif choice == "4":
            title = input("Enter book title to return: ")
            library.return_book(title)

        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
