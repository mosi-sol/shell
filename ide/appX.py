import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText


class TextEditor:
    THEMES = {
        "white": {"bg": "white", "fg": "black", "ln_bg": "lightgray", "ln_fg": "black"},
        "light": {"bg": "#F7F7F7", "fg": "black", "ln_bg": "#E0E0E0", "ln_fg": "black"},
        "black": {"bg": "black", "fg": "white", "ln_bg": "gray", "ln_fg": "white"},
        "dark": {"bg": "#1E1E1E", "fg": "white", "ln_bg": "#3E3E3E", "ln_fg": "white"},
        "darkblue": {"bg": "#2A3B4C", "fg": "white", "ln_bg": "#4A5B6C", "ln_fg": "white"}
    }

    def __init__(self, master):
        self.master = master
        self.master.title("Text Editor")

        self.text = ScrolledText(self.master, wrap='word', font=('Consolas', 12))
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.add_menu()

        self.linenumbers = tk.Text(self.master, width=4, padx=3, takefocus=0, border=0, background=self.THEMES["light"]["ln_bg"], foreground=self.THEMES["light"]["ln_fg"], state='disabled', wrap='none')
        self.linenumbers.pack(side=tk.LEFT, fill=tk.Y)

        self.text.bind('<Key>', self.on_key)
        self.text.bind('<Button-1>', self.on_click)

        self.update_linenumbers()

    def add_menu(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)
        file_menu.add_command(label="Open...", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        file_menu.add_command(label="Save As...", accelerator="Ctrl+Shift+S", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator="Alt+F4", command=self.exit_app)

        edit_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=self.text.edit_undo)
        edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", command=self.text.edit_redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=self.cut)
        edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=self.copy)
        edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=self.paste)
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", accelerator="Ctrl+A", command=self.select_all)

        format_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Format", menu=format_menu)
        format_menu.add_checkbutton(label="Word Wrap", variable=self.text['wrap'], onvalue='word', offvalue='none', command=self.update_linenumbers)

        view_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Line Numbers", accelerator="Ctrl+L", command=self.toggle_linenumbers)

        theme_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Themes", menu=theme_menu)
        self.master.theme = tk.StringVar(value="light")
        for theme in self.THEMES:
            theme_menu.add_radiobutton(label=theme.capitalize(), variable=self.master.theme, value=theme, command=self.change_theme)

        help_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.about)

    def new_file(self, event=None):
        self.text.delete('1.0', tk.END)
        self.master.title("Text Editor - Untitled")

    def open_file(self, event=None):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                self.text.delete('1.0', tk.END)
                self.text.insert(tk.END, file.read())
            self.update_linenumbers()
            self.master.title("Text Editor - " + file_path)

    def save_file(self, event=None):
        if 'Untitled' in self.master.title():
            self.save_file_as()
        else:
            with open(self.master.title().replace("Text Editor - ", ""), 'w') as file:
                file.write(self.text.get('1.0', tk.END))

    def save_file_as(self, event=None):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text.get('1.0', tk.END))
            self.master.title("Text Editor - " + file_path)

    def exit_app(self, event=None):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.master.destroy()

    def update_linenumbers(self, event=None):
        if self.text['wrap'] == 'none':
            self.linenumbers.config(state='normal')
            self.linenumbers.delete('1.0', tk.END)
            line_count = self.text.get('1.0', tk.END).count('\n') + 1
            for i in range(1, line_count):
                self.linenumbers.insert(tk.END, str(i) + '\n')
            self.linenumbers.config(state='disabled')
        else:
            self.linenumbers.pack_forget()

    def toggle_linenumbers(self, event=None):
        if self.linenumbers.winfo_ismapped():
            self.linenumbers.pack_forget()
        else:
            self.update_linenumbers()

    def cut(self, event=None):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.text.selection_get())
        self.text.delete(tk.SEL_FIRST, tk.SEL_LAST)

    def copy(self, event=None):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.text.selection_get())

    def paste(self, event=None):
        self.text.insert(tk.INSERT, self.master.clipboard_get())

    def select_all(self, event=None):
        self.text.tag_add(tk.SEL, '1.0', tk.END)
        self.text.mark_set(tk.INSERT, '1.0')
        self.text.see(tk.INSERT)
        return 'break'

    def change_theme(self, event=None):
        theme = self.THEMES[self.master.theme.get()]
        self.text.config(background=theme["bg"], foreground=theme["fg"])
        self.linenumbers.config(background=theme["ln_bg"], foreground=theme["ln_fg"])

    def on_key(self, event=None):
        self.update_linenumbers()

    def on_click(self, event=None):
        self.update_linenumbers()

    def about(self, event=None):
        messagebox.showinfo("About", "Mosi ide\n\nA Mosi IDE, ver 1.0.1")


if __name__ == '__main__':
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()