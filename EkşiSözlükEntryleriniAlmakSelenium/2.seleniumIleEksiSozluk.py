# -*- coding: utf-8 -*-
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

baslık = input("hangi baslıgı aramak istiyorsun")

d = webdriver.Chrome()

time.sleep(2)

d.get("https://eksisozluk.com/")

time.sleep(2)

input_area = d.find_element_by_class_name("ui-autocomplete-input")

button = d.find_element_by_xpath("//*[@id='search-form']/button")

time.sleep(1)

input_area.send_keys(baslık)
time.sleep(1)
button.click()

url = d.current_url

source = d.page_source

soup = BeautifulSoup(source,"html.parser")

try:
    page_count = len(soup.find("div",{"class":"clearfix sub-title-container"}).find("div",{"class":"pager"}).find_all("option"))

except:
    page_count = 1

print(page_count)

headers={'user-agent': 'Ozgur Kucet'}
for i in range(1,page_count +1):
    response = requests.get(url + "?p=" +str(i),headers = headers)
    time.sleep(1)
    soup = BeautifulSoup(response.content,"html.parser")
    entry_divs = soup.find_all("div",{"class":"content"})
    for entry in entry_divs:
        print(entry.text)
        footer = entry.findNext("footer")
        author = footer.find_all("a")[1].text
        print("yazar: "+author)
        print("*"*100)


