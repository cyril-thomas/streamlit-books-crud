# Book Inventory App

This is a Streamlit application for managing an inventory of books. It provides a user-friendly interface to perform CRUD (Create, Read, Update, Delete) operations on book records.

## Features

- Add new books to the inventory
- View all books in the inventory
- Update existing book details
- Delete books from the inventory

## Project Structure

```
book-inventory-app
├── src
│   ├── app.py                # Main entry point of the application
│   ├── pages
│   │   ├── add_book.py       # Interface for adding new books
│   │   ├── delete_book.py    # Interface for deleting books
│   │   ├── update_book.py    # Interface for updating book details
│   │   └── view_books.py     # Interface for viewing all books
│   └── utils
│       └── database.py       # Database operations
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   streamlit run src/app.py
   ```

## Usage
- Uncomment lines 16 to 19 in app.py only on your first run, then comment back if you see unique constraint error.
- Navigate through the application using the sidebar.
- Use the "Add Book" page to input new book details.
- View the list of books on the "View Books" page. Use the microphone to provide input for filtering the data frame.
- Update or delete books as needed.

## License

This project is licensed under the MIT License.