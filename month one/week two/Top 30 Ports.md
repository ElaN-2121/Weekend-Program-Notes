# Top 30 Common Ports + Associated Risks

## 1. Port 20/21 — FTP (File Transfer Protocol)
- **What it does:** Transfers files between computers
- **Problem:** No encryption
- **Attacks:**
    - Password sniffing
    - Brute force login
    - Anonymous login abuse
## 🔐 2. Port 22 — SSH (Secure Shell)
- **What it does:** Secure remote login (like controlling a server)
- **Problem:** Exposed login service
- **Attacks:**
    - Brute force
    - Key theft
## ☎️ 3. Port 23 — Telnet
- **What it does:** Remote login (old version of SSH)
- **Problem:** Sends everything in plain text
- **Attacks:**
    - Credential sniffing
    - Man-in-the-middle (MITM)
## 📧 4. Port 25 — SMTP
- **What it does:** Sends emails
- **Attacks:**
    - Email spoofing
    - Spam relay abuse
    - Phishing
## 5. Port 53 — DNS
- **What it does:** Converts domain names → IP addresses
- **Attacks:**
    - DNS spoofing (redirecting users)
    - DDoS amplification
## 🧠 6. Port 67/68 — DHCP
- **What it does:** Automatically assigns IP addresses
- **Attacks:**
    - Rogue DHCP server (attacker gives fake network settings)
## 📂 7. Port 69 — TFTP
- **What it does:** Simple file transfer (no login)
- **Problem:** No authentication
- **Attacks:**
    - Unauthorized file access
## 🌐 8. Port 80 — HTTP
- **What it does:** Loads websites (no encryption)
- **Attacks:**
    - SQL Injection
    - XSS (Cross-Site Scripting)
    - Session hijacking
## 📬 9. Port 110 — POP3
- **What it does:** Receives emails (downloads them)
- **Problem:** Unencrypted
- **Attacks:**
    - Credential sniffing
## 📰 10. Port 119 — NNTP
- **What it does:** Usenet discussions (old forums)
- **Attacks:**
    - Spam abuse
## ⏱️ 11. Port 123 — NTP
- **What it does:** Syncs time across computers
- **Attacks:**
    - DDoS amplification
## 🖧 12. Ports 137–139 — NetBIOS
- **What it does:** File/printer sharing (Windows)
- **Attacks:**
    - Information gathering
    - Null session (no password access)
## 📥 13. Port 143 — IMAP
- **What it does:** Access email on server
- **Attacks:**
    - Credential theft
## 📡 14. Port 161/162 — SNMP
- **What it does:** Network device monitoring
- **Problem:** Weak/default passwords
- **Attacks:**
    - Information leakage
    - Brute force
## 🌐 15. Port 179 — BGP
- **What it does:** Internet routing between networks
- **Attacks:**
    - Route hijacking (redirect traffic)
## 💬 16. Port 194 — IRC
- **What it does:** Chat system
- **Attacks:**
    - Botnet command control
## 📂 17. Port 389 — LDAP
- **What it does:** Directory services (user info)
- **Attacks:**
    - LDAP injection
    - Info disclosure
## 🔒 18. Port 443 — HTTPS
- **What it does:** Secure websites
- **Attacks:**
    - SSL stripping
    - TLS downgrade
## 🖥️ 19. Port 445 — SMB
- **What it does:** Windows file sharing
- **Attacks:**
    - Worms like WannaCry ransomware
    - Remote code execution
## 📧 20. Port 465 — SMTPS
- **What it does:** Secure email sending
- **Attacks:**
    - Misconfiguration abuse
## 🔐 21. Port 500 — ISAKMP (VPN)
- **What it does:** Sets up VPN connections
- **Attacks:**
    - VPN brute force
## 📜 22. Port 514 — Syslog
- **What it does:** Sends logs
- **Attacks:**
    - Log injection (hide tracks)
## 🖨️ 23. Port 515 — LPD
- **What it does:** Printer service
- **Attacks:**
    - Print job abuse
## 🌐 24. Port 520 — RIP
- **What it does:** Routing protocol
- **Attacks:**
    - Route poisoning
## 🔐 25. Port 636 — LDAPS
- **What it does:** Secure LDAP
- **Attacks:**
    - Certificate issues
## 📂 26. Port 989/990 — FTPS
- **What it does:** Secure FTP
- **Attacks:**
    - Misconfigurations
## 📧 27. Port 993 — IMAPS
- **What it does:** Secure email access
- **Attacks:**
    - Credential attacks
## 📬 28. Port 995 — POP3S
- **What it does:** Secure email retrieval
- **Attacks:**
    - Credential attacks
## 🖥️ 29. Port 3389 — RDP (Remote Desktop Protocol)
- **What it does:** Lets you remotely control a Windows computer (full desktop access)
- **Why it’s important:** Very commonly exposed on the internet
- Attacks:
	- Brute-force login attacks
	- Credential stuffing
	- Ransomware entry point (attackers log in, then deploy malware)
👉 **Real-world note:** Many ransomware attacks start from weak RDP passwords
## 🗄️ 30. Port 1433 — Microsoft SQL Server
- **What it does:** Database service (stores application data)
- **Why it’s important:** Databases = high-value target 🎯
- Attacks:
	- SQL brute force
	- SQL injection (if connected to a web app)
	- Data theft / database dumping