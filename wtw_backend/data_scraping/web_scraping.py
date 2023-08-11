import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

url = "https://www.jamieoliver.com/recipes/category/special-diets/vegetarian/"

page = requests.get(url)
soup = BeautifulSoup(page.text,"html.parser")

recipe_urls_df = pd.DataFrame()

food_cater = ["mains","snacks","desserts","breakfast"]

recipe_urls = pd.Series([a.get("href") for a in soup.find_all("a")])
recipe_urls = recipe_urls[
    (recipe_urls.str.count("-")>0) &
    (recipe_urls.str.contains("/recipes/")==True) &
    (recipe_urls.str.contains("-recipes/")==True) &
    (recipe_urls.str.contains("course")==False) &
    (recipe_urls.str.contains("books")==False) &
    (recipe_urls.str.endswith("recipes/")==False)
].unique()
# print(recipe_urls[0:5])
df = pd.DataFrame({'recipe_urls':recipe_urls})
df['recipe_urls'] = "https://www.jamieoliver.com" + df['recipe_urls'].astype('str')
recipe_urls_df = pd.concat((recipe_urls_df,df),axis=1)
# print(recipe_urls_df[0:5].to_string())

recipe_urls_df.to_csv(r"/Users/shriyugaglani/Desktop/WTW/wtw_backend/inputs/recipe_urls.csv",sep="\t",index=False)