#! /usr/bin/python3
#  Copy selective files from one directory to another. 

import os
import shutil

def prepDirectory(targetDirectory):
    targetDirectory = os.path.abspath(targetDirectory)
    subDirectory = "subDirectory"
    try:
        shutil.rmtree(targetDirectory)
    except:
        pass
    os.mkdir(targetDirectory)
    os.mkdir(os.path.join(targetDirectory,subDirectory))
    fileDicts = [
            {"base_directory": targetDirectory, "sub_directory": "", "filename": "File_01.txt", "size": 1000},
            {"base_directory": targetDirectory, "sub_directory": "", "filename": "File_02.txt", "size": 100000000},
            {"base_directory": targetDirectory, "sub_directory": "", "filename": "File_03.txt", "size": 1000000},
            {"base_directory": targetDirectory, "sub_directory": subDirectory, "filename": "File_04.txt", "size": 1000},
            {"base_directory": targetDirectory, "sub_directory": subDirectory, "filename": "File_05.txt", "size": 100000000}
    ]
    for fileObject in fileDicts:
        f = open(os.path.join(fileObject["base_directory"],fileObject["sub_directory"],fileObject["filename"]),"wb")
        f.seek(fileObject["size"] - 1)
        f.write(b"\0")
        f.close()

def selectiveDelete(targetDirectory, sizeThreshold):
    targetDirectory = os.path.abspath(targetDirectory)
    for foldername, subfolders, filenames in os.walk(targetDirectory):
        for filename in filenames:
            fullFileName = os.path.join(foldername, filename)
            fileSize = os.path.getsize(fullFileName)
            if fileSize > sizeThreshold:
                print('File: ' + filename + ' is of size: ' + str(fileSize) + \
                    ' which is larger than the threshold of : ' + str(sizeThreshold))
                os.unlink(fullFileName)

def main():
    targetDirectory = 'TESTDIR_forLargeFileDelete'
    
    # Create directory with files for testing
    prepDirectory(targetDirectory)

    # Perform the actual zip of the folder 
    selectiveDelete(targetDirectory, 100000)

if __name__ == "__main__":
    main()
