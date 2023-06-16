import tkinter as tk
from tkinter import filedialog

class Editor:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Editor")
        
        # create the Text widget and pack it
        self.text = tk.Text(self.master, undo=True)
        self.text.pack(side='left', fill='both', expand=True)
        
        # create the Scrollbar widget and pack it
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.pack(side='right', fill='y')
        
        # configure the Text widget to use the Scrollbar widget
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)
        
        # create the menus and shortcuts
        self.create_menus()
        self.bind_shortcuts()
    
    def create_menus(self):
        menu_bar = tk.Menu(self.master)
        
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.text.edit_undo)
        edit_menu.add_command(label="Redo", command=self.text.edit_redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)
        
        theme_menu = tk.Menu(menu_bar, tearoff=0)
        theme_menu.add_radiobutton(label="Light", command=self.set_light_theme)
        theme_menu.add_radiobutton(label="Dark", command=self.set_dark_theme)
        theme_menu.add_radiobutton(label="Dark Blue", command=self.set_dark_blue_theme)
        theme_menu.add_radiobutton(label="Dark Gray", command=self.set_dark_gray_theme)
        theme_menu.add_radiobutton(label="Plastic Dark", command=self.set_plastic_dark_theme)
        
        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        menu_bar.add_cascade(label="Theme", menu=theme_menu)
        
        self.master.config(menu=menu_bar)
    
    def bind_shortcuts(self):
        self.master.bind('<Control-n>', lambda event: self.new_file())
        self.master.bind('<Control-o>', lambda event: self.open_file())
        self.master.bind('<Control-s>', lambda event: self.save_file())
        self.master.bind('<Control-z>', lambda event: self.text.edit_undo())
        self.master.bind('<Control-y>', lambda event: self.text.edit_redo())
        self.master.bind('<Control-x>', lambda event: self.cut())
        self.master.bind('<Control-c>', lambda event: self.copy())
        self.master.bind('<Control-v>', lambda event: self.paste())
    
    def new_file(self):
        self.text.delete('1.0', 'end')
        self.master.title("Python Editor")
    
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                file_content = file.read()
                self.text.delete('1.0', 'end')
                self.text.insert('1.0', file_content)
                self.master.title(f"{file_path} - Python Editor")
    
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text.get('1.0', 'end'))
                self.master.title(f"{file_path} - Python Editor")
    
    def cut(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.text.selection_get())
        self.text.delete('sel.first', 'sel.last')
    
    def copy(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.text.selection_get())
    
    def paste(self):
        self.text.insert('insert', self.master.clipboard_get())
    
    def set_light_theme(self):
        self.text.config(bg='white', fg='black')
    
    def set_dark_theme(self):
        self.text.config(bg='black', fg='white')
    
    def set_dark_blue_theme(self):
        self.text.config(bg='#222244', fg='white')
    
    def set_dark_gray_theme(self):
        self.text.config(bg='#444444', fg='white')
    
    def set_plastic_dark_theme(self):
        self.text.config(bg='#2B2B2B', fg='white')


if __name__ == '__main__':
    root = tk.Tk()
    editor = Editor(root)
    root.mainloop()