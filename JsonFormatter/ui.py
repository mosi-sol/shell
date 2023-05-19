#  { "name": "John", "age": 30, "city": "New York", "name": "John", "age": 30, "city": "New York" }
import json
import tkinter as tk
from tkinter import filedialog

class JSONFormatterGUI:
    def __init__(self, master):
        self.master = master
        master.title("JSON Formatter")

        # Create widgets
        self.input_label = tk.Label(master, text="Enter JSON data:")
        self.input_text = tk.Text(master, width=50, height=10)
        self.output_label = tk.Label(master, text="Formatted JSON:")
        self.output_text = tk.Text(master, width=50, height=10)
        self.save_button = tk.Button(master, text="Save", command=self.save_file)

        # Position widgets
        self.input_label.grid(row=0, column=0, padx=10, pady=10)
        self.input_text.grid(row=1, column=0, padx=10, pady=10)
        self.output_label.grid(row=0, column=1, padx=10, pady=10)
        self.output_text.grid(row=1, column=1, padx=10, pady=10)
        self.save_button.grid(row=2, column=1, pady=10)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json")
        if file_path:
            with open(file_path,"w") as file:
                file.write(self.output_text.get("1.0", "end-1c"))

    def format_json(self):
        try:
            json_data = json.loads(self.input_text.get("1.0", "end-1c"))
            formatted_json = json.dumps(json_data, indent=4)
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", formatted_json)
        except ValueError as e:
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", f"Error: {e}")

root = tk.Tk()
app = JSONFormatterGUI(root)

# Bind the format_json method to the input text widget so that
# it is called whenever the user types in new JSON data
app.input_text.bind("<KeyRelease>", lambda event: app.format_json())

root.mainloop()