class Library:

#The library uses it's own inventory for reference.
    def __init__(self):
        self.library = {}
        
#If an item is added, it's status is on the shelf.
    def add_item(self, book_name):
        self.library[book_name] = 'on shelf'

#An item can only be on the shelf or checked out, and if it's neither, it's not available at the library.
    def update_item(self, book_name, status):
        if book_name in self.library:
            if self.library[book_name] == 'on shelf':
                self.library[book_name] = 'checked out'
            else:
                self.library[book_name] = 'on shelf'
        else:
            print("This book is not available at the library.") 

#When a user wants to print a list of books and their statuses, it will be formatted as the title before the status.
    def print_inventory(self):
        for title, status in self.library.items():
            print(f"{title}: {status}")
        
    def check_title_details(self, book_name):
        if book_name in self.library:
            status = self.library[book_name]
            return f"Book Title: {'book_name'}, Status: {'status'}"
        else:
            return "This book is not available at the library."
    
    
#Now that we've established statuses of books, we need to make sure that the program is viable to function based on user input. 
def main():
    my_library = Library()
    while True:
        print("\nWelcome to the Library! What a wonderful reading adventure awaits you.")
        print("1. Print a list of books available at the library")
        print("2. Add a book to the library's inventory")
        print("3. Is there a book you can't find on the shelf, or are returning today? Choose this option to toggle it's location status.")
        print("4. Exit the application. We hope to you see you at the library again soon!")
        choice = input("Please select one of the options above to continue: ")
        
        if choice == '1':
            my_library.print_inventory()
        elif choice == '2':
            title = input("Enter the title of the book to add: ")
            my_library.add_item(title)
            print(f"'{title}' has been added to the online library inventory.")
        elif choice == '3':
            title = input("Please enter the title of the book to toggle it's status: ")
            if title in my_library.library:
                status = my_library.library[title]
                my_library.update_item(title, status)
                print(f"The status of {title} has been changed.")
            else:
                print("This book is not available at the library.")
        elif choice == '4':
            print("You are now exiting the program.")
            break
        else:
            print("Oh no! You've chosen an option that doesn't exist. Please try again.")

if __name__ == "__main__":
    main()
