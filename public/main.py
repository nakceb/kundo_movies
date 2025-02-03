#!/usr/bin/env python3
import requests
import json
import logging

from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse

from kundo_movies.utils import load_omdb_api

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load in templates
templates = Jinja2Templates(directory="templates")

# Fetch api_key
OMDB_API_KEY, OMDB_API_URL = load_omdb_api()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "movies": None}
    )

@app.post("/search", response_class=HTMLResponse)
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


@app.get("/details/{title}", response_class=HTMLResponse)
async def details(title: str):

    if OMDB_API_KEY is None:
        # TODO
        logging.critical("Offline logging not implemented")
        movie_data = json.loads("../data/details.json")
        print(movie_data)
        exit()
    # Make request to OMDb API
    params = {
        "apikey": OMDB_API_KEY,
        "t": title,
    }

    response = requests.get(OMDB_API_URL, params=params)
    movie_data = response.json()

    print(movie_data)
    # Check if movie was found
    if movie_data.get("Response") == "True":
        return JSONResponse(content=movie_data)
    else:
        raise HTTPException(status_code=404, detail="Movie not found")

