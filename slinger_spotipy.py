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

from type_of_song import resolve_type_of_song

cid = os.getenv('SPOTIFY_API_ID')
secret = os.getenv('SPOTIFY_API_KEY')

client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


song_url = input('Enter url of playlist or album: ')

type_of_music = resolve_type_of_song(song_url)

print(f'Type of media --> {type_of_music}')


def mkdir_and_chdir_to_download(type_of_music):
    """
    create a directory to download music  based on the type of music.
    After creating the directory,change to that directory

    Args:
        type_of_music (string): type of music media e.g show,playlist....
    """
    MUSIC_DIR = '/home/kris/Music/'

    song_folder = input('enter folder name: ')

    download_to_folder = f'{MUSIC_DIR}/{type_of_music}s/{song_folder}'

    x = os.makedirs(download_to_folder) if not os.path.exists(
        download_to_folder) else None

    os.chdir(download_to_folder)

# call function to create and change to this dir


mkdir_and_chdir_to_download(type_of_music)


def getPlaylistTracks(link):
    """ get a list of playlist tracks and the artist that created them 

    Args:
        link (string): spotify playlist link
    Returns:
            list : a list of playlist songs and artists 
    """
    tracks = []
    playlist = sp.playlist_items(link)
    df = pd.DataFrame(playlist)
    for i in df.index:
        items = df.loc[i, 'items']
        artist = items['track']['album']['artists'][0]['name']
        song = items['track']['album']['name']
        tracks.append(f'{artist} {song}')
    return tracks

def getAlbumTracks(link):
    """
    get a list of album tracks and the artist that created them 
    Args:
        link (string): spotify album link
    Returns:
            list : a list of album songs and artists 
    """
    tracks = []
    album = sp.album_tracks(link)
    data_flame = pd.DataFrame(album)
    for i in range(len(data_flame)):
        items = data_flame.loc[i]['items']
        artist = items['artists'][0]['name']
        song = items['name']
        tracks.append(f'{artist} {song}')
    return tracks

def downloadTracks(tracks):
    for track in tracks:
        match_song = str(VideosSearch(track, limit=1).result()) # search for song and return match
        song = YouTube(str(match_song))
        print(f'downloading {song.title}')
        stream = song.streams.filter(only_audio=True)
        stream.first().download() # dowload audio
        print('--------------------------------------------------------')


if type_of_music == 'playlist':
    playlist_tracks = getPlaylistTracks(song_url)
    downloadTracks(playlist_tracks)
elif type_of_music == 'album':
    album_tracks = getAlbumTracks(song_url)
    downloadTracks()

# # # handle playlists
# # def get_playlist_ids(user, playlist_id):
# #     ids = []
# #     playlist = sp.user_playlist(user, playlist_id)
# #     for item in playlist['tracks']['items']:
# #         track = item['track']
# #         ids.append(track['id'])
# #     return ids


# if album_playlist_bool == 'y':
#     tracks = get_album_tracks(song_url)
#     for song in tracks:
#         search_song = VideosSearch(song, limit=1)
#         result = search_song.result()
#         song = YouTube(str(result))
#         print(f'downloading {song.title} ')
#         stream = song.streams.filter(only_audio=True)
#         print('--------------------------------------------------------')
#         stream.first().download()
#     sys.exit(1)


# else:
#     ids = getTrackIDs('', playlist_url)


# def getAlbumId(album_id):
#     ids = []
#     album = sp.albums(album_id)


# def getTrackFeatures(id):
#     meta = sp.track(id)
#     # meta
#     name = meta['name']
#     album = meta['album']['name']
#     artist = meta['album']['artists'][0]['name']

#     track = [name+' '+artist]
#     return track

# # loop over track ids


# for i in range(len(ids)):
#     track = getTrackFeatures(ids[i])
#     tracks.append(track)


# # youtube search and download

# for details in tracks:
#     for song in details:
#         song = str(song)
#         search_song = VideosSearch(song, limit=1)
#         result = search_song.result()
#         song = YouTube(str(result))
#         print(f'downloading {song.title} ')
#         stream = song.streams.filter(only_audio=True)
#         print('--------------------------------------------------------')
#         stream.first().download()
