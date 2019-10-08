#! /usr/bin/python3
#  Copy selective files from one directory to another. 

import os
import shutil

def prepDirectory(sourceDirectory):
    sourceDirectory = os.path.abspath(sourceDirectory)
    try:
        shutil.rmtree(sourceDirectory)
    except:
        pass
    os.mkdir(sourceDirectory)
    open(os.path.join(sourceDirectory,'File_01.txt'),'a').close()
    open(os.path.join(sourceDirectory,'File_02.txt'),'a').close()
    open(os.path.join(sourceDirectory,'File_03.jpg'),'a').close()
    os.mkdir(os.path.join(sourceDirectory,'subDirectory'))
    open(os.path.join(sourceDirectory,'subDirectory','File_04.txt'),'a').close()
    open(os.path.join(sourceDirectory,'subDirectory','File_05.jpg'),'a').close()

def selectiveCopy(sourceDirectory, targetDirectory):
    sourceDirectory = os.path.abspath(sourceDirectory)
    targetDirectory = os.path.abspath(targetDirectory)
    for foldername, subfolders, filenames in os.walk(sourceDirectory):
        for filename in filenames:
            print(filename)
            #newBase = os.path.basename(directoryPath) + '_'
            #if filename.startswith(newBase) and filename.endswith('.zip'):
            #    continue
            #backupZipFile.write(os.path.join(foldername, filename))
    #backupZipFile.close()

def main():
    sourceDirectory = 'TESTDIR_forSelectiveCopySource'
    targetDirectory = 'TESTDIR_forSelectiveCopyTarget'
    
    # Create directory with files for testing
    prepDirectory(sourceDirectory)

    # Perform the actual zip of the folder 
    selectiveCopy(sourceDirectory, targetDirectory)

if __name__ == "__main__":
    main()
