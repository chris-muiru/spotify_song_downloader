# spotify_song_dowloader

A spotify music downloader that downloads playlists,albums or single music/video using spotify music link

# Installation
Clone repo on your machine.
```bash
> git clone https://github.com/kris-slinger/spotify_song_dowloader
```
Install python requirements.
```bash
pip install -r requirements.txt
```
If using python3,use pip3.

Head over to [spotify for developer](https://developer.spotify.com/documentation/web-api/) and create an account.Create an app inside `spotify for developer` which will give you a secret id and key(check out their docs for more info).

If using linux,in your `.bashrc` or `.zshrc`,create two shell variables `SPOTIFY_API_KEY` and `SPOTIFY_API_ID`.

```bash
export SPOTIFY_API_KEY = 'c23........'
export SPOTIFY_API_ID ='vt5......'
```

If not using linux or not feeling like creationg shell variables,replace the two lines `cid and secret` with the spotify api key and id in `slinger_spotify.py`.

```python
# slinger_spotify.py
cid = 'ghq.....'
secret = 'cf5.....'
```
This api keys and id were created in  [spotify for developer](https://developer.spotify.com/documentation/web-api/) above.

Run the `slinger_spotify` file,
```
python slinger_spotify.py
```
and follow the steps
## Technologies
- [pytube](https://pytube.io/en/latest/)
- [pandas](https://pandas.pydata.org/)

- [youtube-search-python](https://pypi.org/project/youtube-search-python/)
- [spotipy](https://spotipy.readthedocs.io/en/master/)
## License 
- [MIT](https://choosealicense.com/licenses/mit/)

