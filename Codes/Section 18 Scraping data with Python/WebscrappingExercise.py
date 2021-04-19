# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 06:37:44 2021

@author: sidhu
"""

# Grab title and link of the story that has more than 100 points

import requests
from bs4 import BeautifulSoup
import pprint

# requests allow us to download data
res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.storylink')

subtext = soup.select('.subtext')

def get_data_till_page(page_number):
    links = []
    subtext = []
    for page in range(1, page_number+1):
        res = requests.get(f'https://news.ycombinator.com/news?p={page}')
        soup = BeautifulSoup(res.text, 'html.parser')
        links = links + soup.select('.storylink')
        subtext = subtext + soup.select('.subtext')
    return links, subtext

links, subtext = get_data_till_page(2)

def sort_by_votes(hnlist):
    return sorted(hnlist, key=lambda item: item.get("votes"), reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        points = 0
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if(points > 99):
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_by_votes(hn)

hn = create_custom_hn(links, subtext)
#hn.sort(key=lambda item: item.get("votes"), reverse=True)
pprint.pprint(hn)