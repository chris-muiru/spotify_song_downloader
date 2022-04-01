# spotify_song_dowloader
This is a script created to download spotify music. It consumes data from spotipy api,searches for the media in youtube using the pytube module and dowload the
music or a 720p videos if the music exists. 


# instructions
- clone this repo in ur machine
- run `pip3 install -r requiremnts.txt` to install the requirements.
- head to https://developer.spotify.com/documentation/web-api/ and create an account.
- create an app inside spotify for developer which will give you a secret id and key.

- if running linux,in your `.bashrc` or `.zshrc`,create the two shell variables 'SPOTIFY_API_KEY' and `SPOTIFY_API_ID`.
- you can also replace the two lines `cid and secret` with the key and id in `slinger_spotify.py` if on another os.

- run the `slinger_spotify` file.

