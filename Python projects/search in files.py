import os
import fitz  # PyMuPDF
from docx import Document
import tkinter as tk
from tkinter import scrolledtext



def search_pdf(file_path, query):
    try:
        doc = fitz.open(file_path) # search_pdf function uses PyMuPDF to open a PDF file, fitz.open
        for page_num in range(doc.page_count): # 
            page = doc.load_page(page_num)
            text = page.get_text() # iterates through each page to extract text
            if query.lower() in text.lower():
                return True # If the query is found in the text, it returns True.
    except Exception as e:
        print(f"Error searching in PDF {file_path}: {e}")
    return False # If any errors occur during this process, it prints an error message and returns False.

def search_word_document(file_path, query):
    try:
        doc = Document(file_path) # search_word_document function uses python-docx to open a Word document 
        for paragraph in doc.paragraphs:
            if query.lower() in paragraph.text.lower(): #  iterates through each paragraph. 
                return True # If the query is found in any paragraph, it returns True.
    except Exception as e:
        print(f"Error searching in Word document {file_path}: {e}")
    return False # If any errors occur, it prints an error message and returns False.

def search_file_content(file_path, query): # search_file_content function determines the file type based on its extension. 
    if file_path.lower().endswith('.pdf'):
        return search_pdf(file_path, query)
    elif file_path.lower().endswith('.docx'):
        return search_word_document(file_path, query)
    else:
        print(f"File type not supported: {file_path}")
        return False

def search_files(directory, query): # search_files function takes a directory and a search query. 
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if search_file_content(file_path, query): # For each file, it calls search_file_content and appends the file path to the results list if the content matches the query.
                results.append(file_path) # Add the file path in the "result" variable.
    return results

def display_file_options(files):
    print("\nMatching Files:")
    for i, file_path in enumerate(files, start=1):
        print(f"{i}. {os.path.basename(file_path)}")

def open_and_display_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        content = ""
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            text = page.get_text("text")
            content += f"\nPage {page_num + 1} Content:\n{text}"
        return content
    except Exception as e:
        return f"Error reading PDF file {file_path}: {e}"

def open_and_display_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return f"\nFile Content:\n{content}"
    except Exception as e:
        return f"Error reading file {file_path}: {e}"

def open_and_display_file(file_path):
    if file_path.lower().endswith('.pdf'):
        return open_and_display_pdf(file_path)
    else:
        return open_and_display_text(file_path)

def display_file_options(files):
    print("\nMatching Files:")
    for i, file_path in enumerate(files, start=1):
        print(f"{i}. {os.path.basename(file_path)}")
        


# Example usage
search_query = input("Enter search query: ")
search_directory = r'D:\Mude\university application\university application木德\master'

found_files = search_files(search_directory, search_query)

if found_files:
    display_file_options(found_files)

    try:
        selected_index = int(input("\nEnter the number of the file to open and read: "))
        selected_file = found_files[selected_index - 1]
        content_to_display = open_and_display_file(selected_file)

        # Tkinter GUI
        root = tk.Tk()
        root.title("File Content Display")

        text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
        text_area.insert(tk.INSERT, content_to_display)
        text_area.pack(expand=True, fill='both')

        root.mainloop()
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid file number.")
else:
    print("\nNo matching files found.")