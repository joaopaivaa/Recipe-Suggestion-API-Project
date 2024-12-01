import uvicorn
from fastapi import FastAPI
import find_recipe

app = FastAPI(title='Recipe Suggestion API', version='1.0.0')

app.include_router(find_recipe.router, tags=['Recipe Finder'])

if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8000)