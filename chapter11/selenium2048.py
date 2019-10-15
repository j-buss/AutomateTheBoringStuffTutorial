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
