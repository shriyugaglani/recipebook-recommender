import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from ingredient_parser import ingredient_parser
import pickle
import config
import unidecode,ast

def get_recommendations(N,scores):
    recipes_df = pd.read_csv(config.PARSED_PATH)
    top = sorted(range(len(scores)),key=lambda x: scores[x], reverse=True)[:N]
    recommend = pd.DataFrame(columns=['recipe','ingredients','score','url'])
    count = 0
    for x in top:
        recommend.at[count,'recipe'] = parse_title(recipes_df['recipe_title'][x])
        recommend.at[count,'ingredients']= parse_ingredient(recipes_df['ingredients'][x])
        recommend.at[count,'url']=recipes_df['recipe_urls'][x]
        recommend.at[count,'score']= "{:.3f}".format(float(scores[x]))
        count +=1
        
    return recommend

def parse_title(title):
    title = unidecode.unidecode(title)
    return title

def parse_ingredient(ingred):
    if isinstance(ingred,list):
        ingredients = ingred
    else:
        ingredients = ast.literal_eval(ingred)
    ingredients = ','.join(ingredients)
    ingredients = unidecode.unidecode(ingredients)
    return ingredients

def recommendation_system(ingredients,N=5):
    with open(config.TFIDF_ENCODING_PATH,'rb') as f:
        tfidf_encodings = pickle.load(f)
    with open(config.TFIDF_MODEL_PATH,"rb") as f:
        tfidf = pickle.load(f)

    try:
        ingredients_parsed = ingredient_parser(ingredients)
    except:
        ingredients_parsed = ingredient_parser([ingredients])
    
    tfidf_ingredients = tfidf.transform([ingredients_parsed])
    
    cos_sim = map(lambda x: cosine_similarity(tfidf_ingredients,x),tfidf_encodings)
    scores = list(cos_sim)
    recommend = get_recommendations(N,scores)
    # print(recommend)
    return recommend

if __name__ == "__main__":
    test_ingredients = "potatoes, spring onion, broccoli, red pepper, eggs, cheddar cheese, spinach"
    recs = recommendation_system(test_ingredients)
    print(recs)

# input = "potatoes, spring onion, broccoli, red pepper, eggs, cheddar cheese, spinach"
# print(recommendation_system(input).recipe)
# print(recommendation_system(input).score)