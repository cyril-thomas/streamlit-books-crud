import streamlit as st
from utils.database import get_all_books
import pandas as pd
import speech_recognition as sr
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
import os


def filter_books_with_llm(text, books_df):
    llm = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        # model="gpt-4o-mini",
    )
    prompt_template = PromptTemplate(
        input_variables=["text", "books"],
        template="""
        Given the following text: "{text}"
        and the following books data:
        {books}
        Filter the books data based on the text and return the filtered data as a JSON string.
        """,
    )
    books_json = books_df.to_json(orient="records")
    prompt = prompt_template.format(text=text, books=books_json)
    response = llm(prompt)
    filtered_books = pd.read_json(response, orient="records")
    return filtered_books


def view_books():
    st.title("Book Inventory")
    st.subheader("List of Books")

    books = get_all_books()
    audio = st.audio_input("Tell me how to filter the data")
    if audio:
        recognizer = sr.Recognizer()
        audio_data = sr.AudioFile(audio)
        with audio_data as source:
            audio_content = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_content)
            st.write(f"Recognized Text: {text}")

            filtered_books = filter_books_with_llm(text, panda_dataframe(books))
            streamlit_dataframe(filtered_books)

        except sr.UnknownValueError:
            st.write("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            st.write(
                f"Could not request results from Google Speech Recognition service; {e}"
            )
    else:
        if books:
            streamlit_dataframe(books)
        else:
            st.write("No books in the inventory")


def streamlit_dataframe(books):
    config = {
        "Publication Year": st.column_config.TextColumn("Publication Year"),
        "ISBN": st.column_config.TextColumn("ISBN"),
    }

    st.dataframe(
        panda_dataframe(books),
        hide_index=True,
        use_container_width=True,
        column_config=config,
    )


def panda_dataframe(books):
    return pd.DataFrame(
        books,
        columns=["Book ID", "Title", "Author", "Publication Year", "ISBN"],
    )


if __name__ == "__main__":
    view_books()
