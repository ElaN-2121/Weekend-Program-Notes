# Common TCP Ports

TCP is connection-oriented (reliable, ordered delivery).
These are well-known services that use TCP:

Port	Service	Description
20/21	FTP	File transfer
22	SSH	Secure remote login
23	Telnet	Remote login (insecure)
25	SMTP	Email sending
80	HTTP	Web traffic
110	POP3	Email retrieval
143	IMAP	Email retrieval
443	HTTPS	Secure web traffic
445	SMB	File sharing (Windows)
3389	RDP	Remote Desktop

# Common UDP Ports

UDP is connectionless (faster, but no guarantee of delivery).
These are services that use UDP:

Port	Service	Description
53	DNS	Domain name resolution
67/68	DHCP	IP address assignment
69	TFTP	Simple file transfer
123	NTP	Time synchronization
161	SNMP	Network management
500	ISAKMP	VPN key exchange

# Ports That Use BOTH TCP & UDP

Some protocols use both, depending on the situation:

Port	Service	Usage
53	DNS	UDP (normal), TCP (large responses/zone transfers)
80	HTTP	Mostly TCP, but HTTP/3 uses UDP (QUIC)
443	HTTPS	TCP (traditional), UDP (QUIC/HTTP3)


**TCP → Reliable stuff (websites, email, SSH)**
**UDP → Fast stuff (streaming, DNS, gaming)**