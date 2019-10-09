#! /usr/bin/python3

import os
import shutil

def prepDirectory(sourceDirectory, targetDirectory):
    sourceDirectory = os.path.abspath(sourceDirectory)
    try:
        shutil.rmtree(sourceDirectory)
        shutil.rmtree(targetDirectory)
    except:
        pass
    os.mkdir(sourceDirectory)
    open(os.path.join(sourceDirectory,'File_01.txt'),'a').close()
    open(os.path.join(sourceDirectory,'File_02.txt'),'a').close()
    open(os.path.join(sourceDirectory,'File_03.jpg'),'a').close()
    os.mkdir(os.path.join(sourceDirectory,'subDirectory'))
    open(os.path.join(sourceDirectory,'subDirectory','File_04.txt'),'a').close()
    open(os.path.join(sourceDirectory,'subDirectory','File_05.jpg'),'a').close()

def selectiveCopy(sourceDirectory, targetDirectory, fileExtension):
    sourceDirectory = os.path.abspath(sourceDirectory)
    targetDirectory = os.path.abspath(targetDirectory)
    os.mkdir(targetDirectory)
    for foldername, subfolders, filenames in os.walk(sourceDirectory):
        for filename in filenames:
            extension = os.path.splitext(filename)[1]
            if extension == fileExtension:
                fullFileName = os.path.join(foldername, filename)
                print(fullFileName)
                shutil.copy(fullFileName, targetDirectory)

def main():
    sourceDirectory = 'TESTDIR_forSelectiveCopySource'
    targetDirectory = 'TESTDIR_forSelectiveCopyTarget'
    
    # Create directory with files for testing
    prepDirectory(sourceDirectory, targetDirectory)

    # Perform the actual zip of the folder 
    selectiveCopy(sourceDirectory, targetDirectory, '.txt')

if __name__ == "__main__":
    main()
