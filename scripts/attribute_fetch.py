import requests
import json
import pandas as pd
import time

CLIENT_ID = "50179b9e0a064ad09ffb159682151c22"
CLIENT_SECRET = "839cf55128424188bdae3d1083921ecf"

try:
    AUTH_URL = "https://accounts.spotify.com/api/token"

    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    auth_response_data = auth_response.json()
except Exception as e:
    print("error in auth")
    print(e)

# save the access token

try:
    access_token = auth_response_data['access_token']

    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    BASE_URL = 'https://api.spotify.com/v1/'
except Exception as e:
    print("error getting access token")
    print(e)

def get_urls(song_id):
    # Track ID from the URI
        
    # GET request to fetch details
    res = requests.get("https://api.spotify.com/v1/tracks/{id}".format(id = song_id), headers=headers).json()
    try:
        img_url = res["album"]["images"][0]["url"]
    except Exception as e:
        img_url = "error getting image"
        print(e)

    try:
        prev_url = res["preview_url"]
    except Exception as e:
        prev_url = "error getting preview"
        print(e)

    if prev_url == "None":
        prev_url = ""

    return img_url, prev_url

df = pd.read_csv("data/search.csv")
df["preview"] = ""
df["img"] = ""

for i in range(0, 50000):
    try:
        urls = get_urls(df.iloc[i, 3])
        df.iloc[i,5] = urls[0]
        df.iloc[i,6] = urls[1]

        if i%100 == 0:
            df.to_csv("data/song_meta.csv", index=False)
            print("Current song: ", str(df.iloc[i, 0]))
            print("saving")
            time.sleep(5)

    except Exception as e:
        print(e)
        print("error at ", str(df.iloc[i, 0]))
        df.to_csv("data/song_meta.csv", index=False)
        print(i)
        continue

df.to_csv("data/song_meta.csv", index=False)
