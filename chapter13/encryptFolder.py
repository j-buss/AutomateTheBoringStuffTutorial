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
    targetDirectory = sys.argv[3]
    logging.debug("Parameters passed: ")
    logging.debug("\tPassword: " + password)
    logging.debug("\tSourceDirectory: " + sourceDirectory)
    logging.debug("\tTargetDirectory: " + targetDirectory)

    prepDirectory(sourceDirectory, targetDirectory)

    #os.chdir(targetDirectory)
    targetDirectory = os.path.abspath(targetDirectory)

    for foldername, subfolders, filenames in os.walk(targetDirectory):
        #backupZipFile.write(foldername, compress_type=zipfile.ZIP_DEFLATED)
        for filename in filenames:
            #newBase = os.path.basename(directoryPath) + '_'
            logging.debug("File: " + filename)
            root, ext = os.path.splitext(filename)
            if ext == ".pdf":
                # get file base name

                encryptedFile = encryptFile(foldername, filename, password)
                if testDecryptFile(foldername, encryptedFile, password):
                    logging.debug("Decrypt test is successful. Ready to delete original file: " + filename)
                    os.unlink(os.path.join(foldername, filename))
                #root, ext = os.path.splitext(filename)
                #newFilename = root + "_encrypted" + ext
                #fullFilename = os.path.join(foldername, filename)
                #fullNewFilename = os.path.join(foldername, newFilename)

                # create new filename
                #logging.debug("PDF File: " + fullFilename)
                #logging.debug("Creating File: " + fullNewFilename)
                #pdfFile = open(fullFilename, 'rb')
                #pdfWriter = PyPDF2.PdfFileWriter()
                #pdfReader = PyPDF2.PdfFileReader(pdfFile)
                #for pageNum in range(pdfReader.numPages):
                #    pdfWriter.addPage(pdfReader.getPage(pageNum))
                #pdfWriter.encrypt(password)
                #resultPdf = open(fullNewFilename,'wb')
                #pdfWriter.write(resultPdf)
                #resultPdf.close()

if __name__ == "__main__":
    main()
