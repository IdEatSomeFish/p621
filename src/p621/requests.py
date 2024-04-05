from p621.posts import Post

import requests
from requests import Response

USER_AGENT: str = 'p621/0.1.0'

def search_posts(limit: int = None, tags: list[str] = None, page: int = None) -> list[Post]:
    parameters: dict = {}
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
        case status_code:
            raise Exception("failed with status code: " + status_code)

def list_favorites(user_id: int) -> list[Post]:
    parameters: dict = {'user_id': user_id}

    response: Response = requests.get('https://e621.net/favorites.json', params = parameters, headers = {'User-Agent': USER_AGENT})

    match response.status_code:
        case 200:
            posts: dict = response.json()['posts']
            return [Post(post) for post in posts]
        case status_code:
            raise Exception("failed with status code: " + status_code)
        
def get_post(post_id: int) -> Post:
    url: str = 'https://e621.net/posts/{}.json'.format(post_id)

    response: Response = requests.get(url, headers = {'User-Agent': USER_AGENT})

    match response.status_code:
        case 200:
            post: dict = response.json()['post']
            return Post(post)
        case status_code:
            raise Exception("failed with status code: " + status_code)
        
def list_popular(date: str = None, scale: str = None) -> list[Post]:
    parameters: dict = {}
    if date:
        parameters['date'] = date
    if scale:
        parameters['scale'] = scale

    response: Response = requests.get('https://e621.net/popular.json', params = parameters, headers = {'User-Agent': USER_AGENT})

    match response.status_code:
        case 200:
            posts: dict = response.json()['posts']
            return [Post(post) for post in posts]
        case status_code:
            raise Exception("failed with status code: " + status_code)