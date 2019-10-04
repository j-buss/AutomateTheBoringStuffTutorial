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

## Zipfile Example:
```python
import zipfile
import os
os.chdir('\tmp')
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()
```

------
# Chapter X - Practice Questions
Q:1. QUESTION STUFF

