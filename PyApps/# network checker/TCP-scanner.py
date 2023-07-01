import ipaddress
import socket

# get user input for IP range and port range
ip_range = input("Enter IP range to scan (e.g. 192.168.1.1/24): ")
port_range = input("Enter port range to scan (e.g. 1-1024): ")

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

# print table header
print(f'{"IP Address":^20}', end='')
for port in range(port_start, port_end+1):
    print(f'{"Port "+str(port):^10}', end='')
print()

# loop over IP addresses and port numbers
for host in hosts:
    address = str(host)
    print(f'{address:<20}', end='')

    for port in range(port_start, port_end+1):
        # construct the IP address and port number
        server_address = (address, port)

        # attempt a TCP connection
        try:
            s.connect(server_address)
            print(f'{str("Open"):^10}', end='')
        except:
            print(f'{str("Closed"):^10}', end='')

        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

    print()