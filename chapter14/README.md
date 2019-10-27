# Chapter 14 - Working with CSV Files and JSON Data
In [Chapter 14](https://automatetheboringstuff.com/chapter14/) we work with 2 different types of text files. CSV and JSON. Both of which have a certain structure and are used extensively today.

## Summary Notes

Item|Description
----|---------
CSV|Library to handle CSV files
JSON|Library to read / parse JSON files

------
# Chapter X - Practice Questions
Q:1. What are some features Excel spreadsheets have that CSV spreadsheets don’t?

#### CSV files simply have text, separated by commas; Whereas Excel spreadsheets can have formatting, styling, formulas etc.

Q:2. What do you pass to csv.reader() and csv.writer() to create Reader and Writer objects?

#### A file object

Q:3. What modes do File objects for reader and Writer objects need to be opened in?

##### reader object needs a file in read mode and writer needs a file object in write mode

Q:4. What method takes a list argument and writes it to a CSV file?

##### writerow

Q:5. What do the delimiter and lineterminator keyword arguments do?

##### delimiter tells the object that will be used as a delimiter between cells and lineterminator designates the object used to terminate lines

Q:6. What function takes a string of JSON data and returns a Python data structure?

##### json.loads

Q:7. What function takes a Python data structure and returns a string of JSON data?

##### json.dumps

## Project: Remove Header from CSV Files - My Version

```python
#! /usr/bin/python3

import os
import logging
import sys
import shutil
import csv

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

def prepDirectory(sourceDirectory, targetDirectory):
        try:
            shutil.rmtree(targetDirectory)
        except:
            pass 
        
        shutil.copytree(sourceDirectory, targetDirectory)

def reWriteCSV(filename):
    # Source File
    sourceFile = open(filename)
    sourceReader = csv.reader(sourceFile)

    # Target File
    tempFile = 'tempFile'
    targetFile = open(tempFile,'w')
    targetWriter = csv.writer(targetFile)

    # Copy each row...except for the first row
    for row in sourceReader:
        logging.debug('Row #' + str(sourceReader.line_num) + ' ' + str(row))
        if sourceReader.line_num == 1:
            pass
        else:
            targetWriter.writerow(row)

    targetFile.close()
    sourceFile.close()
    shutil.move(tempFile, filename)


if __name__ == "__main__":
    
    sourceDirectory = "TESTDIR_csvFileTemplate"
    targetDirectory = "TESTDIR_csvFiles"
    
    logging.debug("Parameters passed: ")
    logging.debug("\tSourceDirectory: " + sourceDirectory)
    logging.debug("\tTargetDirectory: " + targetDirectory)
    
    prepDirectory(sourceDirectory, targetDirectory)
    targetDirectory = os.path.abspath(targetDirectory)
    
    for foldername, subfolders, filenames in os.walk(targetDirectory):
        for filename in filenames:
             root, ext = os.path.splitext(filename)
             if ext == ".csv":
                 logging.debug(filename)
                 reWriteCSV(os.path.join(foldername,filename))
```

## Project: Remove Header from CSV Files - Al's Version

```python
#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory.

import csv
import os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue    # skip non-csv files
    
    print('Removing header from ' + csvFilename + '...')

    # Read the CSV file in (skipping first row).
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue    # skip first row
        csvRows.append(row)
    csvFileObj.close()
    
    # Write out the CSV file.
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()

```
## Project: Fetching Current Weather Data - My Version

```python


#! /usr/bin/python3

import json
import logging
import sys
import requests
import config_OWM
import collections
import datetime
from dateutil.parser import parse

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

def convertKelvinToFahrenheit(inputKelvin):
    celsius = inputKelvin - 273.15
    logging.debug(celsius)
    fahrenheit = (9/5 * celsius) + 32
    logging.debug(fahrenheit)
    return round(fahrenheit,2)

def printCurrent(currentJSON):
    print("\n----------------------")
    print("Forecast for: " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("\t" + currentJSON["weather"][0]["description"])
    kelvinTemp = convertKelvinToFahrenheit(currentJSON["main"]["temp"])
    logging.debug("\tTemperature (K): " + str(currentJSON["main"]["temp"]))
    print("\tTemperature (F): " + str(convertKelvinToFahrenheit(currentJSON["main"]["temp"])))
    logging.debug("\n-----------------")
    logging.debug(currentJSON)
    return None

def printForecast(forecastJSON):
    targetTime = datetime.time(hour=12,minute=0)
    targetForecasts = []
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow2 = tomorrow + datetime.timedelta(days=1)
    targetDT = datetime.datetime.combine(tomorrow,targetTime)
    targetDT2 = datetime.datetime.combine(tomorrow2,targetTime)
    targetForecasts.append(targetDT)
    targetForecasts.append(targetDT2)

    for forecast in forecastJSON["list"]:
        if parse(forecast["dt_txt"]) in targetForecasts:
            logging.debug("Found Match: " + str(targetDT))
            logging.debug(forecast)
            print("\n----------------------")
            print("Forecast for: " + forecast["dt_txt"])
            print("\t" + forecast["weather"][0]["description"])
            kelvinTemp = forecast["main"]["temp"]
            logging.debug("\tTemperature (K): " + str(kelvinTemp))
            print("\tTemperature (F): " + str(convertKelvinToFahrenheit(kelvinTemp)))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: quickWeather.py apiName zipCode')
        sys.exit()

    apiName = sys.argv[1]
    zipCode = sys.argv[2]

    if apiName == "forecast":
        URL = "https://api.openweathermap.org/data/2.5/forecast"
    else:
        URL = "https://api.openweathermap.org/data/2.5/weather"

    logging.debug(config_OWM.api_key)
    params = collections.OrderedDict([('zip',zipCode),('APPID',config_OWM.api_key)])

    r = requests.get(URL, params=params)
    r.raise_for_status()
    
    weatherData = json.loads(r.text)
    if apiName == "forecast":
        printForecast(weatherData)
    else:
        printCurrent(weatherData)

```

## Practice Project: Excel-to-csv Converter

```python

#! /usr/bin/python3

import os
import logging
#import sys
import csv
import shutil
import openpyxl
from openpyxl.utils import get_column_letter

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

def prepDirectory(sourceDirectory, targetDirectory):
    try:
        shutil.rmtree(targetDirectory)
    except:
        pass
    
    shutil.copytree(sourceDirectory, targetDirectory)

def ExcelToCSVFile(fullFilename, rootFilename):
    print("Converting workbook: " + fullFilename)
    wb = openpyxl.load_workbook(fullFilename)
   
    for sheet in wb.sheetnames:
        
        # For each Sheet
        print("...converting sheet: " + sheet)
        csvFileName = rootFilename + "_" + sheet + ".csv"
        print("Creating file: " + csvFileName)
        sourceSheet = wb.get_sheet_by_name(sheet)
        # How many columns does current sheet have?
        sheetMaxColumn = sourceSheet.max_column
        # How many rows does current sheet have?
        sheetMaxRow = sourceSheet.max_row
       
        # Create Target File 
        targetFile = open(csvFileName, 'w')
        targetWriter = csv.writer(targetFile)
        
        logging.debug("Source File: %s sheet: %s Max Columns: %s Max Rows: %s", 
                fullFilename, sheet, sheetMaxColumn, sheetMaxRow)

        for row in range(1,sheetMaxRow+1):
            rowArray = []
            for column in range(1,sheetMaxColumn):
                logging.debug(sourceSheet.cell(row=row,column=column).value)
                rowArray.append(sourceSheet.cell(row=row,column=column).value)

            logging.debug(rowArray)

            targetWriter.writerow(rowArray)
    targetFile.close()


def ExcelToCSVDirectory(targetDirectory):
    for foldername, subfolders, filenames in os.walk(targetDirectory): 
        for filename in filenames:
            fFilename = os.path.join(foldername, filename)
            logging.debug("File: " + fFilename)
            root, ext = os.path.splitext(fFilename)
            
            if ext == ".xlsx":
                #Load workbook object
                ExcelToCSVFile(fFilename,root)

if __name__ == "__main__":
    sourceDirectory = "TESTDIR_excelToCSVTemplate"
    targetDirectory = "TESTDIR_excelToCSV"
    prepDirectory(sourceDirectory, targetDirectory)
    ExcelToCSVDirectory(targetDirectory)

```
