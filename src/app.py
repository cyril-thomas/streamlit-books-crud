import streamlit as st
from streamlit_option_menu import option_menu
from streamlit import session_state as SessionState

# Import pages
from pages.add_book import add_book
from pages.delete_book import delete_book
from pages.update_book import update_book
from pages.view_books import view_books
from utils.database import create_table, load_table_data


# Main application
def main():

    if "db_intialization" not in st.session_state:
        SessionState.db_intialization = True
        create_table()
        # load_table_data()

    st.title("Book Inventory Management")

    with st.sidebar:
        selected = option_menu(
            "Menu",
            ["Add Book", "Delete Book", "Update Book", "View Books"],
            icons=["book", "trash", "pencil", "eye"],
            menu_icon="cast",
            default_index=3,
        )

    if selected == "Add Book":
        add_book()
    elif selected == "Delete Book":
        delete_book()
    elif selected == "Update Book":
        update_book()
    elif selected == "View Books":
        view_books()


if __name__ == "__main__":
    main()
