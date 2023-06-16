import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog


class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("WYSIWYG Text Editor")
        self.root.geometry("800x600")

        # Create a toolbar frame
        self.toolbar = ttk.Frame(self.root, padding=(5, 2, 5, 2))
        self.toolbar.pack(side="top", fill="x")

        # Create toolbar buttons
        self.bold_button = ttk.Button(self.toolbar, text="B", command=self.toggle_bold)
        self.bold_button.pack(side="left", padx=(0, 5))

        self.italic_button = ttk.Button(self.toolbar, text="I", command=self.toggle_italic)
        self.italic_button.pack(side="left", padx=(0, 5))

        self.underline_button = ttk.Button(self.toolbar, text="U", command=self.toggle_underline)
        self.underline_button.pack(side="left", padx=(0, 5))

        self.link_button = ttk.Button(self.toolbar, text="Link", command=self.insert_link)
        self.link_button.pack(side="left", padx=(0, 5))

        self.font_size_var = tk.StringVar()
        self.font_size_var.set("12")
        self.font_size_menu = ttk.OptionMenu(self.toolbar, self.font_size_var, "10", "12", "16", "20", "24", "32", command=self.change_font_size)
        self.font_size_menu.pack(side="left", padx=(0, 5))

        # Create the text editor
        self.text = tk.Text(self.root, font=("Helvetica", 12))
        self.text.pack(fill="both", expand=True)

        # Configure the text widget to support rich text
        self.text.tag_configure("bold", font=("Helvetica", 12, "bold"))
        self.text.tag_configure("italic", font=("Helvetica", 12, "italic"))
        self.text.tag_configure("underline", font=("Helvetica", 12, "underline"))
        self.text.tag_configure("link", font=("Helvetica", 12, "underline"), foreground="blue")

        # Create the menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Create the file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit)

    def toggle_bold(self):
        self.toggle_tag("bold")

    def toggle_italic(self):
        self.toggle_tag("italic")

    def toggle_underline(self):
        self.toggle_tag("underline")

    def toggle_tag(self, tag):
        # Get the current selection
        sel_start = self.text.index("sel.first")
        sel_end = self.text.index("sel.last")

        # If there is no selection, apply the tag to the whole text widget
        if not sel_start or not sel_end:
            sel_start = "1.0"
            sel_end = "end"

        # Toggle the tag
        if tag in self.text.tag_names(sel_start):
            self.text.tag_remove(tag, sel_start, sel_end)
        else:
            self.text.tag_add(tag, sel_start, sel_end)

    def insert_link(self):
        # Get the current selection
        sel_start = self.text.index("sel.first")
        sel_end = self.text.index("sel.last")

        # If there is no selection, prompt the user for a URL
        if not sel_start or not sel_end:
            url = tk.simpledialog.askstring("Insert Link", "Enter URL:")
            if url:
                self.text.insert("insert", url, ("link", url))
        else:
            url = tk.simpledialog.askstring("Insert Link", "Enter URL:")
            if url:
                self.text.tag_add("link", sel_start, sel_end)
                self.text.tag_config("link", foreground="blue", underline=1)
                self.text.tag_bind("link", "<Button-1>", lambda event, u=url: self.open_link(u))

    def open_link(self, url):
        import webbrowser
        webbrowser.open(url)

    def change_font_size(self, size):
        self.text.configure(font=("Helvetica", int(size)))

    def new_file(self):
        #Continued code:

        # Clear the text widget
        self.text.delete("1.0", "end")

    def open_file(self):
        # Ask the user for a file to open
        file_path = filedialog.askopenfilename()

        if file_path:
            # Open the file and insert its contents into the text widget
            with open(file_path, "r") as f:
                self.text.delete("1.0", "end")
                self.text.insert("1.0", f.read())

    def save_file(self):
        # Save the contents of the text widget to the current file
        if self.file_path:
            with open(self.file_path, "w") as f:
                f.write(self.text.get("1.0", "end-1c"))
        else:
            self.save_file_as()

    def save_file_as(self):
        # Ask the user for a file name and save the contents of the text widget to that file
        file_path = filedialog.asksaveasfilename()

        if file_path:
            self.file_path = file_path
            with open(file_path, "w") as f:
                f.write(self.text.get("1.0", "end-1c"))

    def exit(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    editor.run()