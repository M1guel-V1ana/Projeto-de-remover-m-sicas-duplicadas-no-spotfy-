"Configuration for Mixify."
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = "http://127.0.0.1:8888/callback"
# Catalog search does not need playlist-write permissions.
SCOPES = ""
MARKET = "BR"
SEARCH_PAGE_SIZE = 50
SPOTIFY_SEARCH_MAX_OFFSET = 1000
