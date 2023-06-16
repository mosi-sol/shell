import tkinter as tk
from tkinter import scrolledtext
import subprocess

# Define a dark color scheme
DARK_BG = "#1a1a1a"
LIGHT_TEXT = "#f2f2f2"
DARK_TEXT = "#bfbfbf"

root = tk.Tk()
root.title("Windows Network Commands")
root.config(bg=DARK_BG)

# Function to execute network command
def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = result.stdout.decode('utf-8') + result.stderr.decode('utf-8')
    return output

# Function to display network command output
def display_output(command):
    output = run_command(command)
    output_box.delete('1.0', tk.END)
    output_box.insert(tk.END, output)

# Create a label for the network commands
label = tk.Label(root, text="Network Commands", font=("Arial", 16), fg=LIGHT_TEXT, bg=DARK_BG)
label.pack(pady=10)

# Create a scrolled text box for the output
output_box = scrolledtext.ScrolledText(root, width=60, height=10, wrap=tk.WORD, bg=DARK_BG, fg=LIGHT_TEXT)
output_box.pack(padx=10, pady=10)

# Create a frame for the buttons
button_frame = tk.Frame(root, bg=DARK_BG)
button_frame.pack(padx=10, pady=10)

# Create buttons for each network command
ipconfig_button = tk.Button(button_frame, text="ipconfig", width=15, command=lambda: display_output("ipconfig"), bg=DARK_BG, fg=LIGHT_TEXT, activebackground=DARK_BG, activeforeground=LIGHT_TEXT)
ipconfig_button.pack(pady=5)

ping_button = tk.Button(button_frame, text="ping", width=15, command=lambda: display_output("ping google.com"), bg=DARK_BG, fg=LIGHT_TEXT, activebackground=DARK_BG, activeforeground=LIGHT_TEXT)
ping_button.pack(pady=5)

nslookup_button = tk.Button(button_frame, text="nslookup", width=15, command=lambda: display_output("nslookup google.com"), bg=DARK_BG, fg=LIGHT_TEXT, activebackground=DARK_BG, activeforeground=LIGHT_TEXT)
nslookup_button.pack(pady=5)

tracert_button = tk.Button(button_frame, text="tracert", width=15, command=lambda: display_output("tracert google.com"), bg=DARK_BG, fg=LIGHT_TEXT, activebackground=DARK_BG, activeforeground=LIGHT_TEXT)
tracert_button.pack(pady=5)

netstat_button = tk.Button(button_frame, text="netstat", width=15, command=lambda: display_output("netstat -ano"), bg=DARK_BG, fg=LIGHT_TEXT, activebackground=DARK_BG, activeforeground=LIGHT_TEXT)
netstat_button.pack(pady=5)

# Run the main loop
root.mainloop()