#!/usr/bin/python

# author kris muiru

# title: slinger_spotify music downloader

import os
import spotipy
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

print('--------------------------------------------------------')
print(f'Type of media --> {type_of_music}')
print('--------------------------------------------------------')


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
    print('--------------------------------------------------------')

# call function to create and change to specified directory dir


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


def downloadVideoOrAudio(song, choice):
    print(f'downloading {song.title}')
    if choice == 'audio':
        stream = song.streams.filter(only_audio=True).first(
        ).download()  # dowload first audio file
    elif choice == 'video':
        stream = song.streams.filter(
            progressive=True).first().download()


def downloadTracks(tracks):
    """
    download the music in tracks parameter

    Args:
        tracks (list): tracks to download from getTrack functions specified

    """
    choice = input('audio or video?: ')
    print('--------------------------------------------------------')
    for track in tracks:
        match_song = str(VideosSearch(track, limit=1).result()
                         )  # search for song and return match

        song = YouTube(str(match_song))

        downloadVideoOrAudio(song, choice)
        print('--------------------------------------------------------')


def downloadTracksBasedOnMediaType(type_of_music):
    """
    checks the type of song and invoke the downloadTracks based on song type

    Args:
        type_of_music (str): the type of song
    """
    if type_of_music == 'playlist':
        playlist_tracks = getPlaylistTracks(song_url)
        downloadTracks(playlist_tracks)
    elif type_of_music == 'album':
        album_tracks = getAlbumTracks(song_url)
        downloadTracks(album_tracks)


downloadTracksBasedOnMediaType(type_of_music)
