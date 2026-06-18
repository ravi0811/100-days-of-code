from bs4 import BeautifulSoup
import requests
from ytmusicapi import YTMusic
import os

date=input("which year do you want to travel to?Type the date in this format YYYY-MM-DD:\n")
hd= os.getenv("ID")
header={
    hd
}

targetUrl= "https://appbrewery.github.io/bakeboard-hot-100/2026-04-18/"

response= requests.get(targetUrl)

bakeWebpage= response.text

soup= BeautifulSoup(bakeWebpage,"html.parser")

songNames= soup.find_all(name="h3",class_="chart-entry__title")
songList=[item.getText() for item in songNames]

yt=YTMusic("browser.json")
playlist= yt.get_library_playlists(limit=100)
print(f"found {len(playlist)} playlist in your library.")

playlistName=f"{date} Billboard 100"
playlist_id= None

for p in playlist:
    if p["title"]==playlistName:
        playlist_id= p["playlistId"]
        break

if playlist_id:
    print("This playlist already exists")
else:
    playlist_id=yt.create_playlist(
        playlistName,
        f"Playlist with the hottest songs from {date}",
        privacy_status="PRIVATE"
    )

    print("Playlist Created")

for song in songList:
    try:
        searchResults = yt.search(song, filter="songs", limit=1)
        
        if searchResults:
            song_id = searchResults[0]['videoId']
            
            yt.add_playlist_items(playlistId=playlist_id, videoIds=[song_id])
            print(f"Added: {song}")
        else:
            print(f"Skipped: {song} | Reason: Not found on YouTube Music")
            
    except Exception as e:
        print(f"Skipped: {song} | Reason: {e}")