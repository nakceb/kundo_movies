from kundo_movies.utils import load_omdb_api
from kundo_movies.main import create_app

def test_load_omdb_api():
    key, url = load_omdb_api()
    assert key is not None
    assert url is not None

def test_create_app():
    # Dummy import, make sure we can instansiate app at least
    app = create_app()
    assert app is not None