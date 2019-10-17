#! /usr/bin/python3

import PyPDF2
import os
import shutil
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

pdfDirectory = "TESTDIR_combinePDFs"
outputFilename = "/mnt/chromeos/MyFiles/Downloads/allminutes.pdf"

try:
    os.chdir(pdfDirectory)
    logging.debug("Changed Directory to: " + pdfDirectory)
except:
    logging.debug("Unable to change directory to: " + pdfDirectory)
    pass

fileList = os.listdir()
fileList = [fname for fname in fileList if ".pdf" in fname]
fileList.sort()
logging.debug(fileList)

pdfWriter = PyPDF2.PdfFileWriter()

for sourcePDF in fileList:
    pdfFile = open(sourcePDF, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)

    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    #pdfFile.close()
    logging.debug("Finished appending file: " + sourcePDF + " to the file: " + outputFilename)

pdfOutputFile = open(outputFilename,'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
