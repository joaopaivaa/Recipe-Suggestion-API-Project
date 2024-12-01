from pydantic import BaseModel, Field

class IngredientsRequest(BaseModel):
    ingredients: list = Field(description='List of ingredients', default=None)
