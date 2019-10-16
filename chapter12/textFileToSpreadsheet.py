#! /usr/bin/python3
# textFileToSpreadsheet.py

import openpyxl
import logging
import os
import glob

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

dirList = glob.glob("text*.txt")
logging.debug(dirList)
targetWB = openpyxl.Workbook()
targetSheet = targetWB.active
targetFileName = "TextToExcel.xlsx"

for columnCounter, fileName in enumerate(dirList):
    logging.debug(fileName)
    #columnCounter += 1 #Have to "convert" the columnCounter for 0 based to 1 based counter
    rowCounter = 1 #Note - This counter starts at 1 to track row count in Excel
    with open(fileName, 'r') as f:
        lineOfText = f.readline()
        rowCounter = 1
        while lineOfText:
            logging.debug(lineOfText)
            targetSheet.cell(row=rowCounter,column=columnCounter+1).value = lineOfText
            lineOfText = f.readline()
            rowCounter += 1

targetWB.save(targetFileName)
targetWB.save('/mnt/chromeos/MyFiles/Downloads/' + targetFileName)
