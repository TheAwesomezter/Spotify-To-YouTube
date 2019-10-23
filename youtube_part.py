from apiclient.discovery import build
import csv

api_key = '' # enter your YouTube API key
youtube = build('youtube', 'v3', developerKey=api_key)

songs = []

with open("modified_list.csv") as file:
    fileLine = csv.reader(file)
    for value in fileLine:
        songs.append(value)

songs = [" ".join(song) for song in songs]

song_ids = []

for i in songs:
    req = youtube.search().list(q=i, part="snippet", type="video")
    res = req.execute()

    song_ids.append(res['items'][0]['id']['videoId'])

for song_id in song_ids:
    print(song_id)
