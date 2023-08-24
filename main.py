import spotipy
from bs4 import BeautifulSoup
import requests
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
from datetime import datetime


def get_date_from_user():
    """
    This function takes the date as the input from the user and validates it.
    :return: str
    """

    is_correct_format = False
    user_date = ''

    while not is_correct_format:
        user_date = input("Which year do you want to travel to? Type the date in this format YYYY-DD-MM: ")

        try:
            datetime.strptime(user_date, '%Y-%m-%d')
            is_correct_format = True

        except ValueError:
            print("Invalid input. Please pass the date in proper format.")

    return user_date


# Loads the Environment variables from the .env file.
load_dotenv()

# Storing the Environment variables in appropriate variables.
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_url = os.getenv("REDIRECT_URL")
spotify_username = os.getenv("SPOTIFY_USERNAME")

# Fetching the date from the User.
date = get_date_from_user()

# Updating the URL appending the proper date.
billboard_url = 'https://www.billboard.com/charts/hot-100/' + date

# Sending the request to the URL.
response = requests.get(url=billboard_url)
html_code = response.text

# Initializing the BeautifulSoup Object to parse the HTML code.
soup = BeautifulSoup(markup=html_code, features='html.parser')
h3_tags = soup.select(selector='.o-chart-results-list__item #title-of-a-story')\

year = date.split("-")[0]

# Providing proper authorization parameters and setting it up.
oauth = SpotifyOAuth(
    scope='playlist-modify-private',
    redirect_uri=redirect_url,
    client_id=client_id,
    client_secret=client_secret,
    show_dialog=True,
    cache_path='token.txt',
    username=spotify_username
)

# The Object 'sp' will handle all Spotify operations.
sp = spotipy.Spotify(auth_manager=oauth)

# Saving the user_id as we will need it later.
user_id = sp.current_user()['id']

playlist_description = f'Contains top Billboard top 100 songs of the year {year}.'

# Creating a new Playlist.
playlist_id = sp.user_playlist_create(
    user=user_id,
    name=f'{date} Billboard 100',
    public=False,
    description=playlist_description
)

song_uris = []

for h3_tag in h3_tags:

    # .strip() removes all trailing and leading whitespaces.
    song_name = h3_tag.text.strip()
    search_query = f'track:{song_name} year:{year}'
    result = sp.search(q=search_query, type='track')

    try:
        song_uri = result['tracks']['items'][0]['uri']
        song_uris.append(song_uri)

    except IndexError:
        print(f"{song_name} not found in Spotify. Skipping")

# Simply adding all the songs.
sp.playlist_add_items(
    playlist_id=playlist_id['id'],
    items=song_uris,
)
