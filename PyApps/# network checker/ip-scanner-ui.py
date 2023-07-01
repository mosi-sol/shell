import socket
import subprocess
import os
import re
import tkinter as tk
from tkinter import ttk

def icmp_ping_scan(ip_addr):
    command = ['ping', '-n', '1', '-w', '100', ip_addr]
    result = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result == 0:
        return True
    else:
        return False

def udp_port_scan(ip_addr, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)
    result = sock.sendto(b'', (ip_addr, port))
    if result:
        return True
    else:
        return False

def arp_scan(ip_addr):
    cmd = 'arp -a ' + ip_addr
    result = os.popen(cmd).read()
    match = re.search(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', result)
    if match:
        return match.group(0)
    else:
        return None

def icmp_ping_scan_all(ip_from, ip_to):
    results = []

    for i in range(int(ip_from.split('.')[3]), int(ip_to.split('.')[3])+1):
        ip_addr = ip_from.rsplit('.', 1)[0] + '.' + str(i)
        result = {"ip": ip_addr, "status": None}

        if icmp_ping_scan(ip_addr):
            result["status"] = "live"

        results.append(result)

    return results

def udp_port_scan_all(ip_from, ip_to):
    results = []

    for i in range(int(ip_from.split('.')[3]), int(ip_to.split('.')[3])+1):
        ip_addr = ip_from.rsplit('.', 1)[0] + '.' + str(i)
        result = {"ip": ip_addr, "ports": []}

        for port in range(1, 1025):
            if udp_port_scan(ip_addr, port):
                result["ports"].append({"protocol": "UDP", "port": port, "status": "open"})

        results.append(result)

    return results

def arp_scan_all(ip_from, ip_to):
    results = []

    for i in range(int(ip_from.split('.')[3]), int(ip_to.split('.')[3])+1):
        ip_addr = ip_from.rsplit('.', 1)[0] + '.' + str(i)
        result = {"ip": ip_addr, "mac": None}

        mac_addr = arp_scan(ip_addr)
        if mac_addr:
            result["mac"] = mac_addr

        results.append(result)

    return results

def print_results(results, treeview):
    for i in treeview.get_children():
        treeview.delete(i)

    for result in results:
        ip = result["ip"]
        status = result.get("status", "-")
        udp_ports = ", ".join(str(port["port"]) for port in result.get("ports", []) if port["protocol"] == "UDP")
        mac_addr = result.get("mac", "-")
        treeview.insert("", tk.END, values=(ip, status, udp_ports, mac_addr))

def run_scan(ip_from, ip_to, command, treeview):
    if command == "icmp":
        results = icmp_ping_scan_all(ip_from, ip_to)
    elif command == "udp":
        results = udp_port_scan_all(ip_from, ip_to)
    elif command == "arp":
        results = arp_scan_all(ip_from, ip_to)
    elif command == "all":
        results = []
        results.extend(icmp_ping_scan_all(ip_from, ip_to))
        results.extend(udp_port_scan_all(ip_from, ip_to))
        results.extend(arp_scan_all(ip_from, ip_to))
    else:
        print("Invalid command. Please try again.")
        return

    print_results(results, treeview)

"""

def main():
    root = tk.Tk()
    root.title("IP Scanner")

    # Create input fields
    ip_from_label = ttk.Label(root, text="Starting IP address:")
    ip_from_label.grid(row=0, column=0, padx=5, pady=5)
    ip_from_entry = ttk.Entry(root)
    ip_from_entry.grid(row=0, column=1, padx=5, pady=5)

    ip_to_label = ttk.Label(root, text="Ending IP address:")
    ip_to_label.grid(row=1, column=0, padx=5, pady=5)
    ip_to_entry = ttk.Entry(root)
    ip_to_entry.grid(row=1, column=1, padx=5, pady=5)

    command_label = ttk.Label(root, text="Command:")
    command_label.grid(row=2, column=0, padx=5, pady=5)
    command_options = ["icmp", "udp", "arp", "all"]
    command_combobox = ttk.Combobox(root, values=command_options)
    command_combobox.grid(row=2, column=1, padx=5, pady=5)

    # Create button to run scan
    run_button = ttk.Button(root, text="Run Scan", command=lambda: run_scan(ip_from_entry.get(), ip_to_entry.get(), command_combobox.get(), treeview))
    run_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    # Create treeview to display results
    treeview = ttk.Treeview(root, columns=("status", "udp_ports", "mac_addr"), show="headings")
    treeview.heading("status", text="Status")
    treeview.heading("udp_ports", text="Open UDP Ports")
    treeview.heading("mac_addr", text="MAC Address")
    treeview.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()

"""


def main():
    root = tk.Tk()
    root.title("IP Scanner")

    # Create input fields
    ip_from_label = ttk.Label(root, text="Starting IP address:")
    ip_from_label.grid(row=0, column=0, padx=5, pady=5)
    ip_from_entry = ttk.Entry(root)
    ip_from_entry.grid(row=0, column=1, padx=5, pady=5)

    ip_to_label = ttk.Label(root, text="Ending IP address:")
    ip_to_label.grid(row=1, column=0, padx=5, pady=5)
    ip_to_entry = ttk.Entry(root)
    ip_to_entry.grid(row=1, column=1, padx=5, pady=5)

    command_label = ttk.Label(root, text="Command:")
    command_label.grid(row=2, column=0, padx=5, pady=5)
    command_options = ["icmp", "udp", "arp", "all"]
    command_combobox = ttk.Combobox(root, values=command_options)
    command_combobox.grid(row=2, column=1, padx=5, pady=5)

    # Create button to run scan
    run_button = ttk.Button(root, text="Run Scan", command=lambda: run_scan(ip_from_entry.get(), ip_to_entry.get(), command_combobox.get(), treeview))
    run_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    # Create treeview to display results
    treeview_frame = ttk.Frame(root)
    treeview_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    treeview_scrollbar = ttk.Scrollbar(treeview_frame)
    treeview_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    treeview = ttk.Treeview(treeview_frame, columns=("status", "udp_ports", "mac_addr"), show="headings", yscrollcommand=treeview_scrollbar.set)
    treeview.heading("status", text="Status")
    treeview.heading("udp_ports", text="Open UDP Ports")
    treeview.heading("mac_addr", text="MAC Address")
    treeview.pack(side=tk.LEFT)

    treeview_scrollbar.config(command=treeview.yview)

    root.mainloop()
    
if __name__ == "__main__":
    main()