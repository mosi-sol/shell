import socket
import tkinter as tk
from tkinter import ttk

def scan_ports(ip_address, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def scan_ips():
    target = ip_entry.get()
    port_or_range = port_entry.get()
    if "-" in port_or_range:
        start_port, end_port = [int(x) for x in port_or_range.split("-")]
    else:
        try:
            start_port = end_port = int(port_or_range)
        except ValueError:
            result_listbox.insert(tk.END, "Error: invalid port or port range")
            return
    if "-" in target:
        start_ip, end_ip = target.split("-")
        start_ip = ".".join(start_ip.split(".")[:-1]) + "." + start_ip.split(".")[-1]
        end_ip = ".".join(end_ip.split(".")[:-1]) + "." + end_ip.split(".")[-1]
        for i in range(int(start_ip.split(".")[-1]), int(end_ip.split(".")[-1])+1):
            ip_address = start_ip.replace(start_ip.split(".")[-1], str(i))
            open_ports = scan_ports(ip_address, start_port, end_port)
            if open_ports:
                result_listbox.insert(tk.END, "Open ports on {}: {}".format(ip_address, ", ".join([str(port) for port in open_ports])))
    else:
        open_ports = scan_ports(target, start_port, end_port)
        if open_ports:
            result_listbox.insert(tk.END, "Open ports on {}: {}".format(target, ", ".join([str(port) for port in open_ports])))
        else:
            result_listbox.insert(tk.END, "No open ports found on {}".format(target))

# Create GUI
root = tk.Tk()
root.title("IP Scanner")

# Create frames
input_frame = ttk.Frame(root)
result_frame = ttk.Frame(root)

# Add widgets to input frame
ip_label = ttk.Label(input_frame, text="Enter target IP address or range (e.g. 192.168.0.1 or 192.168.0.1-10):")
ip_entry = ttk.Entry(input_frame)
port_label = ttk.Label(input_frame, text="Enter target port or port range (e.g. 80 or 1-100):")
port_entry = ttk.Entry(input_frame)
scan_button = ttk.Button(input_frame, text="Scan", command=scan_ips)

ip_label.pack(side="left", padx=5, pady=5)
ip_entry.pack(side="left", padx=5, pady=5)
port_label.pack(side="left", padx=5, pady=5)
port_entry.pack(side="left", padx=5, pady=5)
scan_button.pack(side="left", padx=5, pady=5)

# Add widgets to result frame
result_label = ttk.Label(result_frame, text="Scan results:")
result_label.pack(side="top", padx=5, pady=5)

result_scrollbar = ttk.Scrollbar(result_frame, orient="vertical")
result_listbox = tk.Listbox(result_frame, yscrollcommand=result_scrollbar.set)
result_scrollbar.config(command=result_listbox.yview)
result_scrollbar.pack(side="right", fill="y")

result_listbox.pack(side="left", fill="both", expand=True, padx=5, pady=5)

# Pack frames into root
input_frame.pack(side="top", fill="x", padx=5, pady=5)
result_frame.pack(side="bottom", fill="both", expand=True, padx=5, pady=5)

root.mainloop()