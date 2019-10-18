#! /usr/bin/python3

import PyPDF2
import os
import logging
import sys
import shutil

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

def prepDirectory(sourceDirectory, targetDirectory):
    try:
        shutil.rmtree(targetDirectory)
    except:
        pass

    shutil.copytree(sourceDirectory, targetDirectory)

def encryptFile(foldername, filename, password):
    root, ext = os.path.splitext(filename)
    newFilename = root + "_encrypted" + ext 
    fullFilename = os.path.join(foldername, filename)
    fullNewFilename = os.path.join(foldername, newFilename)
    
    # create new filename
    logging.debug("PDF File: " + fullFilename)
    logging.debug("Creating File: " + fullNewFilename)
    pdfFile = open(fullFilename, 'rb')
    pdfWriter = PyPDF2.PdfFileWriter()
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    pdfWriter.encrypt(password)
    resultPdf = open(fullNewFilename,'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()
    return fullNewFilename

def decryptFile(foldername, filename, password):
    root, ext = os.path.splitext(filename)
    root = root.replace("_encrypt","_DECRYPT") 
    newFilename = root + ext 
    fullFilename = os.path.join(foldername, filename)
    fullNewFilename = os.path.join(foldername, newFilename)
    
    # create new filename
    logging.debug("PDF File: " + fullFilename)
    logging.debug("Creating File: " + fullNewFilename)
    
    pdfFile = open(fullFilename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfReader.decrypt(password)
    if not decryptResponse:
        print("Could not decrypt file: " + fullFilename)
    else:
        logging.debug("Decrypted file: " + fullFilename)
    
    pdfWriter = PyPDF2.PdfFileWriter()
    
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    resultPdf = open(fullNewFilename,'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()

def testDecryptFile(foldername, filename, password):
    fullFilename = os.path.join(foldername, filename)
    logging.debug("Trying to decrypt file: " + fullFilename)
    pdfReader = PyPDF2.PdfFileReader(open(fullFilename, 'rb'))
    testResponse = pdfReader.decrypt(password)
    logging.debug(testResponse)
    return testResponse


def main():
    password = sys.argv[1]
    sourceDirectory = sys.argv[2]
    logging.debug("Parameters passed: ")
    logging.debug("\tPassword: " + password)
    logging.debug("\tSourceDirectory: " + sourceDirectory)

    sourceDirectory = os.path.abspath(sourceDirectory)

    for foldername, subfolders, filenames in os.walk(sourceDirectory):
        for filename in filenames:
            logging.debug("File: " + filename)
            base, ext = os.path.splitext(filename)
            logging.debug("Splitting Filename: " + filename)
            logging.debug(base.split('_'))
            if "encrypted" in base.split('_'):
                # get file base name

                decryptFile(foldername, filename, password)
                logging.debug("Decrypt successful." + filename)

if __name__ == "__main__":
    main()
