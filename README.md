# spotify_song_dowloader
A spotify music downloader that downloads playlists,albums or single music/video. A user provides the spotify music link to download the video(s) or audio(s).Follow the installation


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
If running linux,in your `.bashrc` or `.zshrc`,create two shell variables `SPOTIFY_API_KEY` and `SPOTIFY_API_ID`.

```bash
export SPOTIFY_API_KEY = 'c23........'
export SPOTIFY_API_ID ='vt5......'
```

You can also replace the two lines `cid and secret` with the spotify api key and id in `slinger_spotify.py`.
```python
# slinger_spotify.py
cid = 'ghq.....'
secret = 'cf5.....'
```
Run the `slinger_spotify` file,
```
python slinger_spotify.py
```
and follow the steps
## Technologies
- [pytube](https://pytube.io/en/latest/)
- [pandas](https://pandas.pydata.org/)

- [youtube-search-python](https://pypi.org/project/youtube-search-python/)
## Licence 
- [MIT](https://choosealicense.com/licenses/mit/)

