import random

import pandas as pd


def send_results():
    """
    selects 10 songs at random to show at the search page
    """
    df = pd.read_csv("data/song_meta.csv")
    randomlist = []
    for i in range(10):
        n = random.randint(0, 50000)
        randomlist.append(n)
    
    random_songs = []

    for i in randomlist:
        song_id = df.iloc[i, 0]
        song_name = df.iloc[i, 1]
        artist_name = df.iloc[i, 2]
        spotify_id = df.iloc[i, 3]
        preview = df.iloc[i, 5]
        if preview == 'not_avail':
            preview = ""
        img = df.iloc[i, 6]
        # print(song_name, " by ", artist_name)
        temp_dict = {
            "id": str(song_id),
            "song_name": song_name,
            "artist_name": artist_name,
            "spotify_id": spotify_id,
            "image_url": img,
            "preview": preview
        }
        random_songs.append(temp_dict)
    return random_songs

