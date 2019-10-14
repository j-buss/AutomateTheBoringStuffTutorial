#! /usr/bin/python3

from selenium import webdriver
browser = webdriver.Chrome('/usr/bin/chromedriver')
browser.get('https://www.petfinder.com/search/dogs-for-adoption/us/wi/west-bend/')
breedElem = browser.find_element_by_id('breed-autosuggest_List_Box_Btn')
breedElem.send_keys('Poodle')
ageElem = browser.find_element_by_id('age-select_List_Box_Btn')
ageElem.send_keys('Adult')
ageElem.submit()
