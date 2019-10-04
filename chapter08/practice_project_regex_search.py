import re
import os

def main():
    folderpath = input('Enter the folder path: ')
    search_string = input('Enter the string to search for: ')
    
    # ensure path is absolute
    folderpath = os.path.abspath(folderpath)

    for filename in os.listdir(folderpath):
        if filename[-4:] == '.txt':
            absolute_filename = os.path.join(folderpath, filename)
            with open(absolute_filename, "r") as f:
                found_lines = []
                fileHasLine = False
                for line in f:
                    if search_string in line:
                        fileHasLine = True
                        found_lines.append(line)
                if fileHasLine == True:
                    print(absolute_filename)
                    for x in range(len(found_lines)):
                        print(found_lines[x])

if __name__ == "__main__":
    main()
