# data/data.py

def read_notes():
    # Open and read the notes.txt file inside the 'data' folder
    with open("data/medical_book.txt", "r") as file:
        notes_content = file.read()
    return notes_content
read_notes()