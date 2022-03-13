#!/usr/bin/python

# author kris muiru

# title: slinger_spotify music downloader


import os
import spotipy
import sys
import json
import pandas as pd
from pytube import YouTube
from spotipy.oauth2 import SpotifyClientCredentials
from youtubesearchpython import VideosSearch

cid = os.getenv('SPOTIFY_API_ID')
secret = os.getenv('SPOTIFY_API_KEY')

client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


playlist_url = input('Enter url of playlist or album: ')
album_playlist_bool = input('Album or playlist?(y-album n-playlist)')
song_folder = input('enter folder name: ')
MUSIC_DIR = '/home/kris/Music/'

if os.path.exists(MUSIC_DIR+song_folder):
    pass
else:
    os.mkdir(MUSIC_DIR+song_folder)

os.chdir(MUSIC_DIR+song_folder)


# handle albums


tracks = []


def get_album_tracks(album_id):
    album = sp.album_tracks(album_id)
    data_flame = pd.DataFrame(album)
    for i in range(len(data_flame)):
        items = data_flame.loc[i]['items']
        name = items['artists'][0]['name']
        song = items['name']
        track = name+' '+song
        tracks.append(track)
    return tracks

# handle playlists


def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids


if album_playlist_bool == 'y':
    tracks = get_album_tracks(playlist_url)
    for song in tracks:
        search_song = VideosSearch(song, limit=1)
        result = search_song.result()
        song = YouTube(str(result))
        print(f'downloading {song.title} ')
        stream = song.streams.filter(only_audio=True)
        print('--------------------------------------------------------')
        stream.first().download()
    sys.exit(1)


else:
    ids = getTrackIDs('', playlist_url)


def getAlbumId(album_id):
    ids = []
    album = sp.albums(album_id)


def getTrackFeatures(id):
    meta = sp.track(id)
    # meta
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']

    track = [name+' '+artist]
    return track

# loop over track ids


for i in range(len(ids)):
    track = getTrackFeatures(ids[i])
    tracks.append(track)


# youtube search and download

for details in tracks:
    for song in details:
        song = str(song)
        search_song = VideosSearch(song, limit=1)
        result = search_song.result()
        song = YouTube(str(result))
        print(f'downloading {song.title} ')
        stream = song.streams.filter(only_audio=True)
        print('--------------------------------------------------------')
        stream.first().download()
