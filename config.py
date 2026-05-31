import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Load variables from .env
load_dotenv()

# Get credentials
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

# Authentication manager
auth_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

# Create Spotify object
sp = spotipy.Spotify(auth_manager=auth_manager)