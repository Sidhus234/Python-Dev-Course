# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 06:33:16 2021

@author: sidhu
"""

# Selectors: https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors

import requests
from bs4 import BeautifulSoup

# requests allow us to download data
res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

print(soup.select('div'))

# Select all classes of score (.)
print(soup.select('.score'))


print(soup.select('#score_26867300'))
