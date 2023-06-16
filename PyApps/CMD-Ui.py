import tkinter as tk
import subprocess

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Windows CMD App")
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)
        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        cmd_menu = tk.Menu(self.menu, tearoff=0)
        cmd_menu.add_command(label="dir", command=lambda: self.execute_command("dir"))
        cmd_menu.add_command(label="cd", command=lambda: self.execute_command("cd"))
        cmd_menu.add_command(label="md", command=lambda: self.execute_command("md"))
        cmd_menu.add_command(label="rd", command=lambda: self.execute_command("rd"))
        cmd_menu.add_command(label="copy", command=lambda: self.execute_command("copy"))
        cmd_menu.add_command(label="xcopy", command=lambda: self.execute_command("xcopy"))
        cmd_menu.add_command(label="del", command=lambda: self.execute_command("del"))
        cmd_menu.add_command(label="type", command=lambda: self.execute_command("type"))
        cmd_menu.add_command(label="rename", command=lambda: self.execute_command("rename"))
        cmd_menu.add_command(label="attrib", command=lambda: self.execute_command("attrib"))
        cmd_menu.add_command(label="ping", command=lambda: self.execute_command("ping"))
        cmd_menu.add_command(label="ipconfig", command=lambda: self.execute_command("ipconfig"))
        cmd_menu.add_command(label="netstat", command=lambda: self.execute_command("netstat"))
        cmd_menu.add_command(label="tasklist", command=lambda: self.execute_command("tasklist"))
        cmd_menu.add_command(label="taskkill", command=lambda: self.execute_command("taskkill"))
        cmd_menu.add_command(label="shutdown", command=lambda: self.execute_command("shutdown"))
        self.menu.add_cascade(label="CMD", menu=cmd_menu)

        theme_menu = tk.Menu(self.menu, tearoff=0)
        theme_menu.add_command(label="Dark", command=lambda: self.set_theme("dark"))
        theme_menu.add_command(label="Light", command=lambda: self.set_theme("light"))
        theme_menu.add_command(label="Blue", command=lambda: self.set_theme("blue"))
        theme_menu.add_command(label="Matrix", command=lambda: self.set_theme("matrix"))
        self.menu.add_cascade(label="Theme", menu=theme_menu)

    def create_widgets(self):
        self.cmd_panel = tk.Text(self.master, height=20, width=80, bg="black", fg="white")
        self.cmd_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(self.master)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.cmd_panel.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.cmd_panel.yview)

        self.cmd_panel.insert(tk.END, "> ")

        self.cmd_panel.bind("<Return>", self.on_enter_pressed)
        self.cmd_panel.bind("<Key>", self.disable_insert_mode)
        self.cmd_panel.bind("<BackSpace>", self.enable_insert_mode)

        self.cmd_panel.focus_set()

    def on_enter_pressed(self, event):
        cmd = self.cmd_panel.get("end-2c linestart", "end-2c lineend")
        self.execute_command(cmd)
        self.cmd_panel.insert(tk.END, "> ")

    def disable_insert_mode(self, event):
        if event.keysym == "Insert":
            return "break"

    def enable_insert_mode(self, event):
        if event.keysym == "Escape":
            return
        if self.cmd_panel.cget("state") != "normal":
            self.cmd_panel.configure(state="normal")
        self.cmd_panel.insert(tk.END, event.char)
        self.cmd_panel.configure(state="disabled")

    def execute_command(self, command):
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            self.cmd_panel.insert(tk.END, output.decode())
        except subprocess.CalledProcessError as e:
            self.cmd_panel.insert(tk.END, e.output.decode())

    def set_theme(self, theme):
        if theme == "dark":
            self.cmd_panel.configure(bg="black", fg="white")
        elif theme == "light":
            self.cmd_panel.configure(bg="white", fg="black")
        elif theme == "blue":
            self.cmd_panel.configure(bg="blue", fg="white")
        elif theme == "matrix":
            self.cmd_panel.configure(bg="black", fg="green")

root = tk.Tk()
app = Application(master=root)
app.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
app.mainloop()