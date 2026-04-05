\import socket
from datetime import datetime
import threading
import argparse # to accept flags (uk just like cli tool)
from colorama import Fore, Style, init
init()

"""
Implemented Features: 
1. Open/ closed
2. Banner Grabbing
3. Accept Port Ranges
4. Using Multithreading, to make it fast
4. Acting like a CLI tool
"""

OPEN_COLOR = Fore.GREEN
CLOSED_COLOR = Fore.RED
FILTERED_COLOR = Fore.YELLOW
RESET = Style.RESET_ALL

# Target input
parser = argparse.ArgumentParser(description="Mini Nmap Scanner") # Understands the CLI input

parser.add_argument("-t", "--target", required=True, help="Target IP or domain")
parser.add_argument("-p", "--ports", default="1-100", help="Port range (e.g. 1-1000)")
parser.add_argument("-s", "--scan", default="T", help="Scan type: T (TCP) or U (UDP)")

args = parser.parse_args() #taking what user typed and organizing it

target = args.target
scan_type = args.scan.upper()

# Resolve domain to IP
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname")
    exit()



print(f"\nStarting mock Nmap scan on {target_ip}")
print("-" * 50)

# Start time
start_time = datetime.now()

# Common services
services = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NETBIOS",
    143: "IMAP",
    443: "HTTPS"
}
# given arg scanning
port_range = args.ports.split("-")
start_port = int(port_range[0])
end_port = int(port_range[1])
ports = range(start_port, end_port + 1)
open_ports = []

print("PORT     STATE   SERVICE     BANNER")
print("-" * 50)

if scan_type not in ["T", "U"]:
        print("Invalid scan type. Use T (TCP) or U (UDP)")
        exit()

# Scanning a given port on a target
def scan_port(port):
    service = services.get(port, "Unknown")
    #Resolving using TCP and UDP Scan

    if scan_type == "T":
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.settimeout(1)
    if scan_type == "T":
        result = s.connect_ex((target_ip, port))
        if result == 0: #0 means connected successfully
            try:
                if port == 80:
                    s.send(f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n".encode())
                else:
                    s.send(b"Hello\r\n") # b is used to convert it to bytes

                response = s.recv(1024).decode(errors="ignore")
                banner = response.split("\n")[0] #extract only first line
            except:
                banner = "No banner"

            print(f"{port}/tcp   {OPEN_COLOR}OPEN{RESET}    {service}   {banner}")
            open_ports.append(port)
        else:
            print(f"{port}/tcp   {CLOSED_COLOR}CLOSED{RESET}  {service}")

    else:  # UDP SCAN
        try:
            s.sendto(b"", (target_ip, port)) # sending an empty pkt
            s.recvfrom(1024) # receive up to 1024 bytes
            print(f"{port}/udp   {OPEN_COLOR}OPEN{RESET}    {service}")
            open_ports.append(port)
        except socket.timeout:
            print(f"{port}/udp   {FILTERED_COLOR}OPEN|FILTERED{RESET}  {service}")
        except Exception:
            print(f"{port}/udp   {CLOSED_COLOR}CLOSED{RESET}  {service}")

    s.close()

# Banner Grabing -> taking everything the target is willing to tell - Reading the initial response (banner) sent by a service

# Create and start threads
threads = []
lock = threading.Lock()

for port in ports:
    t = threading.Thread(target=scan_port, args=(port,)) # creates new clone for each port
    threads.append(t)
    t.start()

#wait till all threads finish
for t in threads:
    t.join() # won't print tillthe every thread is finished

# End time
end_time = datetime.now()
print("-" * 50)
print(f"Scan completed in: {end_time - start_time}")
with lock:
    open_ports.append(port)