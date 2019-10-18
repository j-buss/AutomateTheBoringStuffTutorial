# Chapter 13 - DESCRIPTION
In [Chapter 13](https://automatetheboringstuff.com/chapter13/) we work with two other common types of files: PDFs and Micrsoft Word Documents.

## Summary Notes

Item|Description
----|-----------
PyPDF2|External library which can be used to read and create PDF documents



------
# Chapter X - Practice Questions
Q:1. A string value of the PDF filename is not passed to the PyPDF2.PdfFileReader() function. What do you pass to the function instead?

##### Pass in a pdfFileObject

Q:2. What modes do the File objects for PdfFileReader() and PdfFileWriter() need to be opened in?

##### The file needs to be opened in Binary mode

Q:3. How do you acquire a Page object for About This Book from a PdfFileReader object?

##### If the "About This Book" is the first page then you would call a `getPage method pageObj = pdfReader.getPage(0)`

Q:4. What PdfFileReader variable stores the number of pages in the PDF document?

##### `numPages`

Q:5. If a PdfFileReader object’s PDF is encrypted with the password swordfish, what must you do before you can obtain Page objects from it?

##### You have to use the decrypt method and supply the password; Like the following: `pdfReader.decrypt('rosebud')`

Q:6. What methods do you use to rotate a page?

##### If you have a page object defined you simply call the `rotateClockwise(90)` method to rotate clockwise 90 degrees

Q:7. What method returns a Document object for a file named demo.docx?

##### docObject = docx.Document('demo.docx')

Q:8. What is the difference between a Paragraph object and a Run object?

##### A Paragraph object contains many runs. A run is the smallest unit of information within a document. It contains text and possibly styling.

Q:9. How do you obtain a list of Paragraph objects for a Document object that’s stored in a variable named doc?

##### `doc.paragraphs`

Q:10. What type of object has bold, underline, italic, strike, and outline variables?

##### a run object

Q:11. What is the difference between setting the bold variable to True, False, or None?

##### True - the attribute is always enabled; False - the attribute is always disabled; None - defaults to the run's style

Q:12. How do you create a Document object for a new Word document?

##### Just use the `doc = docx.Document()`

Q:13. How do you add a paragraph with the text 'Hello there!' to a Document object stored in a variable named doc?

##### `doc.add_paragraph('Hello world!')`

Q:14. What integers represent the levels of headings available in Word documents?

##### 0 - 4

## PROJECT: Combinging Select Pages From Many Projects
### The following is my version of the combinePdfs.py program
```python

#! /usr/bin/python3

import PyPDF2
import os
import shutil
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

pdfDirectory = "TESTDIR_combinePDFs"
outputFilename = "/mnt/chromeos/MyFiles/Downloads/allminutes.pdf"

try:
    os.chdir(pdfDirectory)
    logging.debug("Changed Directory to: " + pdfDirectory)
except:
    logging.debug("Unable to change directory to: " + pdfDirectory)
    pass

fileList = os.listdir()
fileList = [fname for fname in fileList if ".pdf" in fname]
fileList.sort()
logging.debug(fileList)

pdfWriter = PyPDF2.PdfFileWriter()

for sourcePDF in fileList:
    pdfFile = open(sourcePDF, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)

    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    #pdfFile.close()
    logging.debug("Finished appending file: " + sourcePDF + " to the file: " + outputFilename)

pdfOutputFile = open(outputFilename,'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
```

### Al's version of combinePdfs.py

```python
#! /usr/bin/python3

import PyPDF2
import os
import logging

pdfDirectory = "TESTDIR_combinePDFs"
outputFilename = "/mnt/chromeos/MyFiles/Downloads/allminutes.pdf"

try:
    os.chdir(pdfDirectory)
    logging.debug("Changed Directory to: " + pdfDirectory)
except:
    logging.debug("Unable to change directory to: " + pdfDirectory)

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through all the pages (except the first) and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open(outputFilename, 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
```

## Practice Projects: PDF Paranoia - "Encrypt"

```python

#! /usr/bin/python3

import PyPDF2
import os
import logging
import sys
import shutil

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

def prepDirectory(sourceDirectory, targetDirectory):
    try:
        shutil.rmtree(targetDirectory)
    except:
        pass

    shutil.copytree(sourceDirectory, targetDirectory)

def encryptFile(foldername, filename, password):
    root, ext = os.path.splitext(filename)
    newFilename = root + "_encrypted" + ext 
    fullFilename = os.path.join(foldername, filename)
    fullNewFilename = os.path.join(foldername, newFilename)
    
    # create new filename
    logging.debug("PDF File: " + fullFilename)
    logging.debug("Creating File: " + fullNewFilename)
    pdfFile = open(fullFilename, 'rb')
    pdfWriter = PyPDF2.PdfFileWriter()
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    pdfWriter.encrypt(password)
    resultPdf = open(fullNewFilename,'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()
    return fullNewFilename

def testDecryptFile(foldername, filename, password):
    fullFilename = os.path.join(foldername, filename)
    logging.debug("Trying to decrypt file: " + fullFilename)
    pdfReader = PyPDF2.PdfFileReader(open(fullFilename, 'rb'))
    testResponse = pdfReader.decrypt(password)
    logging.debug(testResponse)
    return testResponse


def main():
    password = sys.argv[1]
    sourceDirectory = sys.argv[2]
    targetDirectory = sys.argv[3]
    logging.debug("Parameters passed: ")
    logging.debug("\tPassword: " + password)
    logging.debug("\tSourceDirectory: " + sourceDirectory)
    logging.debug("\tTargetDirectory: " + targetDirectory)

    prepDirectory(sourceDirectory, targetDirectory)

    #os.chdir(targetDirectory)
    targetDirectory = os.path.abspath(targetDirectory)

    for foldername, subfolders, filenames in os.walk(targetDirectory):
        #backupZipFile.write(foldername, compress_type=zipfile.ZIP_DEFLATED)
        for filename in filenames:
            #newBase = os.path.basename(directoryPath) + '_'
            logging.debug("File: " + filename)
            root, ext = os.path.splitext(filename)
            if ext == ".pdf":
                # get file base name

                encryptedFile = encryptFile(foldername, filename, password)
                if testDecryptFile(foldername, encryptedFile, password):
                    logging.debug("Decrypt test is successful. Ready to delete original file: " + filename)
                    os.unlink(os.path.join(foldername, filename))

if __name__ == "__main__":
    main()

```
## Practice Projects: PDF Paranoia - "Dencrypt"

```python
#! /usr/bin/python3

import PyPDF2
import os
import logging
import sys
import shutil

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

def prepDirectory(sourceDirectory, targetDirectory):
    try:
        shutil.rmtree(targetDirectory)
    except:
        pass

    shutil.copytree(sourceDirectory, targetDirectory)

def encryptFile(foldername, filename, password):
    root, ext = os.path.splitext(filename)
    newFilename = root + "_encrypted" + ext 
    fullFilename = os.path.join(foldername, filename)
    fullNewFilename = os.path.join(foldername, newFilename)
    
    # create new filename
    logging.debug("PDF File: " + fullFilename)
    logging.debug("Creating File: " + fullNewFilename)
    pdfFile = open(fullFilename, 'rb')
    pdfWriter = PyPDF2.PdfFileWriter()
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    pdfWriter.encrypt(password)
    resultPdf = open(fullNewFilename,'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()
    return fullNewFilename

def decryptFile(foldername, filename, password):
    root, ext = os.path.splitext(filename)
    root = root.replace("_encrypt","_DECRYPT") 
    newFilename = root + ext 
    fullFilename = os.path.join(foldername, filename)
    fullNewFilename = os.path.join(foldername, newFilename)
    
    # create new filename
    logging.debug("PDF File: " + fullFilename)
    logging.debug("Creating File: " + fullNewFilename)
    
    pdfFile = open(fullFilename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfReader.decrypt(password)
    if not decryptResponse:
        print("Could not decrypt file: " + fullFilename)
    else:
        logging.debug("Decrypted file: " + fullFilename)
    
    pdfWriter = PyPDF2.PdfFileWriter()
    
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    resultPdf = open(fullNewFilename,'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()

def testDecryptFile(foldername, filename, password):
    fullFilename = os.path.join(foldername, filename)
    logging.debug("Trying to decrypt file: " + fullFilename)
    pdfReader = PyPDF2.PdfFileReader(open(fullFilename, 'rb'))
    testResponse = pdfReader.decrypt(password)
    logging.debug(testResponse)
    return testResponse


def main():
    password = sys.argv[1]
    sourceDirectory = sys.argv[2]
    logging.debug("Parameters passed: ")
    logging.debug("\tPassword: " + password)
    logging.debug("\tSourceDirectory: " + sourceDirectory)

    sourceDirectory = os.path.abspath(sourceDirectory)

    for foldername, subfolders, filenames in os.walk(sourceDirectory):
        for filename in filenames:
            logging.debug("File: " + filename)
            base, ext = os.path.splitext(filename)
            logging.debug("Splitting Filename: " + filename)
            logging.debug(base.split('_'))
            if "encrypted" in base.split('_'):
                # get file base name

                decryptFile(foldername, filename, password)
                logging.debug("Decrypt successful." + filename)

if __name__ == "__main__":
    main()
```

## Practice Projects: Doc Invitations

```python


#! /usr/bin/python3

import docx
import logging
import sys
import readDocx

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

guestListFilename = sys.argv[1]
invTempFilename = sys.argv[2]

def getGuestList(guestListFilename):
    with open(guestListFilename) as f:
        guestList = f.readlines()
    return guestList

#def getParagraphs(doc):

def other():
    doc = docx.Document(invTempFilename)
    doc.add_paragraph("Hello World!")
    paraObj1 = doc.add_paragraph("This is a second paragraph")
    paraObj2 = doc.add_paragraph("This is a yet another paragraph")
    paraObj1.add_run("This text is being added to the second paragraph")

    doc.save("helloworld_multipleParagraphs.docx")

if __name__ == "__main__":
    logging.debug(readDocx.getText(invTempFilename))
    gl = getGuestList(guestListFilename)
    logging.debug("Guest List:" )
    logging.debug(gl)

    templateDocList = []
    doc = docx.Document(invTempFilename)

    # Build Document Items
    for i, para in enumerate(doc.paragraphs):
        logging.debug("Index number: " + str(i))
        logging.debug(para.style.name)
        logging.debug(para.text)
        templateDocList.append({"text":para.text,"style":para.style.name,"alignment":para.alignment})
    logging.debug(templateDocList)

    doc2 = docx.Document()
    for guest in gl:
        logging.debug("Working on invitation for: " + guest)
        for paragraph in templateDocList:
            if paragraph['text'] == "[NAME]":
                doc2.add_paragraph(guest,style=paragraph['style'])
            else:
                doc2.add_paragraph(paragraph['text'],style=paragraph['style'])
        doc2.add_page_break()
    doc2.save('FinishedInvitations.docx')

```

## Practice Projects: PDF Password Cracker

```python
