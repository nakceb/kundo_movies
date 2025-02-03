from dotenv import load_dotenv
import os
import logging


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
        logging.warning("No OMDB_API_KEY set, will used cached data as offline demo.")
        return None, None