#! /usr/bin/python3

import os
import logging
#import sys
import shutil
import openpyxl

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

def prepDirectory(sourceDirectory, targetDirectory):
    try:
        shutil.rmtree(targetDirectory)
    except:
        pass
    
    shutil.copytree(sourceDirectory, targetDirectory)

def excelFileToCSV(targetDirectory):
    for foldername, subfolders, filenames in os.walk(targetDirectory): 
        for filename in filenames:
            fFilename = os.path.join(foldername, filename)
            logging.debug("File: " + fFilename)
            root, ext = os.path.splitext(fFilename)
            if ext == ".xlsx":
                #Load workbook object
                print("Converting workbook: " + fFilename)
                wb = openpyxl.load_workbook(fFilename)
                for sheet in wb.sheetnames:
                    print("...converting sheet: " + sheet)
                    csvFileName = root + "_" + sheet + ".csv"
                    print("Creating file: " + csvFileName)
                    targetFile = open(csvFileNAme, 'w')
                    targetWriter = csv.writer(targetFile)
                    sourceSheet = wb.get_sheet_by_name(sheet)
                    max_column = sourceSheet.max_column
                    logging.debug("Source File: %s sheet: %s Max Columns: %s", filename, sheet, max_column)
                    for column in range(1,max_column+1):

                        targetWriter.writerow(row)
                        
                    targetFile.close()

                    #wb.get_sheet_by_name(sheet)
                    # Ceate CSV filename 



    #for excelFile in os.listdir('.'):
        # Skip non-xlsx files, load the workbook object.
        #for sheetName in wb.get_sheet_names():
            # Loop through every sheet in the workbook.
            #sheet = wb.get_sheet_by_name(sheetName) 

            # Create the CSV filename from the Excel filename and sheet title.
            # Create the csv.writer object for this CSV file.  

            # Loop through every row in the sheet.
            #for rowNum in range(1, sheet.get_highest_row() + 1):
            #    rowData = []    # append each cell to this list
                # Loop through each cell in the row.
            #    for colNum in range(1, sheet.get_highest_column() + 1):
                    # Append each cell's data to rowData.  
                    pass
        
                # Write the rowData list to the CSV file.
            #csvFile.close()

if __name__ == "__main__":
    sourceDirectory = "TESTDIR_excelToCSVTemplate"
    targetDirectory = "TESTDIR_excelToCSV"
    prepDirectory(sourceDirectory, targetDirectory)
    excelFileToCSV(targetDirectory)
