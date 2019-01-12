#!/usr/bin/python

from backup import *

sourceRoot = "/home/sujit"
destinationRoot = "/media/sujit/Expansion Drive/Backup/Sujit/IIITB/"

backupDirectories = [
	"/home/sujit/funcoding",
	"/home/sujit/IIITB",
	"/home/sujit/Papers",
	"/home/sujit/Personal",
	"/home/sujit/Finance",
	"/home/sujit/My-Movies",
	"/home/sujit/myrepository",
	"/home/sujit/mybin",
	"/home/sujit/texmf",
	"/home/sujit/application",
	"/home/sujit/texmf",
	"/home/sujit/mycourses",
	"/home/sujit/My-Downloads",
	"/home/sujit/research"
]

fbackup = backup(sourceRoot, destinationRoot)
fbackup.next()
for backupDirectory in backupDirectories:
	print("backing up " + backupDirectory)
	fbackup.send(backupDirectory)
fbackup.close()
print("Done!")
