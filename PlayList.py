import os
from kivy.storage.jsonstore import JsonStore
import yt_dlp

CACHE_DIR = "/path/to/cache"  # Update with your actual cache directory

# Create cache directory if it doesn't exist
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

# Cache song download
def cache_song(song_url, song_title):
    cached_file = os.path.join(CACHE_DIR, f"{song_title}.mp3")
    if not os.path.exists(cached_file):
        # Download the song to cache
        ydl_opts = {
            'quiet': True,
            'outtmpl': cached_file,
            'format': 'bestaudio/best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([song_url])
    return cached_file

# Playlist handling
playlist = []  # A list to store the songs
current_playlist_index = 0  # Keep track of the current song index

# Add song to playlist
def add_to_playlist(song_title, song_url):
    cached_song = cache_song(song_url, song_title)
    playlist.append({'title': song_title, 'url': cached_song})

# Play the next song in the playlist
def play_next_song_in_playlist():
    global current_playlist_index
    if current_playlist_index + 1 < len(playlist):
        current_playlist_index += 1
        song_info = playlist[current_playlist_index]
        song_url = song_info['url']
        play_song(song_url)  # Play the next song

# Play the previous song in the playlist
def play_previous_song_in_playlist():
    global current_playlist_index
    if current_playlist_index - 1 >= 0:
        current_playlist_index -= 1
        song_info = playlist[current_playlist_index]
        song_url = song_info['url']
        play_song(song_url)  # Play the previous song
  
