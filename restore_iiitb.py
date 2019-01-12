#!/usr/bin/python

from backup import *

sourceRoot = "/media/sujit/Expansion Drive/Backup/Sujit/IIITB/"
destinationRoot = "/home/sujit"

backupDirectories = [
	"funcoding",
	"IIITB",
#	"/home/sujit/My-Downloads",
	"Papers",
	"Personal",
	"Finance",
	"My-Movies",
	"myrepository",
	"mybin",
	"texmf",
	"application",
	"texmf",
	"mycourses"
]

fbackup = backup(sourceRoot, destinationRoot)
fbackup.next()
for backupDirectory in backupDirectories:
	print("backing up " + backupDirectory)
	fbackup.send(sourceRoot + "/" + backupDirectory)
fbackup.close()
print("Done!")
