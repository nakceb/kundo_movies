import requests

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from kundo_movies.utils import load_omdb_api


router = APIRouter(prefix="/search")

# Fetch api_key
OMDB_API_KEY, OMDB_API_URL = load_omdb_api()

# Load in templates
templates = Jinja2Templates(directory="templates")



@router.post("", response_class=HTMLResponse)
async def search(request: Request, title: str = Form(...)):
    # Make request to OMDb API
    params = {
        "apikey": OMDB_API_KEY,
        "s": title
    }

    # Send request to OMDB
    response = requests.get(OMDB_API_URL, params=params)
    movie_search_data = response.json()

    # Check if movie was found
    if movie_search_data.get("Response") == "True":
        movies_data = []
        for movie in movie_search_data.get("Search"):
            movies_data.append({"title": movie.get("Title"),
                                "year": movie.get("Year"),
                                "poster": movie.get("Poster")})
    else:
        movies_data = None

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "movies": movies_data}
    )