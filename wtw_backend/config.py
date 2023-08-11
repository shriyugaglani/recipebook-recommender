from decouple import config
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
RECIPES_PATH = "./inputs/df_recipes.csv"
PARSED_PATH = "./inputs/df_parsed.csv"
TFIDF_MODEL_PATH = "./models/tfidf.pkl"
TFIDF_ENCODING_PATH = "./inputs/tfidf_encodings.pkl"

class Config:
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS',cast=bool)

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR,'dev.db')
    DEBUG=True
    SQLALCHEMY_ECHO=True

class Prod(Config):
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    SQLALCHEMY_ECHO = False
    TESTING = True
     


