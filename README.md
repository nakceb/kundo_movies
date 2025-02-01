# kundo-movies
Kundo work case for potential job candidates. Let's implement a mini webapp!

## Install:
``` python
# Create venv / conda env
pip install .

# Create a .env file and add optional OMBD-API-Key, we are loading it in as a environment variable
touch .env

# nano .env
OMDB_API_KEY=<enter your key>
```

## Run application
``` bash 
cd public 
uvicorn main:app --reload

# Open browser at localhost:8000
```

## The Task

Together we will build a tiny competitor to IMDB, by using an existing
movie database API.

Create a webpage using [Django](https://www.djangoproject.com/) or [FastAPI](https://fastapi.tiangolo.com/). If you want to build a frontend in React or plain JavaScript, that's also fine. 
We like working with pytest, we appreciate if you add some tests. 
Use the tools that showcases the skills needed for the role you are applying for. Try to show how
you want to write code in a professional setting, what is important to you?


The page should have a search function where you can search for movie
titles. Search results should have their poster, title, and year
displayed. Feel free to add other functionality you think would be fitting.

The movies should also have a small details page,
where you can see the director and plot of the movie.

## The API
We will use [OMDb API](http://www.omdbapi.com/) to have a simple API to work with.

To get started quickly and avoid potential network issues we have saved
the result of two API calls already:

### Search
You can search for movie titles from the API with the `s` query parameter:

    curl -XGET 'http://www.omdbapi.com/?apikey=[API-key]&s=[URL encoded search-string]'

The pre-saved data is in data/search.json.

### Details
You can get the details of a specific movie from the API with the `i` query parameter:

    curl -XGET 'http://www.omdbapi.com/?apikey=[API-key]&i=[imdbID]'

The pre-saved data is in data/details.json.
