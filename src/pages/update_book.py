import streamlit as st
from utils.database import get_book_by_id, update_book

def update_book_page():
    st.title("Update Book Details")

    book_id = st.number_input("Enter Book ID to Update", min_value=1)
    book = get_book_by_id(book_id)

    if book:
        title = st.text_input("Title", value=book['title'])
        author = st.text_input("Author", value=book['author'])
        year = st.number_input("Year", value=book['year'], min_value=0)
        genre = st.text_input("Genre", value=book['genre'])

        if st.button("Update Book"):
            updated_book = {
                'id': book_id,
                'title': title,
                'author': author,
                'year': year,
                'genre': genre
            }
            update_book(updated_book)
            st.success("Book updated successfully!")
    else:
        st.error("Book not found.") 

if __name__ == "__main__":
    update_book_page()