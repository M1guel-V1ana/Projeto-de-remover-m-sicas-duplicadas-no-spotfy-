"""Spotify OAuth client."""
import spotipy
from spotipy.oauth2 import SpotifyOAuth

import config



def create_spotify_client():
    if not config.CLIENT_ID or not config.CLIENT_SECRET:
        raise RuntimeError(
            "Spotify credentials missing. Add SPOTIFY_CLIENT_ID and "
            "SPOTIFY_CLIENT_SECRET to your .env file."
        )

    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=config.CLIENT_ID,
            client_secret=config.CLIENT_SECRET,
            redirect_uri=config.REDIRECT_URI,
            scope=config.SCOPES,
        )
    )
