#! /usr/bin/python3

## Zipfile Example:
import zipfile
import os
os.chdir('/tmp')

#Create some files...
test_filename = 'test_filename_'
for i in range(10):
    test_file = open(test_filename + str(i) + '.txt', 'w')
    test_file.write('hello world this is test file #' + str(i))
    test_file.close()

# Create a zip file...
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('test_filename_0.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

# Now Unzip it
exampleZip = zipfile.ZipFile('new.zip')
exampleZip.extractall('test_my_zip_extract')
exampleZip.close()
