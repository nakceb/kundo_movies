import requests
import logging
import json

from fastapi import APIRouter, HTTPException
from fastapi.templating import Jinja2Templates
from kundo_movies.utils import load_omdb_api
from fastapi.responses import HTMLResponse, JSONResponse


router = APIRouter(prefix="/details")

# Fetch api_key
OMDB_API_KEY, OMDB_API_URL = load_omdb_api()

# Load in templates
templates = Jinja2Templates(directory="templates")


@router.get("/{title}", response_class=HTMLResponse)
async def details(title: str):

    if OMDB_API_KEY is None:
        # TODO
        logging.critical("Offline logging not implemented")
        # movie_data = json.loads("../data/details.json")
        exit()

    # Make request to OMDb API
    params = {
        "apikey": OMDB_API_KEY,
        "t": title,
    }

    response = requests.get(OMDB_API_URL, params=params)
    movie_data = response.json()

    logging.debug(f"Movie data in details: {movie_data}")

    # Check if movie was found
    if movie_data.get("Response") == "True":
        return JSONResponse(content=movie_data)
    else:
        raise HTTPException(status_code=404, detail="Movie not found")

