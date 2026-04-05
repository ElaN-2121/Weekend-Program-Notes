import socket
from datetime import datetime
import threading

"""
Implemented Features: 
1. Open/ closed
2. Banner Grabbing
3. Accept Port Ranges
"""

# Target input
target = input("Enter target (IP or domain): ")

# Resolve domain to IP
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname")
    exit()
# Port Range Insertion
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

# Checking if the given range is allowed
if start_port < 0 or end_port > 65535:
    print("Invalid port range")
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
ports = range(start_port, end_port + 1)
open_ports = []

print("PORT     STATE   SERVICE     BANNER")
print("-" * 50)

# Scanning a given port on a target
def scan_port(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target_ip, port))

        service = services.get(port, "Unknown")

        if result == 0:
            service = services.get(port, "Unknown")

            try:
                #banner grabing
                if port == 80:
                    s.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
                else:
                    s.send(b"Hello\r\n") # used b because we can only send bytes over a network and "hello is a string"
                response = s.recv(1024).decode(errors="ignore") #decode() converts byte to a readable string
                banner = response.split("\n")[0]
            except:
                banner = "No banner"

            print(f"{port}/tcp   OPEN    {service}   {banner}")
            open_ports.append(port)
        else:
            print(f"{port}/tcp   CLOSED  {service}")
        s.close()

# Banner Grabing -> taking everything the target is willing to tell - Reading the initial response (banner) sent by a service

# ✅ Create and start threads
threads = []

for port in ports:
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

#the threads eskemichersu wait
for t in threads:
    t.join()

# End time
end_time = datetime.now()
print("-" * 50)
print(f"Scan completed in: {end_time - start_time}")
print(f"Open ports: {open_ports}")