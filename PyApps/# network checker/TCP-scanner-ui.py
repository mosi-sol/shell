import ipaddress
import socket
import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("IP Scanner")

        # create IP range label and entry
        self.ip_label = tk.Label(self.master, text="IP range (e.g. 192.168.1.1/24):")
        self.ip_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.ip_entry = tk.Entry(self.master, width=30)
        self.ip_entry.grid(row=0, column=1, padx=5, pady=5)

        # create port range label and entry
        self.port_label = tk.Label(self.master, text="Port range (e.g. 1-1024):")
        self.port_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.port_entry = tk.Entry(self.master, width=30)
        self.port_entry.grid(row=1, column=1, padx=5, pady=5)

        # create scan button
        self.scan_button = tk.Button(self.master, text="Scan", command=self.scan)
        self.scan_button.grid(row=2, column=1, padx=5, pady=5)

        # create results label and text box
        self.results_label = tk.Label(self.master, text="Results:")
        self.results_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.results_text = tk.Text(self.master, width=60, height=20)
        self.results_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # create vertical scrollbar for results text box
        self.results_scrollbar = tk.Scrollbar(self.master, orient=tk.VERTICAL, command=self.results_text.yview)
        self.results_scrollbar.grid(row=4, column=1, sticky="ns")
        self.results_text.config(yscrollcommand=self.results_scrollbar.set)

    def scan(self):
        # get IP and port ranges from entries
        ip_range = self.ip_entry.get().strip()
        port_range = self.port_entry.get().strip()

        # parse the IP range into a network address and a list of hosts
        network = ipaddress.ip_network(ip_range, strict=False)
        hosts = list(network.hosts())

        # parse the port range into start and end ports
        if '-' in port_range:
            port_start, port_end = map(int, port_range.split('-'))
        else:
            port_start = int(port_range)
            port_end = int(port_range)

        # create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # clear the results text box
        self.results_text.delete("1.0", tk.END)

        # loop over IP addresses and port numbers
        for host in hosts:
            address = str(host)

            for port in range(port_start, port_end+1):
                # construct the IP address and port number
                server_address = (address, port)

                # attempt a TCP connection
                try:
                    s.connect(server_address)
                    result = f'{address:<20} {"Port "+str(port):<10} {"Open":<10}\n'
                    self.results_text.insert(tk.END, result)
                except:
                    result = f'{address:<20} {"Port "+str(port):<10} {"Closed":<10}\n'
                    self.results_text.insert(tk.END, result)

                s.close()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)

# create the main window
root = tk.Tk()

# create the app
app = App(root)

# run the app
root.mainloop()