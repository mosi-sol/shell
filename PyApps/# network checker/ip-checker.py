import subprocess
import socket
import struct
import sys

def icmp_ping(ip):
    """
    Perform an ICMP ping on the given IP address and return True if the IP is reachable
    """
    try:
        ip = socket.gethostbyname(ip)
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        sock.settimeout(1)
        packet = struct.pack('!BBHHH', 8, 0, 0, 0, 0)
        checksum = calc_checksum(packet)
        packet = struct.pack('!BBHHH', 8, 0, checksum, 0, 0)
        sock.sendto(packet, (ip, 1))
        sock.recvfrom(1024)
        return True
    except:
        return False

def arp_scan(ip):
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

def calc_checksum(data):
    """
    Calculate the checksum of the given data
    """
    if len(data) % 2:
        data += b'\x00'
    s = sum(struct.unpack('!H', data[i:i+2])[0] for i in range(0, len(data), 2))
    s = (s >> 16) + (s & 0xffff)
    s += s >> 16
    return ~s & 0xffff

def scan(ip):
    """
    Perform a scan on the given IP address using both ARP and ICMP and return the results
    """
    clients = []
    if icmp_ping(ip):
        mac = arp_scan(ip)
        if mac:
            clients.append({'ip': ip, 'mac': mac, 'status': 'up'})
        else:
            clients.append({'ip': ip, 'status': 'up'})
    else:
        clients.append({'ip': ip, 'status': 'down'})
    return clients

def main():
    """
    Ask the user for an IP address or IP range, scan the IPs, and ask if the user wants to scan again
    """
    while True:
        ip_range = input("Enter IP address or IP range to scan (e.g. 192.168.0.1 or 192.168.0.1-10): ")
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
            result = scan(ip)
            for r in result:
                if 'mac' in r:
                    print(f"{r['ip']}\t{r['mac']}\t{r['status']}")
                else:
                    print(f"{r['ip']}\t\t{r['status']}")
        choice = input("Do you want to scan another IP address or range? (y/n): ")
        if choice.lower() == 'n':
            break

if __name__ == '__main__':
    main()