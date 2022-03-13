from youtubesearchpython import VideosSearch, PlaylistsSearch, ChannelsSearch


def single_video_search_feature(searchable):
    videosearch = VideosSearch(searchable, limit=1)
    result = videosearch.result()['result']
    vid_details = result[0].get('accessibility')
    link = result[0].get('link')
    print(vid_details['title']+'\n')
    return link


def playlist_search_feature(searchable):
    playlist_search = PlaylistsSearch(searchable, limit=1)
    result = playlist_search.result()['result']
    link = result[0].get('link')
    return link


def channel_search_feature(searchable):
    channels_search = ChannelsSearch(searchable, limit=1)
    result = channels_search.result()['result']
    link = result[0].get('link')
    return link
