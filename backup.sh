#!/bin/bash

TRUE=1;
FALSE=0;

sourceRoot=""; # fill in appropriate value
destinationRoot=""; # fill in appropriate value
backupDirectory=""; # fill in appropriate value

function backupDir(){
	local prefix="$1"; # name of the directory to be backed up.
	local completeName=$(getCompletePathName "${prefix}"); # complete name of the directory to be backed up.	
	if [ ! -d "${completeName}" ]; then
		echo "${completeName} is not a directory. Returning ...";
		return 1;
	fi

	echo "entering directory '${completeName}'";
	local suffix=${completeName#"${sourceRoot}"}; # the name of the directory relative to the sourceRoot.

	if [ ! -d "${destinationRoot}/${suffix}" ]; then # ${destinationRoot}/${suffix} is the complete name of the destination folder
#		echo "creating destination  ${destinationRoot}/${suffix}";
		mkdir "${destinationRoot}/${suffix}"; # there should be a way to check if the make directory succeeded.
	fi
	
	isDirectoryEmpty $completeName;
	local result=$?;
	if [ !  "$result" == "$TRUE" ]; then
		for name in ${completeName}/*; do
	#	for name in `find $completeName -maxdepth 1`; do
			if [ "$name" == "$completeName" ]; then
				continue;
			fi
			local inBetween=${suffix%"${name}"};
			isSubdirectory "${completeName}" "${name}";
			local result=$?;
			local filename=`basename "$name"`;
			if [ -d "${name}" ]; then
			    backupDir "${name}";
			elif [ -f "${name}" ]; then
				local destinationFileName="${destinationRoot}/${inBetween}/${filename}"
				if [ -f "$destinationFileName" ]; then
					whichFileIsOlder "${name}" "${destinationFileName}";
					local older=$?;
					if [ "${older}" -eq "2" ]; then
#			    			echo "copying file ${name} to ${destinationFileName}";
			    			cp "${name}" "${destinationRoot}/${inBetween}"; # there should be a way to check if the file copy succeeded.
#					else
#			    			echo "No need to copy ${name}.";
					fi
				else
#					echo "copying file ${name} to ${destinationFileName}";
					cp "${name}" "${destinationRoot}/${inBetween}"; # there should be a way to check if the file copy succeeded.
		    		fi
			else
				echo "Something wrong with $name";
				exit 1;
			fi
		done;
	fi
#	echo "exiting directory ${prefix} ...";
}

function whichFileIsOlder() {
	local file1="$1";
	local file2="$2";
	local sdate=`date +%s -r "${file1}"`;
	local ddate=`date +%s -r "${file2}"`;
	local diff=`expr ${ddate} - ${sdate}`;
	if [ "${diff}" -lt "0" ]; then
		return 2;
	else
		return 1;
	fi
}

function isSubdirectory(){
	if [ ! $# == 2 ]; then
		echo "isSubdirectory : function takes 2 parameters; your provided $#.";
		exit 1;
	fi
	local dir1=$(getCompletePathName $1);
	local dir2=$(getCompletePathName $2);

	local l=`expr length "${dir1}"`;
	local p=${dir2:0:${l}};
	if [ "${p}" == "${dir1}" ]; then
		return ${TRUE};		
	fi

	return ${FALSE};
}

function createParentDirectories(){
	local name="$1"; # name  of the directory the directory structure of whose ancestor directories has to be created in the destinationRoot.
	local completeName=$(getCompletePathName "$1"); # complete name of name
	isSubdirectory "${sourceRoot}" "${completeName}";
	local result=$?;
	if [ ! ${result} == ${TRUE} ]; then
		echo "createParentDirectories : Can't create the parent directories because ${name} is not a subdirectory of ${sourceDirectory}.";
		return;
	fi
	local suffix=${completeName#"${sourceRoot}"};
	if [ "${suffix}" == "" ]; then
#		echo "createParentDirectories : No directories to be created.";
		return;
	fi
	local inBetween=${suffix%"${name}"};
	if [ "${inBetween}" == "" ]; then
#		echo "createParentDirectories : No directories to be created.";
		return;
	fi
	local subDirectories=( `echo ${inBetween} | tr "/" "\n"` );
	local dirName="${destinationRoot}";
	for n in ${subDirectories[@]}; do
		dirName="${dirName}/${n}";
		if [ ! -d "${dirName}" ]; then
#			echo "creating directory ${dirName}";
			mkdir "${dirName}";
		fi
	done
}

function getCompletePathName(){
	if [ ! $# == 1 ]; then
		echo "completePathName : function takes 1 parameters; your provided $#.";
	fi
	local name=$1;
	local completeName=$1;
	if [ ! ${name:0:1} == "/" ]; then
		completeName="`pwd`/${name}";
	fi
	echo "${completeName}";
}

function isDirectoryEmpty(){
	if find "$1" -maxdepth 0 -empty | read;
	then
		return $TRUE;
	else
		return $FALSE;
	fi
}

function backup(){
	echo "backupDirectory = $backupDirectory";
	if [ "$backupDirectory" == "" ]; then
		echo "backupDirectory can't be empty. Quitting ..."
		return;
	fi
	if [ "$destinationRoot" == "" ] || [ "$sourceRoot" == "" ]; then
		echo "destinationRoot or sourceRoot variable can't be empty. Quitting ...";
		return;
	fi
	createParentDirectories "${backupDirectory}";
	backupDir "${backupDirectory}";
}

#backup;
