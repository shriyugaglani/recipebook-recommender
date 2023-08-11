import requests
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np
import re

headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

class Attributes():
    def __init__(self,url):
        self.url = url
        self.soup = BeautifulSoup(requests.get(url,headers=headers).content,'html.parser')

    def recipe_title(self):
        try:
            return self.soup.find('h1').text.strip()
        except:
            return np.nan
        
    def quantity(self):
        try:
            return self.soup.find('div',{'class':'recipe-detail serves'}).text.split(' ',1)[1]
        except:
            return np.nan

    def cook_time(self):
        try:
            return self.soup.find('div',{'class':'recipe-detail time'}).text.split('In',1)[1]
        except:
            return np.nan
        
    def difficulty(self):
        try:
            return self.soup.find('div',{'class':'col-md-12 recipe-details-col remove-left-col-padding-md'}).text.split('Difficulty')[1]
        except:
            return np.nan

    def ingredients(self):
        try:
            ingredients = []
            for li in self.soup.select('.ingred-list li'):
                ingred = ' '.join(li.text.split())
                ingredients.append(ingred)
            return ingredients
        except:
            np.nan

'''TESTING'''
# url = "https://www.jamieoliver.com/recipes/vegetable-recipes/potato-pepper-and-broccoli-frittata/"
# soup = BeautifulSoup(requests.get(url).content,'html.parser')

# ingredients = []
# for li in soup.select('.ingred-list li'):
#     ingred = ' '.join(li.text.split())
#     ingredients.append(ingred)
# print(ingredients)

# diff = soup.find('div',{'class':'col-md-12 recipe-details-col remove-left-col-padding-md'}).text.split('Difficulty')[1]
# print(diff)

# times = soup.find('div',{'class':'recipe-detail time'}).text.split('In',1)[1]
# print(times)

# quant = soup.find('div',{'class':'recipe-detail serves'}).text.split(' ',1)[1]
# print(quant)

# title = soup.find('h1').text.strip()
# print(title)