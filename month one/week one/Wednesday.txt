## Over the wire (Chapter One - Two)
## Chapter One
Why hackers choose Linux
- It's open source
- it's transparent
- It offers granular control
- Most hacking tools are written for Linux (they still work but it's hard to implement them all)
#### Binaries 
- This term refers to files that can be executed, similar to executables in Windows. 
- Binaries generally reside in the /usr/bin or usr/sbin directory and include utilities  such as ps, cat, ls, and cd as well  as  applications  such as the  wireless hacking tool aircrackng and the intrusion detection system (IDS) Snort.
#### Case sensitivity 
- Unlike Windows, Linux is case sensitive. 
- This means that Desktop is different from desktop, which is different from DeskTop.
- Many people coming from a Windows environment can find this frustrating. 
#### Directory 
- This is the same as a folder in Windows. 
#### Home 
- Each user has their own /home directory, and this is generally where files you create will be saved by default. 
#### Kali 
- Kali Linux is a distribution of Linux specifically designed for penetration testing. 
- In Linux, there is an account called root: *As a hacker or pentester, you will often use the root account to give yourself  control over the system. The windows equivalent of it is an administrator.*
#### Script 
- This is a series of commands run in an interpretive environment that converts each line to source code. 
- Many hacking tools are simply scripts. 
- Scripts can be run with the bash interpreter or any of the other scripting language  interpreters, such as Python, Perl, or Ruby. 
- Python is currently the most popular interpreter among hackers. 
#### Shell 
- This is an environment and interpreter for running commands in Linux. 
- The most widely used shell is bash, which stands for Bourneagain shell. 
#### Terminal 
- This is a command line interface (CLI).
### Linux File System
 - Linux doesn’t have a physical drive *(such as the C: drive)* at the base of the  filesystem but uses a *logical filesystem instead.*
 - At the very top of the filesystem structure is */*, which is often referred to as the root  of the filesystem, as if it were an upsidedown tree.
 - ![[Pasted image 20260318110456.png]]
 - */root* The home directory of the allpowerful root user
 - */etc* Generally contains the Linux configuration files files that control when and how programs start up 
 - */home* The user’s home directory 
 - */mnt* Where other filesystems are attached or mounted to the filesystem
- */media* Where CDs and USB devices are usually attached or mounted to the filesystem 
- */bin* Where application binaries (the equivalent of executables in Microsoft Windows) reside 
- */lib* Where you’ll find libraries (shared programs that are similar to Windows DLLs) 

It’s also important to know before you start that you should not log in as root when performing routine tasks, because anyone who hacks your system when you’re  logged in as root would immediately gain root privileges and thus “own” your system. Log in as a regular user when starting regular applications, browsing the web,  running tools like Wireshark, and so on.

### Basic Linux commands
- **pwd** - The present working directory command, pwd, returns your location within  the directory structure.
- **whoami** - As a hacker, you usually need to have all those privileges to run the programs and commands you need (many hacker tools won’t work unless you have root privileges), *used to see which user we are logged in as*, 
- **cd** - used to change directory 
	- To move up one level in the file structure (toward the root of the file structure),  we use cd followed by double dots (..)
- **ls (list)** -To see the contents of a directory (the files and subdirectories),  windows equivalent is *dir*, to use ls on a folder, we don't necessarily need to be on that folder, we can use *ls /folder_name*
	- The switch *-l* is added to include the date of creation, permission, ... and it is callsed "long list"
	- The switch *-a* is added to show hidden files too
- **--help** - to get help for a command and sometimes we can use *-h* and *-* to get help
- **manual (man)** page with more information, such as a description and synopsis of  the command or application.
- **locate** - Followed by a keyword denoting what it is you want to find, this command  will go through your entire filesystem and locate every occurrence of that word.
- **whereis** -If you’re looking for a binary file, you can use the whereis command  to locate it. This command returns not only the location of the  binary but  also its  source  and man page if they are available.
- **which** - The which command is even more specific: it only returns the location of the binaries in the PATH variable in Linux.
- **find directory options expression** - to find utilities
