import socket
import subprocess
import os
import re

def icmp_ping_scan(ip_addr):
    command = ['ping', '-n', '1', '-w', '100', ip_addr]
    result = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result == 0:
        return True
    else:
        return False

def tcp_port_scan(ip_addr, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip_addr, port))
            if result == 0:
                return True
            else:
                return False
    except socket.error:
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

"""
def tcp_port_scan_all(ip_from, ip_to):
    results = []

    for i in range(int(ip_from.split('.')[3]), int(ip_to.split('.')[3])+1):
        ip_addr = ip_from.rsplit('.', 1)[0] + '.' + str(i)
        result = {"ip": ip_addr, "ports": []}

        for port in range(1, 1025):
            if tcp_port_scan(ip_addr, port):
                result["ports"].append({"protocol": "TCP", "port": port, "status": "open"})

        results.append(result)

    return results
"""

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

"""
def print_results(results):
    for result in results:
        print("IP address:", result["ip"])

        if "status" in result:
            print("Status:", result["status"])

        if "ports" in result and result["ports"]:
            print("Open ports:")
            for port in result["ports"]:
                print(" -", port["protocol"], "port", port["port"], "is", port["status"])

        if "mac" in result and result["mac"]:
            print("MAC address:", result["mac"])

        print()
"""

def print_results(results):
    header = ["IP address", "Status", "Open TCP Ports", "Open UDP Ports", "MAC Address"]
    table = []

    for result in results:
        row = [result["ip"], result.get("status", "-")]

        tcp_ports = [str(port["port"]) for port in result.get("ports", []) if port["protocol"] == "TCP"]
        tcp_ports_str = ", ".join(tcp_ports) if tcp_ports else "-"
        row.append(tcp_ports_str)

        udp_ports = [str(port["port"]) for port in result.get("ports", []) if port["protocol"] == "UDP"]
        udp_ports_str = ", ".join(udp_ports) if udp_ports else "-"
        row.append(udp_ports_str)

        row.append(result.get("mac", "-"))
        table.append(row)

    # Determine column widths
    col_widths = [max(len(str(row[i])) for row in table) for i in range(len(header))]

    # Print header
    print(" | ".join(header[i].ljust(col_widths[i]) for i in range(len(header))))
    print("-" * (sum(col_widths) + 3 * len(header) - 1))

    # Print rows
    for row in table:
        print(" | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))))

"""
def main():
    while True:
        ip_from = input("Enter the starting IP address: ")
        ip_to = input("Enter the ending IP address: ")
        command = input("Enter the command to run (icmp, tcp, udp, arp), or 'exit' to quit: ")

        if command == "exit":
            break

        if command == "icmp":
            results = icmp_ping_scan_all(ip_from, ip_to)
        elif command == "tcp":
            results = tcp_port_scan_all(ip_from, ip_to)
        elif command == "udp":
            results = udp_port_scan_all(ip_from, ip_to)
        elif command == "arp":
            results = arp_scan_all(ip_from, ip_to)
        else:
            print("Invalid command. Please try again.")
            continue

        print_results(results)

    
"""

def main():
    while True:
        ip_from = input("Enter the starting IP address: ")
        ip_to = input("Enter the ending IP address: ")
        #command = input("Enter the command to run (icmp, tcp, udp, arp, or all), or 'exit' to quit: ")
        command = input("Enter the command to run (icmp, udp, arp, or all), or 'exit' to quit: ")

        if command == "exit":
            break

        if command == "all":
            results = []
            results.extend(icmp_ping_scan_all(ip_from, ip_to))
            results.extend(udp_port_scan_all(ip_from, ip_to))
            results.extend(arp_scan_all(ip_from, ip_to))
        else:
            if command == "icmp":
                results = icmp_ping_scan_all(ip_from, ip_to)
            #elif command == "tcp":
                #results = tcp_port_scan_all(ip_from, ip_to)
            elif command == "udp":
                results = udp_port_scan_all(ip_from, ip_to)
            elif command == "arp":
                results = arp_scan_all(ip_from, ip_to)
            else:
                print("Invalid command. Please try again.")
                continue

        print_results(results)
        
        
if __name__ == '__main__':
    main()
