import pandas as pd
import numpy as np


def generate_recoms(idx):
    """
    fetches recommendations for given song (id)
    """
    idx = int(idx)
    # light.npy is pre-saved recommendations for all songs to optimize time
    sim = np.load("data/light.npy")
    df = pd.read_csv("data/song_meta.csv")
    recoms_list = sim[idx, :]
    recommendation = []
    # entered = df.iloc[int(idx), 1]
    # print("Recommendations for: ", entered)
    for i in range(0, 10):
        song_name = df.iloc[int(recoms_list[i]), 1]
        artist_name = df.iloc[int(recoms_list[i]), 2]
        spotify_id = df.iloc[int(recoms_list[i]), 3]
        preview = df.iloc[int(recoms_list[i]), 5]
        if preview == 'not_avail':
            preview = ""
        img = df.iloc[int(recoms_list[i]), 6]
        # print(song_name, " by ", artist_name)
        temp_dict = {
            "song_name": song_name,
            "artist_name": artist_name,
            "spotify_id": spotify_id,
            "image_url": img,
            "preview": preview
        }
        recommendation.append(temp_dict)
    return recommendation

