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

newFileName = os.path.splitext(strFileName)[0] + "_ROWSINSERTED" + os.path.splitext(strFileName)[1]
wb.save('/mnt/chromeos/MyFiles/Downloads/' + newFileName)
