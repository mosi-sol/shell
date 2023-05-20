import tkinter as tk
import json
from tkinter import ttk
from tkinter import Menu

# Create the main tkinter window
root = tk.Tk()
root.title("Sticky Notes")

# Load existing notes from the JSON file
try:
    with open("notes.json", "r") as f:
        notes = json.load(f)
except FileNotFoundError:
    notes = []

# Create a function to save notes to the JSON file
def save_notes():
    with open("notes.json", "w") as f:
        json.dump(notes, f)

# Create a function to add a new note
def add_note():
    # Create a new tkinter window for the note
    note_window = tk.Toplevel(root)
    note_window.title("New Note")

    # Create a label and text box for the note's title
    title_label = tk.Label(note_window, text="Title")
    title_label.pack()
    title_box = tk.Entry(note_window)
    title_box.pack()

    # Create a label and text box for the note's content
    content_label = tk.Label(note_window, text="Content")
    content_label.pack()
    content_box = tk.Text(note_window)
    content_box.pack()

    # Create a button to save the note and close the window
    save_button = tk.Button(note_window, text="Save", command=lambda: save_and_close())
    save_button.pack()

    # Create a function to save the note and close the window
    def save_and_close():
        # Add the note to the list of notes
        note = {"title": title_box.get().strip(), "content": content_box.get("1.0", tk.END).strip()}
        notes.append(note)

        # Save the notes to the JSON file
        save_notes()

        # Close the note window
        note_window.destroy()

# Create a function to display the list of notes
def display_notes():
    # Create a new tkinter window for the notes
    notes_window = tk.Toplevel(root)
    notes_window.title("Notes")

    # Create a table for the notes' contents
    table = ttk.Treeview(notes_window, columns=("Title", "Content"), show="headings")
    table.heading("Title", text="Title")
    table.heading("Content", text="Content")
    table.pack()

    # Add each note to the table
    for note in notes:
        table.insert("", tk.END, values=(note["title"], note["content"]))

    # Create a button to edit a selected note
    def edit_note():
        # Get the selected note from the table
        selected_note = table.item(table.selection())

        # Create a new tkinter window for the note
        note_window = tk.Toplevel(notes_window)
        note_window.title(selected_note["values"][0])

        # Create a label and text box for the note's title
        title_label = tk.Label(note_window, text="Title")
        title_label.pack()
        title_box = tk.Entry(note_window)
        title_box.pack()
        title_box.insert(tk.END, selected_note["values"][0])

        # Create a label and text box for the note's content
        content_label = tk.Label(note_window, text="Content")
        content_label.pack()
        content_box = tk.Text(note_window)
        content_box.pack()
        content_box.insert(tk.END, selected_note["values"][1])

        # Create a button to save the note and close the window
        save_button = tk.Button(note_window, text="Save", command=lambda: save_and_close())
        save_button.pack()

        # Create a function to save the note and close the window
        def save_and_close():
            # Update the selected note in the list of notes
            index = table.index(table.selection())
            note = {"title": title_box.get().strip(), "content": content_box.get("1.0", tk.END).strip()}
            notes[index] = note

            # Update the note in the table
            table.item(table.selection(), values=(note["title"], note["content"]))

            # Save the notes to the JSON file
            save_notes()

            # Close the note window
            note_window.destroy()

    edit_button = tk.Button(notes_window, text="Edit", command=edit_note)
    edit_button.pack()

    # Create a function to remove a selected note
    def remove_note():
        # Get the selected note from the table
        selected_note = table.item(table.selection())

        # Remove the selected note from the list of notes
        index = table.index(table.selection())
        del notes[index]

        # Remove the selected note from the table
        table.delete(table.selection())

        # Save the notes to the JSON file
        save_notes()

    remove_button = tk.Button(notes_window, text="Remove", command=remove_note)
    remove_button.pack()

    # Create a button to close the notes window
    close_button = tk.Button(notes_window, text="Close", command=lambda: notes_window.destroy())
    close_button.pack()

# Create a button to add a new note
add_button = tk.Button(root, text="New Note", command=add_note)
add_button.pack()

# Create a button to display the list of notes
display_button = tk.Button(root, text="Notes", command=display_notes)
display_button.pack()

# ===============
# handle the menu item
def new_note():
    add_note()

def show_notes():
    display_notes()

# Create a menu bar
menu_bar = tk.Menu(root)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New Note", command=new_note)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create an "Edit" menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Notes", command=show_notes)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Add the menu bar to the root window
root.config(menu=menu_bar)
# ===============

# Start the tkinter event loop
root.mainloop()
