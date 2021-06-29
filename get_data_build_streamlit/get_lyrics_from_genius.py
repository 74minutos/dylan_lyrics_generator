import pandas as pd
from typing import List, Dict, Any
from get_data_build_streamlit import utilities

def get_lyrics(api_key_path: str, max_songs: int, seconds: int, retries: int) -> None:

    lyrics_data = []

    songs = utilities.genius_api_calls(api_key_path, 'Bob Dylan', max_songs, seconds, retries)
    lyrics_data  = [song.lyrics for song in songs]
    with open('lyrics/dylan.txt', 'w') as f:
        for item in lyrics_data:
            f.write("%s\n" % item)

if __name__ == '__main__':
    get_lyrics('credentials/genius_credentials', 100, 2, 3)
