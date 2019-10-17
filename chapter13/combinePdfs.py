#! /usr/bin/python3

import PyPDF2
import os
import logging

pdfDirectory = "TESTDIR_combinePDFs"
outputFilename = "/mnt/chromeos/MyFiles/Downloads/allminutes.pdf"

try:
    os.chdir(pdfDirectory)
    logging.debug("Changed Directory to: " + pdfDirectory)
except:
    logging.debug("Unable to change directory to: " + pdfDirectory)

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through all the pages (except the first) and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open(outputFilename, 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
