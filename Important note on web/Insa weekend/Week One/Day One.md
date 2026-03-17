 we do many things in terminal web shell
## Who
- when we run `who` command, same username gn two different processes new load yemiadergew
	- one is normal gui load siaderg new , eg. elnathan seat0
	- the other one is virtual terminal load siaderg which is tty2
## inode

- `ls -i` is used to list inode number, `stat` also shows detailed metafile data
- An **inode** is a **data structure used by the filesystem to store information about a file**. It stores metadata such as:

|Stored in inode|Not stored|
|---|---|
|File size|File name|
|File permissions||
|Owner ID||
|Timestamps||
|Disk block locations||

Important detail: **The filename is NOT inside the inode.**
Two files with different names can point to the **same inode**.
*inode is used in forensics. find / -inum 123456*
In cybersecurity investigations, attackers may:
- rename files
- hide files
- create hard links
Even if the **name changes**, the **inode stays the same**.
So investigators can track files using the inode.
Example workflow:
1. Find suspicious file  
2. Get inode with ls -i  
3. Search system for same inode  
4. Discover hidden links
![[Pasted image 20260314135627.png]]
> Linux deletes file data only when the inode link count reaches 0.
Both can point to the **same inode**.
That means:
>- changing one file changes the other
>- they share the same data
>This is called a **hard link**.
>**Linux cares about the inode, not the filename.**
The filename is just a **pointer**.

## SSH
The default SSH port number is 22. So when you use `ssh user@IP`, it tries to connect to the default port 22. But if the remote server uses some other port for SSH, you should provide the port number:

```
ssh -p port_number user@IP
```
- ssh is like a normal login gn username and password snasgeba our info will be encrypted
### Bandit level01 summary
#### **Goal**
- Connect to the Bandit game server using SSH.
- **Find the password** for **Level 1** to move forward.
#### **Connection Details**
- **Host:** `bandit.labs.overthewire.org`
- **Port:** `2220`
- **Username:** `bandit0`
- **Password:** `bandit0`
**SSH Command to Use:**
ssh -p 2220 bandit0@bandit.labs.overthewire.org
#### **Environment**
- You are logged in as **bandit0**, in your own **home directory**.
- The server is a **Linux environment**, but restricted to this sandbox account.
#### **Tasks in Level 0**
1. **Login via SSH** – this gives you access to your Level 0 account.
2. **Locate the password for Level 1** – usually stored in a file in your home directory.
    - Typical command to check files:
        ls
    - To read the password from a file (e.g., `readme`):
        cat readme
3. **Use the password** from the file to log in to **Level 1**.
#### **Key Tips**
- Always check your current directory with:
    pwd
- List files and di
- directories with:
    ls -la
    (`-la` shows hidden files too)
- Use `cat filename` to see the content of a file.
- Every level teaches a new Linux or cybersecurity concept, so pay attention to the commands you use.
✅ **Outcome of Level 0:**
- You successfully **connect via SSH**.
- You **retrieve the password** for Level 1.
_**Username for level 01 is: bandit01**_
_**Password for level01 is:  ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If**_
#### Goal
- Find the **password for Level 2**.
- The password is stored in a file called **`-`** (a file literally named with a single dash `-`) inside your **home directory**.
#### **Login Details**
- **Username:** `bandit1`
- **Password:** (we get this from Level 0)
- **Host:** `bandit.labs.overthewire.org`
- **Port:** `2220`
**SSH Command:**
ssh -p 2220 bandit1@bandit.labs.overthewire.org
#### **Environment**
- we are now logged in as **bandit1**.
- our home directory is `/home/bandit1`.
#### **Tasks in Level 1**
1. **Locate the file** with the password (`-`) in the home directory.
    - Use `ls -la` to list all files, including hidden ones.
2. **Read the file** to get the password.
    - Since the file is named `-`, you cannot just do `cat -` (it will interpret `-` as a flag).
    - Correct command:
        cat ./-
3. **Use the password** to log into **Level 2** via SSH.
#### **Commands That Can Help**
- `ls` → list files
- `cat` → read file contents
- `file` → check file type
- `du` → check file size - disk usage
- `find` → search for files
#### **Tips**
- Save the **password locally** in a text file.
- Use `./` before filenames if the name is tricky or looks like a flag (e.g., `./-`).
- Always take **notes on commands**; levels get more complicated later.
✅ **Outcome of Level 1:**
- retrieve the password for **Level 2**.
- learn about **files with tricky names** and how to handle them in Linux.
- `du` = check **how big files or directories are**
- Helpful in Bandit to **spot the password file** by its size, especially when filenames are tricky or hidden.
### Level 02
Goal - learning how to **handle filenames that contain spaces in Linux**.
_**password for bandit2 user is - 263JGJPfgU6LtdEvgfWU1XP5yac29mFx**_
#### Steps
1. Login to bandit02 user
2. list files in the current directory
3. read the file in that directory - *since it has got spaces in the file name we need to handle it differently, some of the methods are*
	- putting filename inside double quotes
	- using backward slash
_**When filenames get weird (spaces, symbols, etc.), you can press TAB after typing part of the name and the shell will **auto-complete it.**_
#### Ways to stop Linux from thinking -- shows switch
##### 1. using -- in front of any filename
cat -- "--spaces in this filename--"
the first `--` tells the command:
> **Stop reading options from here onward. Everything after this is a filename.**
So now `cat` correctly understands:
"--spaces in this filename--" = file name
##### 2. Using backlashes
When you ran something like: cat ./--spaces\ in\ this\ filename--
it avoids some parsing issues because the shell treated it more clearly as **a path argument** rather than an option.
Using `./` is another common trick:
cat ./--spaces\ in\ this\ filename--
Here:
> ./ means **current directory**, so the command knows it's a **file path**, not an option.
### Level 03
_**Password is :
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx**_
 - **Goal** - is understading how hidden files work
#### Steps
1. login to bandit account
2. `cd inhere`
3. `ls -a`
4. `cat ...hiding-from-you`
- No need to use double quotes in front of the file name

### Level 04
_**password is :2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ**_
- **Goal** : 
- **Command**: reset is used to clear our terminal
- command to search for a file not containing a file and is not 0 bytes: `find . -type f -size 1c`