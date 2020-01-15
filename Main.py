
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests


print('How many pages would you like to scan?')
amount_of_pages_to_scan = input()
print('What would you like to search for')
search_words = list(map(str, input().split()))


items = []
prices = []
ulist = []
soups = []

for i in range(1,int(amount_of_pages_to_scan) + 1):
    print(i)
    page = requests.get('http://vend.se?page=' + str(i))
    soups.append(BeautifulSoup(page.text, 'html.parser'))


for soup in soups:
    ulist = soup.find(class_='list')
    all_items = soup.find_all('li')
    products = soup.find_all(class_='t')
    item_prices = soup.find_all(class_='p')
    
    
    for price in item_prices:
        prices.append(price.text[:-2])
        
    for item in products:
        items.append(item.find('a').text)
            
item_dict = dict(zip(items, prices))

for word in search_words:
    for item in item_dict:
        if word.lower() in item.lower():
            print('Found item:')
            print(item)
            print('With price:')
            print(item_dict.get(item))
            print('\n')

    

# Pull all text from the BodyText div
ulist = soup.find(class_='list')
all_items = soup.find_all('li')
items = soup.find_all(class_='t')
item_prices = soup.find_all(class_='p')


