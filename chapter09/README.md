# Chapter 9 - Organizing Files
In [Chapter ](https://automatetheboringstuff.com/chapter/) 

## Accompanying Videos:
- [Lesson 9 - def Statements, arguments, and the None value](https://www.youtube.com/watch?v=WB4hJJkfhLU)
- [Lesson 10 - Global Scope and Local Scope](https://www.youtube.com/watch?v=M-CoVBK_bLE)
- [Lesson 11 - Error Handling](https://www.youtube.com/watch?v=qS0UkqaYmfU)
- [Lesson 12 - Writing a Guess the Number Game](https://www.youtube.com/watch?v=48WXHT0dfEY)

# Summary Notes

Item|Description
----|-----------
shutil library|module with functions to copy, move, rename and delete files in python programs
shutil.copy(_source_,_destination_)|copy the file at the path _source_ to the folder at path _destination_
shutil.copytree(_source_,_destination_)|create a new folder named _destination_ with the same content as the original _source_ folder
shutil.move(_source_,_destination_)|move the file at the path _source_ to the folder at path _destination_
os.unlink(_path_)|delete the file at _path_
os.rmdir(_path_)|delete the folder at _path_; folder must be empty
shutil.rmtree(_path_)|remove the folder at _path_ and all files and folders it contains will also be deleted
send2trash library|small package that sends files to the Trash (or Recycle Bin) natively and on all platforms
os.walk(_path_)|function to recursively walk the contents of a folder
zipfile module|tools provided to create, read, write, append and list a ZIP file
ZipFileObject.extractall(optional _path_)|extract the files into the current working directory; optionally you can add a file path to a location other than current diretory
ZipFileObject.extract(_filename_)|extract a single file from the ZIP file
ZipFileObject.close()|close the zip file



## Zipfile Example:
```python
import zipfile
import os
os.chdir('\tmp')
#Create some files...

# Create a zip file...
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('\tmp\*', compress_type=zipfile.ZIP_DEFLATED)

# Now Unzip it
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()
exampleZip.extractall('\tmp\test_my_zip_extract')
exampleZip.close()
```
------
# Chapter X - Practice Questions

Q:1. What is the difference between shutil.copy() and shutil.copytree()?

##### shutil.copy() will copy one file; shutil.copytree() will copy an entire folder and every folder and file contained in it

Q:2. What function is used to rename files?

##### the shutil.move(_source_,_destination_) function will move the file at the path _source_ to the _destination_

Q:3. What is the difference between the delete functions in the send2trash and shutil modules?

##### the os.remove(_filepath_) or os.unlink(_filepath_) will remove the file; however the send2trash.send2trash(_filepath_) will remove the file and send it to the trash/recycle bin of the native system

Q:4. ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?

##### The zipfile.ZipFile(_filepath_, _write/read/append flag_) will 'open' the file ready for processing

-----

## Project: Renaming Files with American-Style Dates to European-Style Dates


## Project: Backing Up a Folder into a Zip File

## Practice Projects: Selective Copy

## Practice Projects: Deleting Unneeded Files

## Practice Projects: Filling in the Gaps

