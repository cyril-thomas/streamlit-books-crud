import streamlit as st
from utils.database import delete_book, get_all_books

def delete_book_page():
    st.title("Delete Book")

    books = get_all_books()
    book_titles = [book['title'] for book in books]

    selected_book = st.selectbox("Select a book to delete", book_titles)

    if st.button("Delete Book"):
        if selected_book:
            delete_book(selected_book)
            st.success(f"Book '{selected_book}' has been deleted.")
        else:
            st.error("Please select a book to delete.")

if __name__ == "__main__":
    delete_book_page()