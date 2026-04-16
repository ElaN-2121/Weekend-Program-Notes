# Text Manipulation (Chapter Two)
Linux has numerous ways of manipulating text, and each way comes with its own strengths and weaknesses.

|Command|Real-life meaning|
|---|---|
|`apt update`|Refresh app store|
|`apt install snort`|Download & install app|
Snort is ==a widely used, open-source network intrusion detection and prevention system (IDS/IPS) developed by Cisco==. It provides real-time traffic analysis, packet logging, and content searching/matching to detect attacks like port scans, buffer overflows, and malware, primarily using a rule-based language to inspect network traffic.

| Snort 2 (old)      | Snort 3 (new)    |
| ------------------ | ---------------- |
| `snort.conf`       | `snort.lua`      |
| simple config file | Lua-based config |
| older structure    | modular system   |
### head and tail
>If you just want to view the beginning of a file, you can use the head command. By default, this command displays the first 10 lines of a file.
`kali >head /etc/snort/snort.con` If you want to see more or fewer than the default 10 lines, enter  the quantity you want with the dash (-) switch after the call to head and before the filename.

>The tail command is similar to the head command, but it’s used to view the last lines of a file.

### Numbering Lines
Sometimes—especially with very long files—we may want the file to display line numbers.
To display a file with line numbers, we use the nl (number lines) command.
`kali >nl /etc/snort/snort.conf`

### Filtering with grep
The command grep is probably the most widely used text manipulation command. It lets you filter the content of a file for display.
`kali >cat /etc/snort/snort.conf | grep output`
The grep command is a very powerful and essential command for working in Linux, because it can save you hours of searching for every occurrence of a word or command in a file.

### Explanation of hacker's practice (page - 48)
`tail -n+507 /etc/snort/snort.conf | head -n 6`
`-n` means show number

| Step | Command     | Result               |
| ---- | ----------- | -------------------- |
| 1    | tail -n+507 | starts at line 507   |
| 2    | pipe        | sends output forward |
| 3    | head -n 6   | keeps only 6 lines   |
- `-n 6` → number of lines
- `-n+507` → starting line
- `grep -n "text" file` outputs the file with number for each line

### grep context options
- `-B` - means before, `grep -B 5 "pattern" file`, *Show **5 lines BEFORE** the matching line*
- `-A` → means after, `grep -A 5 "pattern" file`, *Show **5 lines AFTER** the match*
- `-C` -> means context, `grep -C 5 "pattern" file`, shows 5 before and 5 after lines after a given pattern is detected, (*what happened before, the actual event, what happened after*) think of this like a combo of a and b

| Command | What it does           |
| ------- | ---------------------- |
| `-B 5`  | 5 lines before         |
| `-A 5`  | 5 lines after          |
| `-C 5`  | 5 lines before + after |
### Stream Editor (sed)
- Find something in a file and **transform it on the fly**
- lets you search for occurrences of a word or a text pattern and then perform some  action on it.
> `kali >sed s/mysql/MySQL/g /etc/snort/snort.conf > snort2.conf`
> The s command performs the search: you first give the term you are searching for (mysql) and then the term you want to replace it with (MySQL), separated by a slash (/). The g command tells Linux that you want the replacement performed globally. Then the result is saved to a new file named snort2.conf.

### Controlling the Display with more 
- The more command displays a page of a file at a time and lets you page down through it using the ENTER key. It’s the utility that the man pages use, so let’s look at it first.
### Displaying and Filtering with less 
- The less command is very similar to more, but with additional functionality—hence, the common Linux aficionado quip, “Less is more.” With less, you can not only scroll through a file at your leisure, but you can also filter it for terms. 