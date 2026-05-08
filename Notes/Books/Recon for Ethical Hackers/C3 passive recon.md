# Chapter Three

## Passive Recon

- Passive reconnaissance is collecting information about a target without directly interacting with them.
- Instead of attacking the target, hackers use:
    - Google
    - Social media
    - Public websites
    - Search engines
    - Archived websites
- 💡 Key idea: Passive recon = silent information gathering
- ✅ Advantages of Passive Recon
    - Stealthy
    - Low cost
    - Safer
    - Mostly legal
    - Many information sources
- ❌ Disadvantages of Passive Recon
    - Information may be outdated
    - Data may be inaccurate
    - Time-consuming

## Internet Archive / Wayback Machine

- Stores historical versions of websites.
- Importance: Deleted content may still be accessible.
- Used for:
    - Finding old company data
    - Discovering exposed information
    - Viewing outdated pages 

## Cookies & Privacy Risks

- Cookies: Small files stored in browsers.
- Used for:
    - Tracking users
    - Saving sessions
    - Improving user experience
- Risk: Attackers can steal:
    - Session IDs
    - User activity data
- Result: 
    - Session hijacking / unauthorized access.

## Reverse Image Search

- Tools like Google Images/Google Lens can:
    - Identify people
    - Find locations
    - Match images online
- Social media creates a digital footprint.

## 🏢 Data Brokers

- Companies that collect and sell user data.
- Sources:
    - Cookies
    - Mobile apps
    - Public records
    - Browsing history
-Risk: Attackers can use this data for profiling targets.

## 👣 Footprinting

-Collecting detailed information about a target.
- Used to understand:
    - Systems
    - Networks
    - Employees
    - The attack surface
    - Security weaknesses
### 🔍 Common Footprinting Methods
    - Google searching
    - Google dorking
    - Social media analysis
    - DNS lookup
    - Website analysis
    - Email analysis
    - Network scanning
    - Social engineering

## 📂 Types of Information Collected

### 1. System Information
- Includes:
    - Operating system
    - Applications
    - Services
    - Usernames/passwords
- Purpose:
    - Find vulnerabilities
### 2. Network Information
- Includes:
    - DNS
    - ARP
    - LLMNR
    - Domain names
    - Firewall info
P- urpose:
    - Understand network structure
    - Identify weak protocols
### 3. Organizational Information
- Includes:
    - Employee names
    - Emails
    - Phone numbers
    - Company structure
- Purpose:
    - Social engineering attacks

## OSINT

### Definition
- Collecting and analyzing publicly available information from the internet.

### Common Data Sources
    - Media (photos/videos/audio)
    - Text (blogs/articles/documents)
    - Maps/geolocation data

### Key Idea
> Collect → Analyze → Create Meaning.

### 🔄 OSINT Life Cycle
1. Requirements Gathering
- Understand: Client goals, Risks, Deliverables
2. Data Collection
- Gather: Documents, Photos, Videos, Technical details
3. Data Analysis
- Check: Accuracy, Credibility, Relevance
- Convert data into meaningful intelligence.
4. Pivoting & Reporting
- Explore new related data points, Report findings and risks

### 🧩 YOGA
- Purpose
- OSINT visualization tool.
- Helps:
    - Connect data points
    - Discover relationships
    - Pivot investigations

### ✅ Benefits of OSINT
- Used by:
    - Ethical hackers
    - Law enforcement
    - Investigators
- Helps:
    - Find criminals
    - Track missing persons
    - Discover data leaks
    - Improve security awareness

### 🎭 Sock Puppets

#### Definition
- Fake social media accounts used for OSINT investigations.
- Purpose:
    - Hide real identity
    - Gather intelligence anonymously

#### 📌 Sock Puppet Guidelines
    - Never use personal accounts
    - Use burner email/phone
    - Make profiles realistic
    - Post regularly
    - Avoid VPN/TOR during account creation
    - Do not use stolen pictures

#### 🛠️ Useful Sock Puppet Tools
    - Fake Name Generator
    - This Person Does Not Exist
    - Privacy Cards
    - WEBGAP

## 🌐 Anonymizing Network Traffic

- Purpose:
    - Hide IP address
    - Hide geolocation
    - Prevent tracing
- Methods:
    - VPN
    - Proxychains
    - TOR

### 🔒 VPN
- Purpose: Creates encrypted tunnel over the internet.
- Benefits:
    - Hides IP address
    - Changes geolocation
    - Protects traffic
- Important
    - Avoid DNS leaks
    - Disable IPv6 if unsupported
    - Choose no-log VPNs

### 🔗 Proxychains
- Purpose: Routes traffic through multiple proxy servers.
- Benefits:
    - Better anonymity
    - Hides source IP
    - Bypasses restrictions
- Supports:
    - HTTP
    - HTTPS
    - SOCKS4
    - SOCKS5
- Key Idea: Traffic passes through several proxies before reaching target.

### 🧅 TOR (The Onion Router)
- Purpose: Anonymous internet browsing.

#### How It Works
**Traffic:**
- Encrypted multiple times
- Routed through multiple TOR nodes
**Each node:**
- Knows only previous & next node

**Benefits:**
    - Hides identity
    - Hides location
    - Access to .onion sites
**Key Idea**
*TOR = layered encryption + anonymous routing.*
#### ⚠️ TOR Safety
    - Use only TOR browser for .onion sites
    - Don’t trust downloads
    - Be cautious on dark web

## ⚡ Ultra Quick Revision
    Passive recon = no interaction
    Active recon = direct interaction
    OSINT = public intelligence gathering
    Footprinting = profiling target
    Cookies store session data
    Social media leaks information
    Sock puppet = fake investigation account
    VPN = encrypted tunnel
    Proxychains = multiple proxy routing
    TOR = anonymous layered routing
