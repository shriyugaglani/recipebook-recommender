import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import random
from scraping_class import Attributes


recipe_df = pd.read_csv("/Users/shriyugaglani/Desktop/WTW/wtw_backend/inputs/recipe_urls.csv")
attributes = ['recipe_title','quantity','cook_time','difficulty','ingredients']

temp_df = pd.DataFrame(columns=attributes)
for i in range(0,len(recipe_df['recipe_urls'])):
    url = recipe_df['recipe_urls'][i]
    recipe_scraper = Attributes(url)
    temp_df.loc[i] = [getattr(recipe_scraper,attribute)() for attribute in attributes]
    if i % 25 == 0:
        print(f'Recipe {i} is completed')
    time.sleep(random.randint(1,5))
    

temp_df['recipe_urls'] = recipe_df['recipe_urls']
columns = ['recipe_urls'] + attributes
temp_df = temp_df[columns]

Attributes_df = temp_df
Attributes_df.to_csv(r"/Users/shriyugaglani/Desktop/WTW/wtw_backend/inputs/full_recipes.csv",index=False)
