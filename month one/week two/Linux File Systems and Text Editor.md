# 🖥️ Linux File System & Text Editors Notes
## Job of File System
- The **file system** is what the operating system uses to **store, organize, and manage files**.
- It is **essential for OS functionality** — without it, the OS cannot properly operate.
## 📂 Important Linux Directories
### `/` (Root Directory)
- The **top-level directory** in Linux.
- All files and directories originate from here.
- Everything you do in the system is based on this root.
### `/bin`
- Contains **essential Linux commands** (e.g., `ls`, `cp`, `mv`).
- These commands are required for basic system operation.
### `/boot`
- Stores files needed for **booting the system**.
- Includes the **Linux kernel** and bootloader files.
- Responsible for **loading the OS**.
### `/dev`
- Contains representations of **hardware devices**.
- Example: hard drives, USBs, etc.
### `/etc`
- Stores **configuration files**.
- Similar to **Control Panel** in Windows.
### `/home`
- Contains **user directories**.
- Each user has their own folder here.
### `/mnt` vs `/media`

|Directory|Purpose|
|---|---|
|`/mnt`|Used for **manual (temporary) mounting**|
|`/media`|Used for **automatic mounting** (USB, CD, etc.)|

💡 Note:
- Attackers sometimes use `/mnt` because data may disappear after restart.
### `/usr`
- Contains **user-installed programs and data**.
- Not just personal files—also includes system-wide applications.
## 📝 Text Editors in Linux
### CLI Editors
- `nano`
- `vim`
- `emacs`
### GUI Editors
- Visual Studio Code
- Sublime Text
## ✏️ Nano Editor Commands

|Shortcut|Action|
|---|---|
|`Ctrl + R`|Append/insert file|
|`Ctrl + O`|Save|
|`Ctrl + X`|Exit|
|`Ctrl + T`|Run/check command|

## ⚡ Vim Editor Basics
### Opening File
vim filename.ext
### Modes
- `i` → Insert mode (write text)
- `Esc` → Command mode
### Commands

|Command|Function|
|---|---|
|`:w`|Save|
|`:q`|Quit|
|`:wq!`|Force save & exit|
|`:%!command`|Run command inside vim|

## 🛠️ Using Vim in Cybersecurity
### 🔴 Red Team (Attacker POV)
- Can execute commands inside vim.
- Can hide or inject **malicious code**.
- Used in **Living Off the Land (LotL)** attacks:
    - Using **existing system tools** instead of installing new ones.
### 🔵 Blue Team (Defender POV)
- Analyze suspicious files.
- Monitor unusual vim usage.
- Detect abnormal command execution.
## 🧩 Editing Servers with Vim
- Connect via SSH:
ssh user@server_ip
- Open config file:
vim /etc/config_file
- Edit and save changes.
## 🧠 Tmux (Terminal Multiplexer)
- Tool used to **split terminal into multiple sessions**.
- Allows multitasking in one terminal window.
## 🔐 Red Teaming Concepts
### Living Off the Land (LotL)
- Using **built-in tools** (like vim, bash) to attack a system.
- Harder to detect because no external tools are installed.
### Persistence
- Techniques used by attackers to **maintain access** even after:
    - Reboot
    - Logout
Examples:
- Creating hidden users
- Modifying startup scripts
- Backdoors
## ❓ Answer: Advanced Use of Text Editors in Hacking
Text editors (especially **vim**) can be used for:
### 1. File Manipulation
- Editing system configs (`/etc/passwd`, `/etc/shadow`)
### 2. Command Execution
- Running shell commands inside vim:
:%!whoami
### 3. Privilege Escalation
- If vim runs with sudo:
sudo vim
Then:
:!bash
### 4. Backdoor Creation
- Insert malicious scripts into:
    - `.bashrc`
    - startup files
### 5. Data Exfiltration
- Encode and copy sensitive data