from .posts import Post
from .pools import Pool

import requests

from .data import USER_AGENT, ROOT_URL


def search_posts(tags: list[str] = None, limit: int = None, page: int = None) -> list[Post]:
    url: str = '{root}/posts.json'.format(root = ROOT_URL)
    parameters: dict = {}
    if tags:
        parameters['tags'] = ' '.join(tags)
    if limit:
        parameters['limit'] = limit
    if page:
        parameters['page'] = page

    response: requests.Response = requests.get(url, params = parameters, headers = {'User-Agent': USER_AGENT})
    match response.status_code:
        case 200:
            pass
        case status_code:
            raise Exception("failed with status code: " + str(status_code))
    
    posts: dict = response.json()['posts']
    return [Post(post) for post in posts]


def list_pools(limit: int = None, page: int = None) -> list[Pool]:
    url: str = '{root}/pools.json'.format(root = ROOT_URL)
    parameters: dict = {}
    if limit:
        parameters['limit'] = limit
    if page:
        parameters['page'] = page

    response: requests.Response = requests.get(url, params = parameters, headers = {'User-Agent': USER_AGENT})
    match response.status_code:
        case 200:
            pass
        case status_code:
            raise Exception("failed with status code: " + str(status_code))
    
    pools: dict = response.json()
    return [Post(pool) for pool in pools]


def list_favorites(user_id: int, limit: int = None, page: int = None) -> list[Post]:
    url: str = '{root}/favorites.json'.format(root = ROOT_URL)
    parameters: dict = {'user_id': user_id}
    if limit:
        parameters['limit'] = limit
    if page:
        parameters['page'] = page

    response: requests.Response = requests.get(url, params = parameters, headers = {'User-Agent': USER_AGENT})
    match response.status_code:
        case 200:
            pass
        case status_code:
            raise Exception("failed with status code: " + str(status_code))
    
    posts: dict = response.json()['posts']
    return [Post(post) for post in posts]


def list_popular(date: str = None, scale: str = None) -> list[Post]:
    url: str = '{root}/popular.json'.format(root = ROOT_URL)
    parameters: dict = {}
    if date:
        parameters['date'] = date
    if scale:
        parameters['scale'] = scale

    response: requests.Response = requests.get(url, params = parameters, headers = {'User-Agent': USER_AGENT})
    match response.status_code:
        case 200:
            pass
        case status_code:
            raise Exception("failed with status code: " + str(status_code))
        
    posts: dict = response.json()['posts']
    return [Post(post) for post in posts]


def get_post(post_id: int) -> Post:
    url: str = '{root}/posts/{id}.json'.format(root = ROOT_URL, id = post_id)

    response: requests.Response = requests.get(url, headers = {'User-Agent': USER_AGENT})
    match response.status_code:
        case 200:
            pass
        case status_code:
            raise Exception("failed with status code: " + str(status_code))
    
    post: dict = response.json()['post']
    return Post(post)


def get_pool(pool_id: int) -> Post:
    url: str = '{root}/pools/{id}.json'.format(root = ROOT_URL, id = pool_id)
    
    response: requests.Response = requests.get(url, headers = {'User-Agent': USER_AGENT})
    match response.status_code:
        case 200:
            pass
        case status_code:
            raise Exception("failed with status code: " + str(status_code))
    
    pool: dict = response.json()
    return Pool(pool)