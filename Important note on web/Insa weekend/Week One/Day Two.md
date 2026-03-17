## Command line interface
### /
there is a difference between directory and file
- In linux everything is a file
- bin  -binary yemikemetbet new
- boot is systemu lemenesat yemitekembacgew
- dev yalut devices
- home - user account , and   home irectory lay bzu different users directory linor yichlal
- lib - puts libraries, useful to execute bin
- media and mnt have same function gn mnt lay manualy rasachn mediasn mount madreg enchlalen
- opt
- proc - low level kale process ga integrate yemiadergu processes yemitekemubet new
- root - ye useru info and other files yemikemetbet new ena ye windows equivalent of root is administration
- sbin - system  binary
- sys - about our system info yemikemetbet new
- tmp - temporary things yemikemetubet new
- usr - unique system resource - binary yemikemetbet bota wedezi link new yemideregew - tkuami new
- var - very time change yemiadergu directories nachew
#### Useful directories for blue team
- etc - mekeyer yelelebachewn files new yemiyzew
- var - log slemiaskemt yitekmenal
#### Useful directories for red teaming
- bin - because we will be storing binaries
- tmp - because world writeable slehone ena permission restrict slemayadergen we will use it to store our payload
## Commands
1. mkdir
	- andu wust lela create madreg kefelegn kefit lay aylenbetn parent folder mechermer alebn like "home/test1/test2"
	- parentunm abro create endiadergew kefelegn gn we use mkdir -p "test1/test2"
2. cat
- used to concatenate file
3. echo
- we can redirect echo by using > sign, ya file already exist yemiaderg kehone yezan file content over-write yadergewal
- >> kaderegnew degmo filename lay yalewn document replace ayadergewm
1. touch 
2. cp 
3. mv
	- moving file froone directory
	- other function of move is renaming 
4. use rm 
	- use cauteously
	- teminal lay honen remove yemnadergewn we won't use it directly again
	- `sudo rm -rf /` by force hulunm root lay yale neger remove yadergewal

## File permissions
### Rules
>r = read
w = write
x = execute
### Roles
1. Owner
2. Gues/ lela account lay yale sew/group
3. others
UG0 744
everytime the value of r is 4
value of w is 2
value of x is 1
file1.txt
chmode ug0 filename 
==-== means it is a file
==d== means it is a folderp
## Goal of red teaming
- detect alemedereg
- in red teamig we gotta be cautious
- allow yetederegelnen domain bcha sayhon whole domainaccess madreg enchalalen
- long term new
## Goal of pentesting
- Limited domain bcha new access yemnadergew
- Pentest lay permission eskalen dres we can do anything we want
- short term new

## Challenge
