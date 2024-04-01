from p621.posts import Post

import requests
from requests import Response

USER_AGENT: str = 'p621/0.0.0'

def list_posts(api_key: str, username: str) -> list[Post]:
    response: Response = requests.get('https://e621.net/posts.json', params = {'api_key': api_key, 'login': username}, headers = {'User-Agent': USER_AGENT})
    posts: dict = response.json()['posts']

    return [Post(post) for post in posts]

def list_favorites(api_key: str, username: str) -> list[Post]:
    response: Response = requests.get('https://e621.net/favorites.json', params = {'api_key': api_key, 'login': username}, headers = {'User-Agent': USER_AGENT})
    posts: dict = response.json()['posts']

    return [Post(post) for post in posts]