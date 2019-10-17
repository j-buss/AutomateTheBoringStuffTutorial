#! /usr/bin/python3

import PyPDF2
import os
import shutil
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

pdfDirectory = "TESTDIR_combinePDFs"
outputFilename = "allminutes.pdf"

try:
    os.chdir(pdfDirectory)
    logging.debug("Changed Directory to: " + pdfDirectory)
except:
    logging.debug("Unable to change directory to: " + pdfDirectory)
    pass

try:
    os.unlink(outputFilename)
    logging.debug("Deleted file: " + outputFilename)
except:
    logging.debug("Unable to delete file: " + outputFilename)
    pass

fileList = os.listdir()
fileList = [fname for fname in fileList if ".pdf" in fname]
fileList.sort()
logging.debug(fileList)

pdf1File = open('meetingminutes.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinedminutes.pdf','wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
