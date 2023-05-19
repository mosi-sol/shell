import json
import tkinter as tk

# Define the list of titles
titles = [
    "Startup name",
    "Startup industry",
    "Executive Summary",
    "Problem and Solution",
    "Market Analysis",
    "Target Market and Customer Segments",
    "Marketing and Sales Plan",
    "Product or Service Description",
    "Business Model",
    "Team and Management Structure",
    "Financial Plan and Projections",
    "Funding Needs and Use of Funds",
    "Milestones and Timeline",
    "Roadmap"
]

class BusinessPlanUI:
    def __init__(self, master):
        self.master = master
        master.title("Business Plan")

        # Create a label and entry widget for each title
        self.entries = {}
        for i, title in enumerate(titles):
            label = tk.Label(master, text=title)
            label.grid(row=i, column=0, padx=10, pady=10)
            entry = tk.Entry(master, width=50)
            entry.grid(row=i, column=1, padx=10, pady=10)
            self.entries[title] = entry

        # Create a button to save the input to a JSON file
        save_button = tk.Button(master, text="Save", command=self.save)
        save_button.grid(row=len(titles), column=0, columnspan=2, padx=10, pady=10)

    def save(self):
        # Get the input for each title and store it in a dictionary
        info = {}
        for title, entry in self.entries.items():
            info[title] = entry.get()

        # Save the input to a JSON file
        with open("business_plan.json", "w") as f:
            json.dump(info, f)

        # Display a message to confirm that the input has been saved
        tk.messagebox.showinfo("Success", "Business plan information has been saved to business_plan.json")

# Create the main window and run the UI
root = tk.Tk()
app = BusinessPlanUI(root)
root.mainloop()