import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import config

recipes_df = pd.read_csv(config.PARSED_PATH)
recipes_df['ingredients_parsed'] = recipes_df.ingredients_parsed.values.astype('U')

tfidf = TfidfVectorizer()
tfidf.fit(recipes_df['ingredients_parsed'])
recipes_tfidf = tfidf.transform(recipes_df['ingredients_parsed'])

with open(config.TFIDF_MODEL_PATH,"wb") as f:
    pickle.dump(tfidf,f)

with open(config.TFIDF_ENCODING_PATH,"wb") as f:
    pickle.dump(recipes_tfidf,f)

