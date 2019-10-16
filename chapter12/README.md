# Chapter 12 - Working with Excel Spreadsheets
In [Chapter 12](https://automatetheboringstuff.com/chapter12/) we learn the art of working with Excel spreadsheets with python. 

## Summary Notes

Item|Description
----|-----------
openpyxl|Python module to work with Excel spreadsheet files


### Example openpyxl

```python
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
# A sheet has the following methods: sheet.max_row, sheet.max_column
c = sheet['A1']
# A cell has the following methods: c.row, c.column, c.coordinate

# cycle through rows...
for rowOfCellObjects in sheet.rows:
    for cellObj in rowOfCellObjects:
	print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')
```

## PROJECTS: Reading Data From a Spreadsheet
Q:1. What does the openpyxl.load_workbook() function return?

##### A Workbook object

Q:2. What does the get_sheet_names() workbook method return?

##### A list with the sheet names in it

Q:3. How would you retrieve the Worksheet object for a sheet named 'Sheet1'?

##### wb.get_sheet_by_name('Sheet1')

Q:4. How would you retrieve the Worksheet object for the workbook’s active sheet?

##### wb.active()

Q:5. How would you retrieve the value in the cell C5?

##### sheet['C5'].value

Q:6. How would you set the value in the cell C5 to "Hello"?

##### sheet['C5'].value = "Hello"

Q:7. How would you retrieve the cell’s row and column as integers?

##### c.row and c.column

Q:8. What do the max_column and max_row sheet methods return, and what is the data type of these return values?

##### The return values are the last row and column of data entered into a sheet; the return values are integers

Q:9. If you needed to get the integer index for column 'M', what function would you need to call?

##### column\_index\_from\_string("M")

Q:10. If you needed to get the string name for column 14, what function would you need to call?

##### get_column_letter(14)

Q:11. How can you retrieve a tuple of all the Cell objects from A1 to F1?

##### sheet['A1':'F1']

Q:12. How would you save the workbook to the filename example.xlsx?

##### wb.save('example.xlsx')

Q:13. How do you set a formula in a cell?

##### sheet['A1'] = '=SUM(B1:B10)'

Q:15. How would you set the height of row 5 to 100?

##### sheet.row\_dimensions[5].height = 100

Q:16. How would you hide column C?

##### sheet.column\_dimensions['C'].hidden = True

Q:17. Name a few features that OpenPyXL 2.3.3 does not load from a spreadsheet file.

##### It does not load charts, 

Q:18. What is a freeze pane?

#### An update to the sheet which holds some rows or columns static even as you scroll through the sheet

Q:19. What five functions and methods do you have to call to create a bar chart?

##### Create Reference Object, Create Series Object, Create Chart Object, Appent Series Object to Chart Object, Add Chart Object to Worksheet object

## Practice Projects

### Multiplcation Table Maker

```python
#! /usr/bin/python3
# multiplicationTable.py - take number N from command line and create NxN multiplication table in spreadsheet

import openpyxl
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter
import pprint
import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

intMultiplier = int(sys.argv[1])
intMaxRow = intMultiplier + 1
strMaxColumn = get_column_letter(intMaxRow) 

logging.debug("Multiplier: %s MaxRow: %s MaxColumn: %s", str(intMultiplier), str(intMaxRow), strMaxColumn)
logging.disable(logging.CRITICAL)

print('Opening workbook...')
wb = openpyxl.Workbook()
sheet = wb.active
fontObj1 = Font(bold=True)

# loop over Rows
for row in range(1,intMaxRow):
    for column in range(1,intMaxRow): # use same counter since it is a square
        sheet.cell(row=row,column=column).value = row * column

sheet.insert_rows(1)
sheet.insert_cols(1)

for column in range(2,intMaxRow+1):
    sheet.cell(row=1,column=column).font = fontObj1
    sheet.cell(row=1,column=column).value = column - 1

for row in range(2,intMaxRow+1):
    sheet.cell(row=row,column=1).font = fontObj1
    sheet.cell(row=row,column=1).value = row - 1

wb.save('/mnt/chromeos/MyFiles/Downloads/multiplicationTable_Output.xlsx')
```

### Blank Row Inserter

```python

#! /usr/bin/python3
# blankRowInserter.py - take an existing spreadsheet and insert a number of rows at a certain row number

import openpyxl
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter
import pprint
import logging
import sys
import os

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

intStartingRow = int(sys.argv[1])
intNumberOfEmptyRows = int(sys.argv[2])
strFileName = sys.argv[3]

print('Opening workbook...')
wb = openpyxl.load_workbook(strFileName)
sheet = wb.active

sheet.insert_rows(intStartingRow, amount=intNumberOfEmptyRows)

newFileName = os.path.splitext(strFileName)[0] + "\_ROWSINSERTED" + os.path.splitext(strFileName)[1]
wb.save('/mnt/chromeos/MyFiles/Downloads/' + newFileName)

```

### Spreadsheet Cell Inverter

```python

#! /usr/bin/python3
# invertSpreadsheet.py

import openpyxl
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter
import pprint
import logging
import sys
import os

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

strFileName = sys.argv[1]
newFileName = os.path.splitext(strFileName)[0] + "_INVERTED" + os.path.splitext(strFileName)[1]

logging.disable(logging.CRITICAL)

sourceWB = openpyxl.load_workbook(strFileName)
sourceSheet = sourceWB.active

targetWB = openpyxl.Workbook()
targetSheet = targetWB.active

max_row = sourceSheet.max_row
max_columns = sourceSheet.max_column

# loop over Rows
for row in range(1,max_row+1):
    for column in range(1,max_columns+1): # use same counter since it is a square
        targetSheet.cell(row=column,column=row).value = sourceSheet.cell(row=row,column=column).value

targetWB.save('/mnt/chromeos/MyFiles/Downloads/' + newFileName)
```

## Text Files to Spreadsheet

```python

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
```

### Spreadsheet to Text Files

```python

#! /usr/bin/python3
# textFileToSpreadsheet.py

import openpyxl
from openpyxl.utils import get_column_letter
import logging
import os
import glob

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)


sourceFileName = "TextToExcel.xlsx"
sourceWB = openpyxl.load_workbook(sourceFileName)
sourceSheet = sourceWB.active

# Max Colum is the number of files that will be created. It can be known at the beginning
max_column = sourceSheet.max_column
logging.debug("Source File: %s found to have the following.... Max Columns: %s",sourceFileName, str(max_column))

# loop over Rows
for column in range(1,max_column+1): 
    outputFileName = 'ExcelToText' + str(column) + '.txt'

    maxRowsCurrentColumn = len(sourceSheet[get_column_letter(column)])
    logging.debug("Current Column: " + str(column))
    logging.debug("Current Column: " + get_column_letter(column))
    logging.debug("Max Rows in Current Column: " + str(maxRowsCurrentColumn))
    with open(outputFileName, 'a') as the_file:
        logging.debug("Opened file: " + outputFileName)
        for row in range(1,maxRowsCurrentColumn+1):
            try:
                the_file.write(sourceSheet.cell(row=row,column=column).value)
                logging.debug(sourceSheet.cell(row=row,column=column).value)
            except:
                pass
```
