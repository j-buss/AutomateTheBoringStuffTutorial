#! /usr/bin/python3

import PyPDF2
import os
import logging
import sys
import shutil

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

def testDecryptFile(fullFilename, password):
    logging.debug("Trying to decrypt file: " + fullFilename + " with password: " + password)
    pdfReader = PyPDF2.PdfFileReader(open(fullFilename, 'rb'))
    testResponse = pdfReader.decrypt(password)
    logging.debug(testResponse)
    return testResponse

def loadPasswords(passwordFile):
    with open(passwordFile) as f:
        upperList = f.readlines()
        lowerList = [x.lower() for x in upperList]
    return upperList + lowerList

def main():
    passwordFile = sys.argv[1]
    fileToBreak = sys.argv[2]
    print("Parameters passed: ")
    print("\tPassword File: " + passwordFile)
    print("\tFile to Break: " + fileToBreak)

    passwordList = loadPasswords(os.path.abspath(passwordFile))
    logging.debug(passwordList)
    fileToBreak = os.path.abspath(fileToBreak)

    totalPasswordCount = len(passwordList)
    print("Number of passwords to test: " + str(totalPasswordCount))
    progressInterval = 1000
    progressCounter = 0
    endCounter = totalPasswordCount / progressInterval
    
    pdfReader = PyPDF2.PdfFileReader(open(fileToBreak, 'rb'))
    for i, pw in enumerate(passwordList):
        # Progress
        if i % progressInterval == 0:
            progressCounter += 1
            print(str(progressCounter) + " of " + str(endCounter) )
        testResponse = pdfReader.decrypt(pw)
        logging.debug("Test Response: " + str(testResponse))
        if testResponse:
            print("Decrypt successful of file:" + fileToBreak)
            print("Password: " + pw)

if __name__ == "__main__":
    main()
