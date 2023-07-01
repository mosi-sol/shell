import subprocess
import socket
import struct
import sys
import tkinter as tk
from tkinter import ttk

class IPScannerGUI:
    def __init__(self, master):
        self.master = master
        master.title("IP Scanner")

        # Create input field for IP address or range
        self.ip_label = tk.Label(master, text="IP address or range:")
        self.ip_label.pack(side=tk.TOP, padx=10, pady=10)
        self.ip_entry = tk.Entry(master, width=30)
        self.ip_entry.pack(side=tk.TOP, padx=10, pady=10)

        # Create "Scan" button to start the scan
        self.scan_button = tk.Button(master, text="Scan", command=self.scan_ips)
        self.scan_button.pack(side=tk.TOP, padx=10, pady=10)

        # Create result window with scrollbar
        self.result_frame = tk.Frame(master)
        self.result_frame.pack(side=tk.TOP, padx=10, pady=10)
        self.result_scrollbar = ttk.Scrollbar(self.result_frame, orient=tk.VERTICAL)
        self.result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_listbox = tk.Listbox(self.result_frame, yscrollcommand=self.result_scrollbar.set)
        self.result_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.result_scrollbar.config(command=self.result_listbox.yview)

    def icmp_ping(self, ip):
        """
        Perform an ICMP ping on the given IP address and return True if the IP is reachable
        """
        try:
            ip = socket.gethostbyname(ip)
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            sock.settimeout(1)
            packet = struct.pack('!BBHHH', 8, 0, 0, 0, 0)
            checksum = self.calc_checksum(packet)
            packet = struct.pack('!BBHHH', 8, 0, checksum, 0, 0)
            sock.sendto(packet, (ip, 1))
            sock.recvfrom(1024)
            return True
        except:
            return False

    def arp_scan(self, ip):
        """
        Perform an ARP scan on the given IP address and return the MAC address
        """
        try:
            ip = socket.gethostbyname(ip)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((ip, 1))
            mac = sock.getsockname()[4]
            return ':'.join('%02x' % b for b in mac)
        except:
            return None

    def calc_checksum(self, data):
        """
        Calculate the checksum of the given data
        """
        if len(data) % 2:
            data += b'\x00'
        s = sum(struct.unpack('!H', data[i:i+2])[0] for i in range(0, len(data), 2))
        s = (s >> 16) + (s & 0xffff)
        s += s >> 16
        return ~s & 0xffff

    def scan(self, ip):
        """
        Perform a scan on the given IP address using both ARP and ICMP and return the results
        """
        clients = []
        if self.icmp_ping(ip):
            mac = self.arp_scan(ip)
            if mac:
                clients.append({'ip': ip, 'mac': mac, 'status': 'up'})
            else:
                clients.append({'ip': ip, 'status': 'up'})
        else:
            clients.append({'ip': ip, 'status': 'down'})
        return clients

    def scan_ips(self):
        """
        Scan the IPs in the given range and display the results in the result window
        """
        ip_range = self.ip_entry.get()
        ips = ip_range.split('-')
        start_ip = ips[0]
        if len(ips) > 1:
            end_ip = ips[1]
            ip = start_ip.split('.')
            ip_prefix = ip[0] + '.' + ip[1] + '.' + ip[2] + '.'
            start = int(ip[3])
            end = int(end_ip) + 1
        else:
            ip_prefix = start_ip.rsplit('.', 1)[0] + '.'
            start = int(start_ip.rsplit('.', 1)[1])
            end = start + 1
        for i in range(start, end):
            ip = ip_prefix + str(i)
            result = self.scan(ip)
            for r in result:
                if 'mac' in r:
                    self.result_listbox.insert(tk.END, f"{r['ip']}\t{r['mac']}\t{r['status']}")
                else:
                    self.result_listbox.insert(tk.END, f"{r['ip']}\t\t{r['status']}")

root = tk.Tk()
app = IPScannerGUI(root)
root.mainloop()