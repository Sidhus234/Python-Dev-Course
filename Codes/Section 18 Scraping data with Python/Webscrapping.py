# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 07:09:04 2021

@author: sidhu
"""

# data: https://news.ycombinator.com/

import requests
from bs4 import BeautifulSoup

# requests allow us to download data
res = requests.get('https://news.ycombinator.com/news')

print(res.text)

# Beautiful soup allows us to parse this string
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.body.contents)

print(soup.find_all('div'))

# 'a': links
print(soup.find_all('a'))

print(soup.title)

print(soup.a)

print(soup.find('a'))
