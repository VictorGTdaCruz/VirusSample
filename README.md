# Attention!!
This code was made for educational purposes only. I don't intend on running it on a machine other than my VM. The .exe file was not uploaded for obvious reasons. If this violates anything feel free to contact me.

# About
This code is part of a college project. It's objective is to show how easy it is to create a malicious software with basic programming knowledge. In other words, how anyone is able to cause harm to computer systems it has (or not) access to.

# How It Works
It simply renames all files and directories within the root path with a pseudo random number between 0 and 9999999. If directories are ordered by name, wich is the default ordering method in windows, they'll be shuffled based on the size of the chosen number. Now for the files: every file has an extension on it's name, so the computer knows what kind of file that is and what program should it use to read it, for example .txt or .doc. After renaming, the extension won't exist anymore, so every file will be of an unknown type. This means that, when you try to open something, the computer won't know the proper program it should and will ask the user for help. If the user doesn't know what file that is, wich he will probably not know because of the rename, he will not be able to see what's inside.

Obs: As this is not running with malicious purposes, I didn't have the trouble to comment the prints. Actually they are very helpfull at understanding how the code works and to keep track of what it is doing.

# Possible Coming Features
- Finding a way to make the code auto run or the user to run it.
- ~~Writing the output of prints in a JSON and sending it back/somewhere, so the author can have a way to tranlate the desired file back.~~
- A piece of code to, in some cases, change a file's location(or dir's location) to somewhere else. This would help in cases where only one file is located at a certain directory.
