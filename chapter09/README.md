# Chapter 9 - Organizing Files
In [Chapter ](https://automatetheboringstuff.com/chapter/) 

## Accompanying Videos:
- [Lesson 9 - def Statements, arguments, and the None value](https://www.youtube.com/watch?v=WB4hJJkfhLU)
- [Lesson 10 - Global Scope and Local Scope](https://www.youtube.com/watch?v=M-CoVBK_bLE)
- [Lesson 11 - Error Handling](https://www.youtube.com/watch?v=qS0UkqaYmfU)
- [Lesson 12 - Writing a Guess the Number Game](https://www.youtube.com/watch?v=48WXHT0dfEY)

# Summary Notes

Item|Description
----|-----------
shutil library|module with functions to copy, move, rename and delete files in python programs
shutil.copy(_source_,_destination_)|copy the file at the path _source_ to the folder at path _destination_
shutil.copytree(_source_,_destination_)|create a new folder named _destination_ with the same content as the original _source_ folder
shutil.move(_source_,_destination_)|move the file at the path _source_ to the folder at path _destination_
os.unlink(_path_)|delete the file at _path_
os.rmdir(_path_)|delete the folder at _path_; folder must be empty
shutil.rmtree(_path_)|remove the folder at _path_ and all files and folders it contains will also be deleted
send2trash library|small package that sends files to the Trash (or Recycle Bin) natively and on all platforms
os.walk(_path_)|function to recursively walk the contents of a folder
zipfile module|tools provided to create, read, write, append and list a ZIP file
ZipFileObject.extractall(optional _path_)|extract the files into the current working directory; optionally you can add a file path to a location other than current diretory
ZipFileObject.extract(_filename_)|extract a single file from the ZIP file
ZipFileObject.close()|close the zip file



## Zipfile Example:
```python
import zipfile
import os
os.chdir('\tmp')
#Create some files...

# Create a zip file...
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('\tmp\*', compress_type=zipfile.ZIP_DEFLATED)

# Now Unzip it
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()
exampleZip.extractall('\tmp\test_my_zip_extract')
exampleZip.close()
```
------
# Chapter X - Practice Questions

Q:1. What is the difference between shutil.copy() and shutil.copytree()?

##### shutil.copy() will copy one file; shutil.copytree() will copy an entire folder and every folder and file contained in it

Q:2. What function is used to rename files?

##### the shutil.move(_source_,_destination_) function will move the file at the path _source_ to the _destination_

Q:3. What is the difference between the delete functions in the send2trash and shutil modules?

##### the os.remove(_filepath_) or os.unlink(_filepath_) will remove the file; however the send2trash.send2trash(_filepath_) will remove the file and send it to the trash/recycle bin of the native system

Q:4. ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?

##### The zipfile.ZipFile(_filepath_, _write/read/append flag_) will 'open' the file ready for processing

-----

## Project: Renaming Files with American-Style Dates to European-Style Dates

### My own design, before reading Al's Solution:

```python
#! /usr/bin/python3
#Rename Files with American-Style Dates to European-Style Dates

import re
import os
import shutil

def prepDirectory(directoryPath):
    directoryAbsPath = os.path.abspath(directoryPath)
    try:
        shutil.rmtree(directoryAbsPath)
    except:
        pass
    os.mkdir(directoryAbsPath)
    open(os.path.join(directoryAbsPath,'10-01-2019.txt'),'a').close()
    open(os.path.join(directoryAbsPath,'ExtraPrefix10-01-2019ExtraSuffix.txt'),'a').close()
    open(os.path.join(directoryAbsPath,'2019-10-01.txt'),'a').close()


def renameAmericanDates(directoryPath):
    # Create regex for American Style Date
    americanDateRegex = re.compile(r'''^(.*?)   # all text before the date
        ((0|1)?\d)-                         # one or two digits for the month
         ((0|1|2|3)?\d)-                     # one or two digits for the day
         ((19|20)\d\d)                       # four digits for the year
         (.*?)$                              # all text after the date
         ''', re.VERBOSE)

    # Find all files in the working directory
    directoryAbsPath = os.path.abspath(directoryPath)
    try:
        os.chdir(directoryAbsPath)
    except:
        print('Could not change directory to : ' + directoryAbsPath)

    for filename in os.listdir():
        fullFileName = os.path.join(directoryAbsPath,filename)
        mo = americanDateRegex.search(filename)

        print('\n--------------------')
        if mo is not None:
            prefix = mo.group(1) + '-'
            if prefix == '-':
                prefix = ''
            newFileName = prefix + mo.group(4) + '-' + mo.group(2) + '-' + mo.group(6) + mo.group(8)
            newFullFileName = os.path.join(directoryAbsPath, newFileName)
            shutil.move(fullFileName, newFullFileName)
            
            print('''Renamed file: ''' + fullFileName + ''' To: ''' + newFullFileName)
        else:
            print('''File: ''' + filename + ''' does not have American date format: 'MM-DD-YYYY''')

def main():
    directoryName = 'TESTDIR_forRenameDates'
    prepDirectory(directoryName)
    renameAmericanDates(directoryName)

if __name__ == "__main__":
    main()
```

### From the book...

```python
#! /usr/bin/python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil, os, re

directory = 'TESTDIR_forRenameDates'

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?)  # all text before the date
    ((0|1)?\d)-                      # one or two digits for the month
    ((0|1|2|3)?\d)-                  # one or two digits for the day
    ((19|20)\d\d)                    # four digits for the year
    (.*?)$                           # all text after the date
    """, re.VERBOSE)
# Loop over the files in the working directory.
for amerFilename in os.listdir(directory):
    mo = datePattern.search(amerFilename)
    
    # Skip files without a date.
    if mo == None:
        continue
    
    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)
    
    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    
    # Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename)   # uncomment after testing
```

## Project: Backing Up a Folder into a Zip File

### My Solution. (I did need to use some of the book's logic on the os.walk. I originally had a `zipFile.write(directoryPath)`, but that only zipped an empty directory

```python
#! /usr/bin/python3
#  Create a zip of an entire folder to be used as a backup. Increment the number suffice of the zip file name to keep as archive.

import re
import os
import shutil
import zipfile

def prepDirectory(directoryPath):
    directoryAbsPath = os.path.abspath(directoryPath)
    try:
        shutil.rmtree(directoryAbsPath)
    except:
        pass
    os.mkdir(directoryAbsPath)
    open(os.path.join(directoryAbsPath,'File_01.txt'),'a').close()
    open(os.path.join(directoryAbsPath,'File_02.txt'),'a').close()
    open(os.path.join(directoryAbsPath,'File_03.txt'),'a').close()
    os.mkdir(os.path.join(directoryAbsPath,'newDirectory'))
    open(os.path.join(directoryAbsPath,'newDirectory','File_03.txt'),'a').close()

def nextFileName(directoryPath, baseFileName):
    strNewSuffix = '01'
    zipRegex = re.compile(r'''
        (^\w+)
        (_(\d{2}))
        (.zip)
        ''',re.VERBOSE)

    fileList = os.listdir()
    for f in fileList:
        mo = zipRegex.search(f)
        if mo is not None:
            suffix = int(mo.group(3))
            newSuffix = suffix + 1
            strNewSuffix = str(newSuffix).rjust(2,'0')
    return baseFileName + '_' + strNewSuffix + '.zip'

def zipFolderBackup(directoryPath, zipFileName):
    backupZipFile = zipfile.ZipFile(zipFileName, 'w')
    
    for foldername, subfolders, filenames in os.walk(directoryPath):
        backupZipFile.write(foldername, compress_type=zipfile.ZIP_DEFLATED)
        for filename in filenames:
            newBase = os.path.basename(directoryPath) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZipFile.write(os.path.join(foldername, filename))
    backupZipFile.close()

def main():
    directoryName = 'TESTDIR_forBackupToZip'
    baseFileName = 'backupZip'
    
    # Create directory with files for testing
    prepDirectory(directoryName)

    # Determine file name 
    zipFileName = nextFileName(directoryName,baseFileName)
    
    # Perform the actual zip of the folder 
    zipFolderBackup(directoryName, zipFileName)

if __name__ == "__main__":
    main()
```

### Book's Solution

```python
#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder) # make sure folder is absolute
    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the ZIP file.
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue   # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

backupToZip('/home/jeremyfbuss/AutomateTheBoringStuffTutorial/chapter09/TESTDIR_forBackupToZip')
```

## Practice Projects: Selective Copy

## Practice Projects: Deleting Unneeded Files

## Practice Projects: Filling in the Gaps

