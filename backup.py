#!/usr/bin/python

import os
import sys
import shutil

from os import *
from string import *

sourceRoot = ""; # fill in appropriate value
destinationRoot = ""; # fill in appropriate value
backupDirectoryName = ""; # fill in appropriate value

def isSubdirectory(dir1, dir2):
	if(len(dir1) < len(dir2)):
		return False
	if(not dir1[:len(dir2)] == dir2):
		return False
	return True

def getRelativeName(dirName, root):
	if(not isSubdirectory(dirName, root)):
		raise Exception(dirName + " is not a subdirectory of " + root)
	if(len(dirName) < len(root)):
		return dirName
	if(root[-1] == "/"):
		return dirName[len(root):]
	else:
		return dirName[len(root) + 1:]

# always provide the full path name
def backupDir(dirName):
	global sourceRoot

#	print "going into directory: " + dirName
	relativePathName = getRelativeName(dirName, sourceRoot)
	currentDestinationDir = destinationRoot + "/" + relativePathName
	if(not os.path.exists(currentDestinationDir)):
		os.mkdir(currentDestinationDir)
	allnames = listdir(dirName)
	for name in allnames:
		sourceName = dirName +"/" + name
		if(os.path.isfile(sourceName)):
			destinationFileName = currentDestinationDir + "/" + name
			if((not os.path.exists(destinationFileName)) or (os.path.getmtime(sourceName) > os.path.getmtime(destinationFileName))):
				print "copying " + sourceName + " to " + currentDestinationDir + " ..."
				shutil.copyfile(sourceName, destinationFileName)
		elif(os.path.isdir(sourceName)):
			backupDir(sourceName)
		else:
			print "Something wrong with " + name
#	print "going out of directory: " + dirName

# path is relative to root, not an absolute path
def createPath(path, root):
	def getPathName(path):
		if(len(path) > 1):
			return path[0] + "/" + getPathName(path[1:])
		return path[0]

	if(not os.path.exists(root + "/" + getPathName(path))):
		if(len(path) > 1):
			createPath(path[:-1], root)
		os.mkdir(root + "/" + getPathName(path))

# given a full/absolute pathname dirName, this returns the path relative to root.
def getRelativePath(dirName, root):
	if(not isSubdirectory(dirName, root)):
		raise Exception(dirName + " is not a subdirectory of " + root)
	return split(getRelativeName(dirName, root), "/")

def backup(s, d):
	global backupDirectoryName
	global sourceRoot
	global destinationRoot

	sourceRoot = s
	destinationRoot = d
	if(sourceRoot == ""):
		print "sourceRoot hasn't been set"
		sys.exit()
	if(destinationRoot == ""):
		print "destinationRoot hasn't been set"
		sys.exit()
	if(not os.path.isdir(sourceRoot)):
		print "sourceRoot = " + sourceRoot + " doesn't exist."
		sys.exit()
	if(not os.path.isdir(destinationRoot)):
		print "destinationRoot = " + destinationRoot + " doesn't exist."
		sys.exit()
	while(True):
		backupDirectoryName = (yield)
		if(backupDirectoryName == ""):
			print "backupDirectoryName hasn't been set"
			sys.exit()
		if(not os.path.isdir(backupDirectoryName)):
			print "backupDirectory = " + backupDirectoryName + " doesn't exist."
			sys.exit()
		if(not isSubdirectory(backupDirectoryName, sourceRoot)):
			print "backupDirectoryName isn't a subdirectory of the sourceRoot."
			sys.exit()
		createPath(getRelativePath(backupDirectoryName, sourceRoot), destinationRoot)
		backupDir(backupDirectoryName)
