# Linux User Management
- Linux is multiuser OS
### 1. Root User
- has got whole access of the system
- can even change system files
### 2. Normal User
- has limited permission
### 3. System user
- Used by services not humans
- run background processes like server
### 4. Accessing root user (sudo)
- needs root password
- `su - `
- `sudo apt update` run this command as root
- why choose sudo when we can just login as a root? ==you only elevate privileges when necessary — reducing risk.==
- #### Sudo
	- allows normal user to run root level command
	- it logs all action
	- is temporary privilage
- etc/passwd stores all user info
### 🔹 Difference (d/t) Summary

|Feature|Root User|Normal User|
|---|---|---|
|Permissions|Full|Limited|
|Risk|High|Low|
|Usage|System tasks|Daily tasks|
# Package Installation in Linux
Linux, software is installed using a package manager.
- apt means advanced package manager

👉 A package manager:
>Downloads software
Installs it
Handles dependencies (other required software)
Updates and removes programs

A package = a compressed file that contains:
- Program files
- Libraries (dependencies)
- Configuration files

🧭 3. Different Package Managers

Different Linux distributions use different managers:

| Distribution   | Package Manager |
| -------------- | --------------- |
| Ubuntu/ Debian | apt             |
| Kali Linux     | apt             |
| Arch Linux     | pacman          |
| Fedora         | dnf             |

### ⚙️ 4. APT (Advanced Package Tool)
Used in:
- Ubuntu
- Debian
- Kali Linux (you are using this)
- 🔄 Update Package List
	`sudo apt update`

👉 Downloads latest list of available packages
👉 DOES NOT install anything

⬆️ Upgrade Installed Packages
`sudo apt upgrade`
👉 Updates all installed software
`sudo apt update`
📥 Install a Package
`sudo apt install nmap` 👉 Installs nmap + dependencies

❌ Remove a Package
`sudo apt remove nmap`
🧹 Remove with Config Files
`sudo apt purge nmap`
🧼 Clean Unused Packages
`sudo apt autoremove`
🔍 Search for Packages
`apt search nmap`
📋 Show Package Info
`apt show nmap`
⚠️ Important APT Concept
👉 Always run:
`sudo apt update`
### ⚡️ 5. PACMAN (Arch Linux Package Manager)
Used in:
>Arch Linux
   Manjaro

👉 Faster and more minimal than APT
🔄 Update System (VERY IMPORTANT)
`sudo pacman -Syu` - it sync package, updates system
📥 Install Package
`sudo pacman -S nmap`
❌ Remove Package
`sudo pacman -R nmap`
🧹 Remove with Dependencies
`sudo pacman -Rs nmap`
🔍 Search Package
`pacman -Ss nmap`
📋 Package Info
`pacman -Si nmap`

⚠️ Important PACMAN Concept
👉 Never separate update + upgrade
Always use:
`sudo pacman -Syu`
APT vs PACMAN (Key Differences)

| Feature          | APT          | PACMAN       |
| ---------------- | ------------ | ------------ |
| OS               | Debian-based | Arch-based   |
| Command style    | Word-based   | Short flags  |
| Update + Upgrade | Separate     | Combined     |
| Package format   | .deb         | .pkg.tar.zst |

🔐 7. Why sudo is Required
👉 Installing software modifies system files
👉 Only root can do that
Example:
`sudo apt install git`

🧪 8. Practical Commands You Should Try
On your Kali/Ubuntu:
sudo apt update
sudo apt install git
git --version
Remove:
sudo apt remove git
# Script Installation
A **script** is a file that contains a series of commands that Linux executes automatically.
Instead of typing one by one hulunm and gize execute madreg
Mostly used in automation
### Types of Scripts
Most common:
- **Bash scripts** (`.sh`) → used in Linux
- Python scripts (`.py`)
- Other scripting languages 

|Feature|Bash Script|Python Script|
|---|---|---|
|File Extension|`.sh`|`.py`|
|Interpreter|Bash shell|Python|
|Use Case|System tasks|General programming|
|Complexity|Simple|More powerful|
|Speed|Faster for small tasks|Better for complex logic|
### Structure of a Script
`#!/bin/bash`
`echo "Hello World"`
`./script.sh` - means run from current directory
`bash myscript.sh` - to run a script file with out giving it an execution permission

### Installing a script
Sometimes "script installation" means:
- Downloading a script
- Making it executable
- Running it


|Concept|Meaning|
|---|---|
|Script|File with commands|
|Shebang|Defines interpreter|
|chmod +x|Make executable|
|./script.sh|Run script|
|bash script.sh|Alternative run|
# Software Installation
|Feature|Software Installer|Package Installer|
|---|---|---|
|Installation|Manual|Automatic|
|Dependencies|Manual fix|Auto handled|
|Source|Downloaded file|Online repository|
|Ease of use|Harder|Easier|
|Example|`.deb`, `.rpm`|`apt`, `pacman`|
- **Software installer** → install ONE app manually 📦
- **Package manager** → manages MANY apps automatically 🤖

>A software installer installs a specific application manually using files like `.deb` or `.rpm`, while a package installer (package manager) automatically installs and manages software along with its dependencies from online repositories.
# Shell
A **shell** is a program that lets you **interact with the Linux operating system using commands**.
- You type a command → shell understands it → system executes it
User → Shell → Kernel → Hardware

|Shell|Terminal|
|---|---|
|Software that runs commands|Interface you see|
|Bash, Zsh|GNOME Terminal|
Shell is VERY important because:
- Hackers use shell access (reverse shells)
- Many attacks happen through command execution
- Tools run inside the shell
### Types of Shell
You should know at least these for exams:
 🥇 1. Bash (Bourne Again Shell)
- Most common shell in Linux
- Default in Ubuntu
👉 Example:
echo "Hello"
🥈 2. Sh (Bourne Shell)
- Older version of Bash
- Simpler, less features
 🥉 3. Zsh (Z Shell)
- Advanced version of Bash
- Better customization
🐟 4. Fish Shell
- Beginner-friendly
- Auto-suggestions, colorful output
# or/ and/ piping
### Piping (|)
👉 Sends output of one command → to another command
Syntax:
`command1 | command2`
Example:
ls | grep txt
✔️ `List files → filter .txt`
### ✅ AND (&&)
👉 Run next command ONLY if first succeeds
Syntax:
`command1 && command2`
Example:
mkdir test && cd test
✔️ Go into folder only if created
### ❌ OR ()
👉 Run next command ONLY if first fails
Syntax:
`command1  command2`
Example:
cd folder  echo "Not found"
✔️ Show message if folder doesn’t exist
🧠 Final Memory Trick

>| → pass output
&& → if success → do next
 → if fail → do next
 