# 🐧 Linux File Structure (Filesystem Hierarchy)
## 📌 1. Basic Idea
In Linux, everything is organized in a **hierarchical tree structure** — similar to an upside-down tree.
- The **topmost directory** is called the **root directory**:
    `/`
- Everything (files, folders, devices, etc.) exists under `/`.

👉 Unlike Windows (C:, D:, etc.), Linux has **one unified filesystem**.

## 🌳 2. Structure Overview
Here’s a simplified view:
/  
├── bin  
├── boot  
├── dev  
├── etc  
├── home  
├── lib  
├── media  
├── mnt  
├── opt  
├── proc  
├── root  
├── run  
├── sbin  
├── tmp  
├── usr  
└── var
## 📂 3. Important Directories Explained
### 🔹 `/` (Root Directory)
- The starting point of everything.
- All files and directories branch from here.
### 🔹 `/bin` (Binary Files)
- Contains essential command binaries.
- Used by all users.
Examples:
- `ls`
- `cp`
- `mv`
- `cat`
👉 These commands must be available even in minimal system mode.
### 🔹 `/sbin` (System Binaries)
- Contains system-level commands.
- Mainly used by administrators (root user).
Examples:
- `shutdown`
- `reboot`
- `fsck`
### 🔹 `/boot`
- Contains files needed to boot the system.
Includes:
- Kernel (Linux core)
- Bootloader files (like GRUB)
### 🔹 `/dev` (Devices)
- Contains device files.
Examples:

- `/dev/sda` → hard disk
    
- `/dev/usb` → USB devices
    

👉 In Linux, **hardware is treated like files**.

---

### 🔹 `/etc` (Configuration Files)

- Contains system-wide configuration files.
    

Examples:

- Network settings
    
- User account settings
    
- Service configurations
    

👉 Important files:

- `/etc/passwd` → user accounts
    
- `/etc/hosts` → hostname mapping
    

---

### 🔹 `/home`

- Personal directories for users.
    

Example:

/home/username

👉 This is where:

- Documents
    
- Downloads
    
- Personal files are stored
    

---

### 🔹 `/root`
- Home directory for the **root (admin) user**.
⚠️ Not the same as `/`
### 🔹 `/lib` and `/lib64`
- Contains shared libraries (like DLLs in Windows).
- Needed by programs in `/bin` and `/sbin`.
### 🔹 `/media`
- Mount point for removable devices.
Examples:
- USB drives
- CDs/DVDs
### 🔹 `/mnt`
- Temporary mount point.
- Used manually by system admins.
### 🔹 `/opt`
- Optional software packages.
- Third-party applications are often installed here.
### 🔹 `/proc`
- Virtual filesystem.
- Contains information about:
    - Running processes
    - System memory
    - CPU usage
👉 Example:
/proc/cpuinfo
### 🔹 `/run`
- Stores runtime data.
- Cleared when system reboots.
### 🔹 `/tmp`
- Temporary files.
- Automatically deleted after reboot.
### 🔹 `/usr` (User System Resources)
Contains user-related programs and data.
Subdirectories:
- `/usr/bin` → user commands
- `/usr/lib` → libraries
- `/usr/share` → shared files
👉 Most installed applications live here.
### 🔹 `/var` (Variable Data)
- Stores frequently changing data.
Examples:
- Logs → `/var/log`
- Cache
- Databases
## 🔑 4. Key Concepts
### 📌 Everything is a File
In Linux:
- Files
- Directories
- Devices
- Processes
👉 All are treated as files.
### 📌 Absolute vs Relative Paths
#### Absolute Path
- Full path from root `/`
Example:
/home/user/file.txt
#### Relative Path
- Path from current directory
Example:
documents/file.txt
### 📌 Mounting
- Storage devices are attached to directories.
Example:
- USB → `/media/usb`
👉 No drive letters like Windows.
## 🧠 5. Quick Memory Tips
- `/home` → users
- `/etc` → settings
- `/bin` → commands
- `/var` → logs/data
- `/tmp` → temporary
- `/boot` → startup
- `/dev` → hardware
---
## 🎯 6. Why This Structure Matters
- Helps in **system administration*
- Makes Linux **organized and predictable**
- Essential for
    - Cybersecurity 🔐
    - System troubleshooting 🛠️
    - Server management 🌐
## ✍️ 7. Simple Analogy
Think of Linux like a **library**:
- `/` → building
- `/home` → personal study rooms
- `/etc` → rule book
- `/bin` → tools section
- `/var` → activity logs
- `/tmp` → scratch paper