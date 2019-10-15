# Chapter 11 - Web Scraping
In [Chapter 11](https://automatetheboringstuff.com/chapter11/) we examine the ways to interact with websites in a programatic way starting very basic then progressing in complexity.

## Summary Notes

Item|Description
----|-----------
webbrowser|comes with python and opens a browser to a specific page
Requests|HTTP for Humans; an elegant and simple HTTP library for Python, built for human beings
raise_for_status()|call to check response from requests call
Beautiful Soup|Library to parse HTML
Selenium|Launches and controls a web browser; Selenium is able to fill in forms and simulate mouse clicks
[ChromeDriver](https://chromedriver.chromium.org/)|An open source WebDriver for Chrome

## Beautiful Soup Reference

Method|Description
------|----------
soup.select('div')|All elements named <div> 
soup.select('#author')|The element with an id attribute of author
soup.select('.notice')|All elements that use a CSS class attribute named notice
soup.select('div span')|All elements named <span> that are within an element named <div>
soup.select('div > span')|All elements named <span> that are directly within an element named <div>, with no other element in between
soup.select('input[name]')|All elements named <input> that have a name attribute with any value
soup.select('input[type="button"]')|All elements named <input> that have an attribute named type with value button

### Selenium Reference

Item|Description
----|-----------
browser.find_element_by_class_name(name) or "elements"|Elements that use the CSS class name
browser.find_element_by_css_selector(selector) or "elements"|Elements that match the CSS selector
browser.find_element_by_id(id) or "elements"|Elements with a matching id attribute value
browser.find_element_by_link_text(text)|<a> elements that completely match the text provided
browser.find_element_by_partial_link_text(text)|<a> elements that contain the text provided
browser.find_element_by_name(name)| Elements with a matching name attribute value
browser.find_element_by_tag_name(name)| Elements with a matching tag name (case insensitive; an <a> element is matched by 'a' and 'A')
tag_name|The tag name, such as 'a' for an <a> element
get_attribute(name)| The value for the element’s name attribute
text|The text within the element, such as 'hello' in <span>hello</span>
clear()| For text field or text area elements, clears the text typed into it
is_displayed()| Returns True if the element is visible; otherwise returns False
is_enabled()| For input elements, returns True if the element is enabled; otherwise returns False
is_selected()| For checkbox or radio button elements, returns True if the element is selected; otherwise returns false
location| A dictionary with keys 'x' and 'y' for the position of the element in the page
Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT| The keyboard arrow keys
Keys.ENTER, Keys.RETURN| The ENTER and RETURN keys
Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP| The home, end, pagedown, and pageup keys
Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE| The ESC, BACKSPACE, and DELETE keys
Keys.F1, Keys.F2,..., Keys.F12| The F1 to F12 keys at the top of the keyboard
Keys.TAB| The TAB key

------
# Chapter 11 - Practice Questions
Q:1. Briefly describe the differences between the webbrowser, requests, BeautifulSoup, and selenium modules.

Item|Description
----|-----------
webbrowser|comes with python and opens a browser to a specific page
Requests|Described as "HTTP for Humans"; simple library for Python to interact with HTTP protocol; programatically GET, POST
Beautiful Soup|Library to parse HTML and extract data
Selenium|Launches and controls a web browser; Selenium is able to fill in forms and simulate mouse clicks

Q:2. What type of object is returned by requests.get()? How can you access the downloaded content as a string value?

##### A response object is returned. To get the string value from response use the .text method

Q:3. What Requests method checks that the download worked?

##### the raise_for_status() method

Q:4. How can you get the HTTP status code of a Requests response?

##### By accessing the response.status_code

Q:5. How do you save a Requests response to a file?

##### You need to save the text to a file by iterating over the content. 

```python
#! /usr/bin/python3

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
```

Q:6. What is the keyboard shortcut for opening a browser’s developer tools?

##### Within Chrome you can use the shortcut Shift+Control+c

Q:7. How can you view (in the developer tools) the HTML of a specific element on a web page?

##### If you "right-click" on the web page in the certain area you can pick "Inspect Element" from the drop down list

Q:8. What is the CSS selector string that would find the element with an id attribute of main?

##### soup.select('#main')

Q:9. What is the CSS selector string that would find the elements with a CSS class of highlight?

##### soup.select('.highlight')

Q:10. What is the CSS selector string that would find all the <div> elements inside another <div> element?

##### soup.select('div div')

Q:11. What is the CSS selector string that would find the <button> element with a value attribute set to favorite?

##### soup.select('button[value="favorite"]')

Q:12. Say you have a Beautiful Soup Tag object stored in the variable spam for the element <div>Hello world!</div>. How could you get a string 'Hello world!' from the Tag object?

##### tag.getText()

Q:13. How would you store all the attributes of a Beautiful Soup Tag object in a variable named linkElem?

##### linkElem = tagObject[0].attrs

Q:14. Running import selenium doesn’t work. How do you properly import the selenium module?

```python
from selenium import webdriver
```

Q:15. What’s the difference between the find\_element\_\* and find\_elements\_\* methods?

##### find\_element\_\* will find the first element and find\_elements\_\* will return a list

Q:16. What methods do Selenium’s WebElement objects have for simulating mouse clicks and keyboard keys?

##### There are methods which simulate the mouse clicks: click() on a specific element; keyboard keys can be simulated by the following: [Keys.DOWN, Keys.UP, Keys.LEFT, etc.]

Q:17. You could call send_keys(Keys.ENTER) on the Submit button’s WebElement object, but what is an easier way to submit a form with Selenium?

##### calling submit() on any element

Q:18. How can you simulate clicking a browser’s Forward, Back, and Refresh buttons with Selenium?

##### With the browser methods: [browser.back(), browser.forward(), etc...] 

## PROJECT: Mapit.py with the WebBrowser Module

```python
#! /usr/bin/python3

import sys
import webbrowser
import re
import logging
import pyperclip

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

# lkupAddress contains address string for google maps; explicitly start with "empty string"
lkupAddress = ""

if len(sys.argv) > 1:
    logging.debug('Command line arguments given')
    # Loop through command line arguments; after the program name which is sys.argv[0]
    for i, argument in enumerate(sys.argv[1:],1):
        argument = re.sub('[\.\,]','',argument)
        logging.debug('Command line argument number: ' + str(i) + ' value: ' + argument)
        lkupAddress += argument + "+"

    # Add last "/" after removing last "+"
    lkupAddress = lkupAddress[:-1] + "/"
else:
    logging.debug('No command line arguments given. Using clipboard.')
    lkupAddress = pyperclip.paste()

logging.debug('Using the following address for lookup: ' + lkupAddress)
webbrowser.open('https://www.google.com/maps/place/' + lkupAddress)
```

## PROJECT: myLucky.py - search google; open up the top few links in a new webbrowser page;
### This version is my own; completed before looking at Al's solution in the book

```python
#! /usr/bin/python3
# Commandline argument is the search term; Google search the term; Open top N links in new tabs

import logging
from bs4 import BeautifulSoup
import requests
import webbrowser
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

def returnSoup(pageURL, headers):
    req = requests.get(pageURL, headers)
    req.raise_for_status()
    soup = BeautifulSoup(req.text, "html.parser")
    return soup

def saveSoup(soupObject, fileName):
    with open(fileName, 'w') as f:
        f.write(soupObject.prettify())

def fileToSoup(fileName):
    with open(fileName, 'r') as f:
        strFile = f.read()
    logging.debug("First 500 bytes of file: " + fileName + "\n\n--------------------\n\n" + strFile[:500])
    return BeautifulSoup(strFile, "html.parser")

def returnGoogleLinks(soupObject):
    elems = soupObject.find_all("div",{"class":"kCrYT"})

    logging.debug("Number of elements found: " + str(len(elems)))
    for i, link in enumerate(elems):
        try:
            subElems = elems[i].find_all("a", href=True)

            logging.debug("---------\nNumber of links found: " + str(len(subElems)))
            if len(subElems) > 0:
                for link in subElems:
                    rawLink = link['href']
                    startLink = link['href'].find('q=') + 2
                    endLink = link['href'].find('&sa=')
                    formattedLink = link['href'][startLink:endLink]
                    if formattedLink[:4] == "http":
                        print("Found link: " + formattedLink)
                        webbrowser.open(formattedLink)

            logging.debug("---------\n")
        except:
            continue

if __name__ == "__main__":
    # Get Search Keyword from commandline
    if len(sys.argv) < 2:
        print("Please enter a command line search term")

    searchTerm = ' '.join(sys.argv[1:])
    logging.debug("[Non-trivial] Commandline arg is: " + searchTerm)

    # Setup requests parameters
    baseURL = "https://google.com/search?q="
    url = baseURL + searchTerm
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
   
    # fName = "temporary_google_results.txt"
    # temporarySoup = returnSoup(url, headers)
    # saveSoup(temporarySoup,fName) 
    # temporarySoup = fileToSoup(fName)
    returnGoogleLinks(returnSoup(url, headers))
```

## PROJECT: Download all the Xkcd comic images
#### This version is my own. Completed prior to reviewing Al's solution in the book. As the book was written some time ago, my version seems to handle a few more situations and does download all images (except for composite images/videos etc.)

```python
#! /usr/bin/python3
# Following the motivation of the "Automate the Boring Stuff" book by Al Sweigart. 
# This is my own code to download all the web comics from Xkcd http://xkcd.com.  
# I didn't consult Al's version until mine was working

import logging
from bs4 import BeautifulSoup
import requests
import sys
import os
import shutil

logging.basicConfig(filename='myDownloadXkcdLog.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

def prepDirectory(directoryPath):
    directoryAbsPath = os.path.abspath(directoryPath)
    try:
        shutil.rmtree(directoryAbsPath)
    except:
        pass
    os.mkdir(directoryAbsPath)

def returnXkcdImageURL(soupObject):
    """For an Xkcd page; return the link to the image"""
    comicURL = "http:" + soupObject.find("div", {"id":"comic"}).find("img")['src']
    logging.debug("ComicURL: " + comicURL)
    return comicURL

def downloadImage(folder, imageURL, headers):
    """Download and image given the specific URL"""
    req = requests.get(imageURL, headers)
    req.raise_for_status()
    fileName = os.path.split(imageURL)[1]
    directoryAbsPath = os.path.abspath(folder)
    fileName = os.path.join(directoryAbsPath, fileName)
    logging.debug("Full path: " + imageURL)
    logging.debug("Filename: " + fileName)
    with open(fileName, 'wb') as f:
        for chunk in req.iter_content(100000):
            f.write(chunk)
            logging.debug("Downloaded image: " + fileName)

def returnPrevURL(soupObject, baseURL):
    """Return the link to the previous Xkcd comic page"""
    previousLink = soupObject.find("div", {"id":"middleContainer"}).find("a",{"rel":"prev"})['href']
    fullPreviousLink = baseURL + previousLink
    logging.debug("Found previous link: " + fullPreviousLink)
    return fullPreviousLink, previousLink

def returnSoup(pageURL, headers):
    req = requests.get(pageURL, headers)
    req.raise_for_status()
    soup = BeautifulSoup(req.text, "html.parser")
    return soup

def dailyXkcd(folder, url, headers):
    """Perform the step to find the image url, download it, and return link to previous page"""
    tempSoup = returnSoup(url, headers)
    try:
        imageURL = returnXkcdImageURL(tempSoup)
        downloadImage(folder, imageURL, headers)
    except:
        logging.warning("Couldn't get Image from: " + url)
        pass
    fullPrevURL, prevURL = returnPrevURL(tempSoup, xkcdBaseURL)
    return fullPrevURL, prevURL

if __name__ == "__main__":
    xkcdBaseURL = "https://xkcd.com"
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    imageDirectory = 'TESTDIR_forXkcdImages'
    prepDirectory(imageDirectory)
    
    # Get Xkcd information for current webpage
    fullPrevURL, prevURL = dailyXkcd(imageDirectory, xkcdBaseURL,headers)

    count = 0
    while prevURL:
        fullPrevURL, prevURL = dailyXkcd(imageDirectory, fullPrevURL, headers)
        prevURL = prevURL.strip("/")
        count += 1
        logging.debug(prevURL)
        if count % 100 == 0:
            print("Image count download: " + str(count))
            print("Latest prevURL: " + str(prevURL))
        if prevURL == str(1):
            break
```

## PROJECT: Download all the Xkcd comic images
#### This version is Al's from the book.

```python
#! /usr/bin/python3
# myDownloadxkcd.py - downloads every single XKCD comic.

import requests
import os
import bs4

url = 'http://xkcd.com'
directory = 'TESTDIR_xkcd'
os.makedirs(directory, exist_ok=True)
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
    
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip this comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue

        # Save the image to ./xkcd.
        imageFile = open(os.path.join(directory, os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # TODO: Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')


print('Done.')
```

## Practice Project: Image Site Downloader

```python
#! /usr/bin/python3

# This notebook is to accompany the Automate The Boring Stuff chapter 11.  
# This code is my build of the "Practice Project" Image Site Downloader. 
# Specifically it downloads the first 8 images from a reddit subreddit

import logging
from bs4 import BeautifulSoup
import requests
import sys
import os
import shutil
from urllib.parse import urlparse

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)
def prepDirectory(directoryPath):
    directoryAbsPath = os.path.abspath(directoryPath)
    try:
        shutil.rmtree(directoryAbsPath)
    except:
        pass
    os.mkdir(directoryAbsPath)

def returnSoup(pageURL):
    req = requests.get(pageURL)
    req.raise_for_status()
    soup = BeautifulSoup(req.text, "html.parser")
    return soup

def downloadImage(folder, imageURL):
    # Clean up the imageURL
    a = urlparse(imageURL)
    parsedURL = a.path 
    fileName = os.path.basename(a.path)
    downloadURL = "https://i.redd.it/" + fileName
    logging.debug("----------------------")
    logging.debug("Raw URL: " + imageURL)
    logging.debug("URL Parsed: " + parsedURL)
    logging.debug("Filename: " + fileName)
    logging.debug("DownloadURL: " + downloadURL)
    
    # Download the content
    req = requests.get(downloadURL)
    req.raise_for_status()
    directoryAbsPath = os.path.abspath(folder)
    fileName = os.path.join(directoryAbsPath, fileName)
    with open(fileName, 'wb') as f:
        for chunk in req.iter_content(100000):
            f.write(chunk)
    logging.debug("Downloaded image: " + fileName)
    logging.debug("\n")

if __name__ == "__main__":
    
    baseURL = "http://www.reddit.com/r/itookapicture/"
    imageDirectory = 'TESTDIR_forRedditImages'
    prepDirectory(imageDirectory)
    tempSoup = returnSoup(baseURL)
    elems = tempSoup.find_all("img", {"alt":"Post image"})

    for i in elems:
        rawImageURL = i['src']
        logging.debug(rawImageURL)
    try:
        downloadImage(imageDirectory, rawImageURL)
    except:
        logging.warning("Couldn't get Image from: " + imageURL)
        pass
```

## Practice Project: 2048

```python
#! /usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def runQuadArrows():
    htmlElem.send_keys(Keys.UP)     # scrolls to bottom
    htmlElem.send_keys(Keys.DOWN)     # scrolls to bottom
    htmlElem.send_keys(Keys.LEFT)     # scrolls to bottom
    htmlElem.send_keys(Keys.RIGHT)     # scrolls to bottom

if __name__ == "__main__":
    browser = webdriver.Chrome('/usr/bin/chromedriver')
    browser.get('https://gabrielecirulli.github.io/2048/')
    htmlElem = browser.find_element_by_tag_name('html')
    for i in range(100):
        runQuadArrows()
```

## Practice Project: Link Verification

```python
#! /usr/bin/python3
# Get all links from a page and check their status

import requests
import sys
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

def returnSoup(pageURL, headers):
    req = requests.get(pageURL, headers)
    req.raise_for_status()
    soup = BeautifulSoup(req.text, "html.parser")
    return soup

def cleanLink(rawLink):
    startLink = rawLink.find('http')
    endLink = rawLink.find('&sa=')
    formattedLink = rawLink[startLink:endLink]
    return formattedLink

def printFailedLink(url, headers):
    req = requests.get(url, headers)
    if not req.ok:
        print("Failed link: " + url)

if __name__ == "__main__":
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

    url = "https://google.com/search?q=python"
    tempSoup = returnSoup(url, headers)

    for a in tempSoup.find_all("a", href=True):
        rawLink = a['href']
        if "http" in rawLink:
            cleanedLink = cleanLink(rawLink)
            logging.debug("Found the URL: " + cleanedLink)
            try:
                printFailedLink(cleanedLink, headers)
            except:
                print("Could not verify link: " + cleanedLink)
```
