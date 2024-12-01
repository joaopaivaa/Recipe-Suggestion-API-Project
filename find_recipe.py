from fastapi import APIRouter
from base_models import IngredientsRequest
import json
import pandas as pd

df = pd.read_csv('C:\\Users\\joaov\\Documents\\Recipe Suggestion API Project\\recipes_data_cleaned.csv')

router = APIRouter()

@router.post('/find_recipe')
def find_recipe(data:IngredientsRequest):
    ingredients = data.ingredients
    recipes_found = []
    for i in range (len(df)):
        items = df['NER'][i]
        ingredients_in_recipe = 0
        for ingredient in ingredients:
            for item in json.loads(items):
                if ingredient.lower() in item.lower():
                    ingredients_in_recipe += 1
        if ingredients_in_recipe == len(json.loads(items)):
            recipes_found.append(i)
    df_recipes = df.iloc[recipes_found,:].reset_index(drop=True)
    if df_recipes.empty:
        return "There is no recipe that matches all of your ingredients."
    if len(df_recipes) > 5:
        df_recipes = df_recipes.head()
    return df_recipes.to_dict()

@router.post('/find_my_ingredients')
def find_my_ingredients(data:IngredientsRequest):
    ingredients = data.ingredients
    recipes_found = []
    for i in range (len(df)):
        items = df['NER'][i]
        ingredients_in_recipe = 0
        for ingredient in ingredients:
            for item in json.loads(items):
                if ingredient.lower() in item.lower():
                    ingredients_in_recipe += 1
        if ingredients_in_recipe == len(ingredients):
            recipes_found.append(i)
    df_recipes = df.iloc[recipes_found,:].reset_index(drop=True)
    if df_recipes.empty:
        return "Your ingredients weren't found in any recipe"
    if len(df_recipes) > 5:
        df_recipes = df_recipes.head()
    return df_recipes.to_dict()