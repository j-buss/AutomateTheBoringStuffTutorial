#! /usr/bin/python3

import os
import logging
import sys
import shutil
import csv

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

def prepDirectory(sourceDirectory, targetDirectory):
        try:
            shutil.rmtree(targetDirectory)
        except:
            pass 
        
        shutil.copytree(sourceDirectory, targetDirectory)

def reWriteCSV(filename):
    # Source File
    sourceFile = open(filename)
    sourceReader = csv.reader(sourceFile)

    # Target File
    tempFile = 'tempFile'
    targetFile = open(tempFile,'w')
    targetWriter = csv.writer(targetFile)

    # Copy each row...except for the first row
    for row in sourceReader:
        logging.debug('Row #' + str(sourceReader.line_num) + ' ' + str(row))
        if sourceReader.line_num == 1:
            pass
        else:
            targetWriter.writerow(row)

    targetFile.close()
    sourceFile.close()
    shutil.move(tempFile, filename)


if __name__ == "__main__":
    
    sourceDirectory = "TESTDIR_csvFileTemplate"
    targetDirectory = "TESTDIR_csvFiles"
    
    logging.debug("Parameters passed: ")
    logging.debug("\tSourceDirectory: " + sourceDirectory)
    logging.debug("\tTargetDirectory: " + targetDirectory)
    
    prepDirectory(sourceDirectory, targetDirectory)
    targetDirectory = os.path.abspath(targetDirectory)
    
    for foldername, subfolders, filenames in os.walk(targetDirectory):
        for filename in filenames:
             root, ext = os.path.splitext(filename)
             if ext == ".csv":
                 logging.debug(filename)
                 reWriteCSV(os.path.join(foldername,filename))
