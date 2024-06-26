import requests

from .posts import Post
from .pools import Pool

from .data import USER_AGENT, ROOT_URL

from .login import Login


def search_posts(tags: list[str] | str | None = None, limit: int | None = None, page: int | str | None = None, login: Login | None = None) -> list[Post]:
    url: str = f'{ROOT_URL}/posts.json'
    parameters: dict = {}
    if tags:
        parameters['tags'] = tags if type(tags) == str else ' '.join(tags)
    if limit:
        parameters['limit'] = limit
    if page:
        parameters['page'] = page

    headers: dict = {'User-Agent': USER_AGENT}
    if login:
        headers["Authorization"] = f"Basic {login._encode()}"

    response: requests.Response = requests.get(url, params = parameters, headers = headers)
    match response.status_code:
        case 200:
            pass
        case status_code:
            raise Exception("failed with status code: " + str(status_code))
    
    posts: dict = response.json()['posts']
    return [Post(post) for post in posts]


def list_pools(limit: int | None = None, page: int | str | None = None, login: Login | None = None) -> list[Pool]:
    url: str = f'{ROOT_URL}/pools.json'
    parameters: dict = {}
    if limit:
        parameters['limit'] = limit
    if page:
        parameters['page'] = page

    headers: dict = {'User-Agent': USER_AGENT}
    if login:
        headers['Authorization'] = f'Basic {login._encode()}'

    response: requests.Response = requests.get(url, params = parameters, headers = headers)
    match response.status_code:
        case 200:
            pass
        case status_code:
            raise Exception("failed with status code: " + str(status_code))
    
    pools: dict = response.json()
    return [Pool(pool) for pool in pools]


def list_favorites(user_id: int, limit: int | None = None, page: int | str | None = None, login: Login | None = None) -> list[Post]:
    url: str = f'{ROOT_URL}/favorites.json'
    parameters: dict = {'user_id': user_id}
    if limit:
        parameters['limit'] = limit
    if page:
        parameters['page'] = page

    headers: dict = {'User-Agent': USER_AGENT}
    if login:
        headers['Authorization'] = f'Basic {login._encode()}'

    response: requests.Response = requests.get(url, params = parameters, headers = headers)
    match response.status_code:
        case 200:
            pass
        case status_code:
            raise Exception("failed with status code: " + str(status_code))
    
    posts: dict = response.json()['posts']
    return [Post(post) for post in posts]


def list_popular(date: str | None = None, scale: str | None = None, login: Login | None = None) -> list[Post]:
    url: str = f'{ROOT_URL}/popular.json'
    parameters: dict = {}
    if date:
        parameters['date'] = date
    if scale:
        parameters['scale'] = scale

    headers: dict = {'User-Agent': USER_AGENT}
    if login:
        headers['Authorization'] = f'Basic {login._encode()}'

    response: requests.Response = requests.get(url, params = parameters, headers = headers)
    match response.status_code:
        case 200:
            pass
        case status_code:
            raise Exception("failed with status code: " + str(status_code))
        
    posts: dict = response.json()['posts']
    return [Post(post) for post in posts]


def get_post(post_id: int) -> Post:
    url: str = f'{ROOT_URL}/posts/{post_id}.json'

    response: requests.Response = requests.get(url, headers = {'User-Agent': USER_AGENT})
    match response.status_code:
        case 200:
            pass
        case status_code:
            raise Exception("failed with status code: " + str(status_code))
    
    post: dict = response.json()['post']
    return Post(post)


def get_pool(pool_id: int) -> Pool:
    url: str = f'{ROOT_URL}/pools/{pool_id}.json'
    
    response: requests.Response = requests.get(url, headers = {'User-Agent': USER_AGENT})
    match response.status_code:
        case 200:
            pass
        case status_code:
            raise Exception("failed with status code: " + str(status_code))
    
    pool: dict = response.json()
    return Pool(pool)