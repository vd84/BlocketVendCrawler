# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:04:47 2020

@author: Douglas
"""


from bs4 import BeautifulSoup
import requests
import schedule
import time


print('How many pages would you like to scan?')
amount_of_pages_to_scan = input()
print('What would you like to search for')
search_words = list(map(str, input().split()))
print('What would you like to pay for that?')
desired_pay_amount = int(input())


while True:
    class List_item:
        def __init__(self, item, price, link):
            self.item = item
            self.price = int(price)
            self.link = link
            
        def to_string(self):
            print('Found item with title:')
            print(self.item)
            print('With price:')
            print(self.price)
            print('Here is the link to the item:')
            print(self.link)
            print('\n')
            
        def is_affordable_for_user(self):
    
            if desired_pay_amount >= self.price:
                return True
            return False
    
    item_objs = []
    items = []
    prices = []
    links = []
    soups = []
    
    def find_titles(soup):
        for ad in soup.find_all(class_='styled__SubjectWrapper-sc-1kpvi4z-10 kZyTSM'):
            for item in ad.find_all('a'):
                #print(t.text)
                items.append(item.text)
                
    def find_prices(soup):
        sep = 'kr'
        for item in soup.find_all(class_='TextSubHeading__TextSubHeadingWrapper-sc-1ilszdp-0 jIvScq Price__Wrapper-sc-1v2maoc-0 heunWX'):
            for price in item.find_all('span'):
               price = price.text.strip()
               if price != '':
                   #print(price)
                   prices.append(price.split(sep,1)[0].strip().replace(' ', ''))
                   
    def find_links(soup):
        for ad in soup.find_all(class_='styled__SubjectWrapper-sc-1kpvi4z-10 kZyTSM'):
            for item in ad.find_all('a', href=True):
                #print('https://blocket.se' + item['href'])
                links.append('https://blocket.se' + item['href'])
    
    for i in range(1,int(amount_of_pages_to_scan) + 1):
        print(i)
        page = requests.get('https://www.blocket.se/annonser/hela_sverige?page=' + str(i))
        soups.append(BeautifulSoup(page.text, 'html.parser'))
    
    
    for soup in soups:
        find_titles(soup)
        find_prices(soup)
        find_links(soup)
    
        
    for item, price, link in zip(items, prices,links):
        item_objs.append(List_item(item = item, price = price, link = link))
        
        
    
    
    for word in search_words:
        for o in item_objs:
            if word.lower() in o.item.lower():
            
                if o.price <= desired_pay_amount:
                    o.to_string()
                else:
                    print('There is an item, but you cant afford it')
            

    time.sleep(1)



