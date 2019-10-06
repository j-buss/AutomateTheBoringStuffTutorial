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
