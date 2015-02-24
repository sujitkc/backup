#!/usr/bin/python

from backup import *

sourceRoot = "/home/sujit"
destinationRoot = "/media/Expansion Drive/Backup/Sujit/IIITB/"

backupDirectories = [
	"/home/sujit/funcoding",
	"/home/sujit/IIITB",
	"/home/sujit/My-Downloads",
	"/home/sujit/Personal",
	"/home/sujit/Finance",
	"/home/sujit/My-Movies",
	"/home/sujit/myrepository",
	"/home/sujit/mybin",
	"/home/sujit/texmf",
	"/home/sujit/application",
	"/home/sujit/mycourses"
]

fbackup = backup(sourceRoot, destinationRoot)
fbackup.next()
for backupDirectory in backupDirectories:
	print("backing up " + backupDirectory)
	fbackup.send(backupDirectory)
fbackup.close()
print("Done!")
