import spotipy
import os
import spotipy.util as util
import csv

user_id = "zspiqhjzpsdh6r8vy5wiftudu" # enter your user id
client_id = "17019f0ff50848ecbfa9845242da1484" # enter your client ID
client_secret = "fbc525891a8842b8b967aeb7098c6eac" # enter your client secret
redirect_url = "http://localhost:8888/"

playlist_id = "5IyU7Wdwb0m7XGlcjDGH5d" # enter the playlist id

try:
    token = util.prompt_for_user_token(user_id, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_url)
except:
    os.remove(f".cache-{user_id}")
    token = util.prompt_for_user_token(user_id, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_url)

spotify = spotipy.Spotify(auth=token)

songs = []
user = spotify.current_user()
it = 3 # enter the integer(rounded to the next number) to the number of songs in the playlist, divided by 100; i.e, if the playlist has 272 songs, then the iterant would be 3
for i in range(it):
    results = spotify.user_playlist_tracks(user_id, playlist_id, fields='items', market='fr', limit=100, offset= i*100)
    for value in results.values():
        for val in value:
            for key, v in val.items():
                try:
                    artist_n = v['album']['artists'][0]['name']
                    song_n = v['name']
                    print(artist_n, song_n)
                    col = [artist_n, song_n]
                    songs.append(col)
                except:
                    continue

for i in range(len(songs)):
    print(songs[i])
print(len(songs))

with open('songs_list.csv', 'w+') as file: # enter the file name
    writer = csv.writer(file)
    writer.writerows(songs)

with open('songs_list.csv') as input, open('modified_list.csv', 'w', newline='') as output:
    writer = csv.writer(output)
     for row in csv.reader(input):
         if any(field.strip() for field in row):
             writer.writerow(row)
