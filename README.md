# backup
This set of scripts allows you to efficiently backup your data on to another location. The main addition w.r.t. an exhaustive copy is that the script recursively explores the directories and copies only those files and directories which have been updated since their last backup. This saves some time.

Contents:
---------
    backup.py: This file doesn't need to be modified.
    backup_iiitb.py: Prototype configuration for creating your own custom backup.
    README.md: This file

Instructions for Use:
---------------------
1. Set up
Let us say that you wish to create a backup script to copy your personal data to your external hard-disk. Follow the following steps:
- Copy backup_iiitb.py (above) to backup_personal.py
        cp backup_iiitb.py backup_personal.py
- Open backup_personal.py in your favourite editor.
- The first step is to set up the source and destination root directory. This is done by setting the values of the variables 'sourceRoot' and 'destinationRoot' to appropriate values.
- Next is to set up the list of backup directories. These are subdirectories of the source root directory which you wish to be backed up. The entries in the 'backDirectories' list variable are some examples. Note that all these directories must be descendent directories of the 'sourceRoot' directory. Also, it is not necessary for them to be direct sub-directory fo 'sourceRoot' directory. You may select any directory at an arbitrary depth of nesting. All you have to take care is that it should be within the 'sourceRoot' directory.
There! You are done!

2. Running the backup script
Just run the backup_personal.py
        ./backup_personal.py

3. You can create arbitrary number of backup scripts following the above steps. For example, backup_office.py, backup_music.py etc.
