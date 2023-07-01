import socket

def scan_ports(target, start_port, end_port):
    print("Scanning ports on {}".format(target))
    for port in range(start_port, end_port+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print("[+] Port {} is open".format(port))
        sock.close()

def main():
    target = input("Enter target IP address or range (e.g. 192.168.0.1 or 192.168.0.1-10): ")
    if "-" in target:
        start_ip, end_ip = target.split("-")
        start_ip = ".".join(start_ip.split(".")[:-1]) + "." + start_ip.split(".")[-1]
        end_ip = ".".join(end_ip.split(".")[:-1]) + "." + end_ip.split(".")[-1]
        for i in range(int(start_ip.split(".")[-1]), int(end_ip.split(".")[-1])+1):
            scan_ports(start_ip.replace(start_ip.split(".")[-1], str(i)), 1, 1000)
    else:
        scan_ports(target, 1, 1000)

if __name__ == "__main__":
    main()