import re


def resolve_type_of_song(url):
    """
    function to figure out the type of song

    Args:
        url (string): url from spotify 
    """
    regex = re.compile(r'playlist|album|show')

    mo = regex.search(url)

    return mo.group()


print(resolve_type_of_song(
    'https://open.spotify.com/show/1VXcH8QHkjRcTCEd88U3ti?si=abdea63c60d84a0b'))
