# Chapter X - DESCRIPTION
In [Chapter ](https://automatetheboringstuff.com/chapter/) 

## Accompanying Videos:
- [Lesson 9 - def Statements, arguments, and the None value](https://www.youtube.com/watch?v=WB4hJJkfhLU)
- [Lesson 10 - Global Scope and Local Scope](https://www.youtube.com/watch?v=M-CoVBK_bLE)
- [Lesson 11 - Error Handling](https://www.youtube.com/watch?v=qS0UkqaYmfU)
- [Lesson 12 - Writing a Guess the Number Game](https://www.youtube.com/watch?v=48WXHT0dfEY)

## Summary Notes

- blab: blab blab blab
Item|Description
----|-----------
os.path.join('usr','bin')|function to create path for folder/file based on os conventions ('\\' vs. '/')
os.path.sep|returns the path separator for the system based on OS convention
os.getcwd()|return the current working directory
os.chdir(_path_)|change the directory to _path_
os.makedirs(_path_)|make directory
os.path.abspath(_path_)|return string of absolute path of _path_
os.path.isabs(_path_)|return True if argument is an absolute path, False if argument is relative
os.path.relpath(_path_, _start_)|return string of relative path from _start_ to _path_
os.path.basename(_path_)|return the basename of the _path_ argument
os.path.dirname(_path_)|return the directory name of the _path_ argument
os.path.split(_path_)|return a tupe of directory name and basename of the _path_ argumenti
os.path.getsize(_path_)|return size in bytes
os.path.listdir(_path_)|return list of filename strings
os.path.exists(_path_)|return True if file or folder exists 
os.path.isfile(_path_)|return True if exists and is a file
os.path.isdir(_path_)|return True if exists and is a directory
open(_path_,_mode_)|open the file passed as _path_ argument in the _mode_ (default is r=read mode, w=write plaintext, a=append) and returns a File Object
read(_path_)|return a string value of the content of the file passed as argument
readlines(_path_)|return a list of string values from the file, one string for each line of text
write(_path_)|write to the file object passed as read the file passed as argument
close(_path_)|close the file object passed as argument
shelve library|a simple persistent storage option for Python objects when a relational db is overkill; the shelf is accessed by keys, just as with a dictionary 
shelve.open(_file_)|open a shelve object
pprint.pformat(_obj_)|return pretty print contents of text as string; could store in file to load as module

------
# Chapter 8 - Practice Questions
Q:1. What is a relative path relative to?

##### A relative path is relative to the current working directory

Q:2. What does an absolute path start with?

##### An absolute path starts with the drive (e.g. "C:", "D:" on windows and "/" on linux)

Q:3. What do the os.getcwd() and os.chdir() functions do?

##### the os.getcwd() function will return a string with the absolute path of the current working directory; the os.chdir(_path_) function will change the current working directory to the _path_ variable that is passed as an argument

Q:4. What are the . and .. folders?

##### the dot (.) and the dot-dot (..) folders are not real folders but special names that can be used in the path for (.) "this directory" and (..) "parent directory"

Q:5. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?

##### the basename is the file or "spam.txt" and the dir name is everything before that; namely "C:\bacon\eggs"

Q:6. What are the three “mode” arguments that can be passed to the open() function?

##### read mode (r), write mode (w) and append mode (a)

Q:7. What happens if an existing file is opened in write mode?

##### it will overwrite the file and start it from scratch

Q:8. What is the difference between the read() and readlines() methods?

##### the read() method will load all of the content into one string; but readlines() will load each line of the file into a list object

Q:9. What data structure does a shelf value resemble?

##### a relational database

------
## Project: Generating Random Quiz Files

## Project: Multiclipboard

## Practice Projects: Extending the Multiclipboard

## Practice Projects: Mad Libs

## Practice Projects: Regex Search

