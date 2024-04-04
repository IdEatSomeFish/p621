from p621.posts import Post

import requests
from requests import Response

USER_AGENT: str = 'p621/0.1.1'

def search_posts(api_key: str, username: str, limit: int = None, tags: list[str] = None, page: int = None) -> list[Post]:
    parameters: dict = {'api_key': api_key, 'login': username}
    if limit:
        parameters['limit'] = limit
    if tags:
        parameters['tags'] = ' '.join(tags)
    if page:
        parameters['page'] = page

    response: Response = requests.get('https://e621.net/posts.json', params = parameters, headers = {'User-Agent': USER_AGENT})
    
    match response.status_code:
        case 200:
            posts: dict = response.json()['posts']
            return [Post(post) for post in posts]
        case 401:
            raise Exception("failed with invalid authorization")
        case status_code:
            raise Exception("failed with status code: " + status_code)

def list_favorites(api_key: str, username: str, user_id: int = None) -> list[Post]:
    parameters: dict = {'api_key': api_key, 'login': username}
    if user_id:
        parameters['user_id'] = user_id

    response: Response = requests.get('https://e621.net/favorites.json', params = parameters, headers = {'User-Agent': USER_AGENT})

    match response.status_code:
        case 200:
            posts: dict = response.json()['posts']
            return [Post(post) for post in posts]
        case 401:
            raise Exception("failed with invalid authorization")
        case status_code:
            raise Exception("failed with status code: " + status_code)
        
def get_post(api_key: str, username: str, post_id: int) -> Post:
    parameters: dict = {'api_key': api_key, 'login': username}
    url: str = 'https://e621.net/posts/{}.json'.format(post_id)

    response: Response = requests.get(url, params = parameters, headers = {'User-Agent': USER_AGENT})

    match response.status_code:
        case 200:
            post: dict = response.json()['post']
            return Post(post)
        case 401:
            raise Exception("failed with invalid authorization")
        case status_code:
            raise Exception("failed with status code: " + status_code)
        

class Login:
    def __init__(self, api_key: str, username: str) -> None:
        self.api_key: str = api_key
        self.username: str = username

    def search_posts(self, limit: int = None, tags: list[str] = None, page: int = None) -> list[Post]:
        search_posts(self.api_key, self.username, limit = limit, tags = tags, page = page)

    def list_favorites(self, user_id: int = None) -> list[Post]:
        list_favorites(self.api_key, self.username, user_id = user_id)

    def get_post(self, post_id) -> Post:
        get_post(self.api_key, self.username, post_id = post_id)