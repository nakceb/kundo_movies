from dotenv import load_dotenv
import os
from typing import Tuple


def load_omdb_api():
    """
    Loads and fetches api key and url
    :return:
    """
    # Load environment variables
    load_dotenv()
    # Get API key from environment variable
    api_key = os.getenv("OMDB_API_KEY")
    if api_key:
        url = "http://www.omdbapi.com/"
        return api_key, url
    else:
        return None, None

load_omdb_api()