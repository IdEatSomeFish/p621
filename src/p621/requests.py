from .posts import Post
from .pools import Pool

import requests
from requests import Response

USER_AGENT: str = 'p621/0.2.0'

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
            raise Exception("failed with status code: " + str(status_code))
        
def search_pools(limit: int = None, page: int = None) -> list[Pool]:
    parameters: dict = {}
    if limit:
        parameters['limit'] = limit
    if page:
        parameters['page'] = page

    response: Response = requests.get('https://e621.net/pools.json', params = parameters, headers = {'User-Agent': USER_AGENT})
    
    match response.status_code:
        case 200:
            pools: dict = response.json()
            return [Post(pool) for pool in pools]
        case status_code:
            raise Exception("failed with status code: " + str(status_code))

def list_favorites(user_id: int, limit: int = None, page: int = None) -> list[Post]:
    parameters: dict = {'user_id': user_id}
    if limit:
        parameters['limit'] = limit
    if page:
        parameters['page'] = page

    response: Response = requests.get('https://e621.net/favorites.json', params = parameters, headers = {'User-Agent': USER_AGENT})

    match response.status_code:
        case 200:
            posts: dict = response.json()['posts']
            return [Post(post) for post in posts]
        case status_code:
            raise Exception("failed with status code: " + str(status_code))
        
def get_post(post_id: int) -> Post:
    url: str = 'https://e621.net/posts/{}.json'.format(post_id)

    response: Response = requests.get(url, headers = {'User-Agent': USER_AGENT})

    match response.status_code:
        case 200:
            post: dict = response.json()['post']
            return Post(post)
        case status_code:
            raise Exception("failed with status code: " + str(status_code))
        
def get_pool(pool_id: int) -> Post:
    url: str = 'https://e621.net/pools/{}.json'.format(pool_id)

    response: Response = requests.get(url, headers = {'User-Agent': USER_AGENT})

    match response.status_code:
        case 200:
            pool: dict = response.json()
            return Pool(pool)
        case status_code:
            raise Exception("failed with status code: " + str(status_code))
        
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
            raise Exception("failed with status code: " + str(status_code))