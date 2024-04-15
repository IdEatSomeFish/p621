import requests
from requests import Response

from .data import USER_AGENT, ROOT_URL


class Login:
    def __init__(self, api_key: str, username: str) -> None:
        self.api_key: str = api_key
        self.username: str = username

    def vote(self, post_id: int, vote: int) -> None:
        url: str = '{root}/posts/{id}/votes.json'.format(root = ROOT_URL, id = post_id)
        parameters: dict = {
            'api_key': self.api_key,
            'login': self.username,
            'vote': vote,
            'no_unvote': True,
        }

        response: Response = requests.post(url, params = parameters, headers = {'User-Agent': USER_AGENT})
        match response.status_code:
            case 200:
                pass
            case status_code:
                raise Exception("failed with status code: " + str(status_code))
            
    def favorite(self, post_id: int) -> None:
        url: str = '{root}/favorites.json'.format(root = ROOT_URL)
        parameters: dict = {
            'api_key': self.api_key,
            'login': self.username,
            'post_id': post_id,
        }

        response: Response = requests.post(url, params = parameters, headers = {'User-Agent': USER_AGENT})
        match response.status_code:
            case 200:
                pass
            case status_code:
                raise Exception("failed with status code: " + str(status_code))