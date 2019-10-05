#! /usr/bin/python3
#  Rename Files with American-Style Dates to European-Style Dates

import re
import os
import shutil

def prepDirectory(directoryPath):
    directoryAbsPath = os.path.abspath(directoryPath)
    try:
        shutil.rmtree(directoryAbsPath)
    except:
        pass
    os.mkdir(directoryAbsPath)
    open(os.path.join(directoryAbsPath,'10-01-2019.txt'),'a').close()
    open(os.path.join(directoryAbsPath,'ExtraPrefix10-01-2019ExtraSuffix.txt'),'a').close()
    open(os.path.join(directoryAbsPath,'2019-10-01.txt'),'a').close()


def renameAmericanDates():
    # TODO: create regex for American Style Date
    americanDateRegex = re.compile(r'''^(.*?)   # all text before the date
         ((0|1)?\d)-                         # one or two digits for the month
         ((0|1|2|3)?\d)-                     # one or two digits for the day
         ((19|20)\d\d)                       # four digits for the year
         (.*?)$                              # all text after the date
         ''', re.VERBOSE)

    # TODO: find all files in the working directory
    os.chdir('dir_forRenameDates')
    for filename in os.listdir():
        mo = americanDateRegex.search(filename)
        try:
            prefix = mo.group(1) + '-'
            if prefix == '-':
                prefix = ''
            print(prefix + mo.group(4) + '-' + mo.group(2) + '-' + mo.group(6) + mo.group(8))
        except:
            print('no american date name found here')

def main():
    directoryName = 'TESTDIR_forRenameDates'
    prepDirectory(directoryName)
    #renameAmericanDates(directoryName)

if __name__ == "__main__":
    main()
