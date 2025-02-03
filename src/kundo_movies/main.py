#!/usr/bin/env python3

import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from kundo_movies.routers import details, search


# Load in templates
templates = Jinja2Templates(directory="templates")

def create_app():
    """
    Insansiate app, add routes etc
    :return: fastapi application
    """
    app = FastAPI()

    # Mount static files
    app.mount("/static", StaticFiles(directory="static"), name="static")

    # Add home route
    @app.get("/", response_class=HTMLResponse)
    async def home(request: Request):
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "movies": None}
        )

    app.include_router(search.router)
    app.include_router(details.router)
    return app


app = create_app()
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)