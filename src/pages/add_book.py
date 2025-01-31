import streamlit as st
from utils.database import add_book as add_book_to_db

def add_book():
    st.title("Add New Book")
    
    with st.form(key='add_book_form'):
        title = st.text_input("Title")
        author = st.text_input("Author")
        year = st.number_input("Year", min_value=0, max_value=2023)
        genre = st.text_input("Genre")
        submit_button = st.form_submit_button("Add Book")
        
        if submit_button:
            if title and author and year and genre:
                add_book_to_db(title, author, year, genre)
                st.success("Book added successfully!")
            else:
                st.error("Please fill in all fields.")

if __name__ == "__main__":
    add_book()