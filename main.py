import streamlit as st
import os

# Function to read HTML content
def load_html(file_path):
    with open(file_path, "r") as file:
        return file.read()

# Load the HTML content from the file
html_content = load_html("homepage.html")

# Streamlit app
def main():
    st.title("Brandmark Logo Maker")
    
    # Display the HTML content
    st.components.v1.html(html_content, height=1000, scrolling=True)

if __name__ == "__main__":
    main()

