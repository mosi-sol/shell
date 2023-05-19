import tkinter as tk
import json

# Define the list of pitch deck section titles
pitch_deck_titles = [
    "Cover page",
    "Problem",
    "Solution",
    "Market size",
    "Business model",
    "Marketing and sales strategy",
    "Management team",
    "Financial projections",
    "Funding requirements",
    "Competition",
    "Milestones",
    "Appendix"
]

class PitchDeckApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Pitch Deck App")
        self.create_widgets()

    def create_widgets(self):
        # Create label and text entry widgets for each pitch deck section
        self.section_entries = {}
        for i, title in enumerate(pitch_deck_titles):
            label = tk.Label(self.master, text=title)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
            entry = tk.Entry(self.master, width=50)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            self.section_entries[title] = entry

        # Create a button to save the pitch deck information
        button = tk.Button(self.master, text="Save", command=self.save_info)
        button.grid(row=len(pitch_deck_titles)+1, column=0, columnspan=2, padx=5, pady=10)

    def save_info(self):
        # Get the user input for each pitch deck section
        pitch_deck_info = {}
        for title, entry in self.section_entries.items():
            pitch_deck_info[title] = entry.get()

        # Save the pitch deck information to a JSON file
        with open("pitch_deck_info.json", "w") as f:
            json.dump(pitch_deck_info, f)

        # Clear the text entry widgets
        for entry in self.section_entries.values():
            entry.delete(0, tk.END)

        # Show a message box to confirm that the information has been saved
        tk.messagebox.showinfo("Pitch Deck App", "Pitch deck information has been saved.")

root = tk.Tk()
app = PitchDeckApp(master=root)
app.mainloop()