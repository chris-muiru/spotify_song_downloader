# spotify_song_dowloader
This is a script created to download spotify music. It consumes data from spotipy api,searches for the media in youtube using the pytube module and dowload the
music or 720p videos if the music exists. 


# instructions
- clone this repo in ur machine
- run `pip3 install -r requiremnts.txt` to install the requirements.
- head to spotify for developer(https://developer.spotify.com/documentation/web-api/) and create an account.
- create an app inside `spotify for developer` which will give you a secret id and key.
- if running linux,in your `.bashrc` or `.zshrc`,create the two shell variables 'SPOTIFY_API_KEY' and `SPOTIFY_API_ID`.
```
e.g
export SPOTIFY_API_KEY = 'c23........'
export SPOTIFY_API_ID ='vt5......'
```
- you can also replace the two lines `cid and secret` with the key and id in `slinger_spotify.py`.
- run the `slinger_spotify` file,
```
python slinger_spotify.py
```
and follow the steps

