from flask_restx import Namespace,Resource,fields
from models import Recipe
from flask import request,jsonify,make_response
from flask_jwt_extended import jwt_required
import pandas as pd
import config, recommendation_system
from ingredient_parser import ingredient_parser
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



recipe_ns = Namespace('recipes',description='A namespace for Recipes')

fridge_ns = Namespace('fridge',description='A namespace for ingredients-based recipes')

recipe_model = recipe_ns.model(
    "Recipe",
    {
        "id":fields.Integer(),
        "title":fields.String(),
        "description":fields.String()
    }
)


@recipe_ns.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {"message": "Hello, World!"}
    
@fridge_ns.route('/fridge')
class FridgeResource(Resource):
    def get(self):
        ingredients = request.args.get('ingredients')
        recipes = recommendation_system.recommendation_system(ingredients)

        res = {}
        count = 0
        for index, row in recipes.iterrows():
            res[count] = {
                'recipe' : str(row['recipe']),
                'score' : str(row['score']),
                'ingredients' : str(row['ingredients']),
                'url' : str(row['url'])
            }
            count += 1
        return jsonify(res)

    
@recipe_ns.route('/recipes')
class RecipesResource(Resource):
    @recipe_ns.marshal_list_with(recipe_model)
    def get(self):
        recipes = Recipe.query.all()

        return recipes
    
    @recipe_ns.marshal_with(recipe_model)
    @recipe_ns.expect(recipe_model)
    @jwt_required()
    def post(self):
        data = request.get_json()
        new_recipe = Recipe(
            title = data.get('title'),
            description = data.get('description')
        )
        new_recipe.save()
        return new_recipe,201

@recipe_ns.route('/recipe/<int:id>')
class RecipeResource(Resource):
    @recipe_ns.marshal_with(recipe_model)
    def get(self,id):
        recipe = Recipe.query.get_or_404(id)
        return recipe
    
    @recipe_ns.marshal_with(recipe_model)
    @jwt_required()
    def put(self,id):
        recipe_to_update = Recipe.query.get_or_404(id)
        data = request.get_json()
        recipe_to_update.update(data.get('title'),data.get('description'))
        return recipe_to_update
    
    @recipe_ns.marshal_with(recipe_model)
    @jwt_required()
    def delete(self,id):
        recipe_to_delete = Recipe.query.get_or_404(id)
        recipe_to_delete.delete()
        return recipe_to_delete