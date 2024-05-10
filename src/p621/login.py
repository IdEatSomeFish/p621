import requests

from .data import USER_AGENT, ROOT_URL


class Login:
    def __init__(self, api_key: str, username: str) -> None:
        self.api_key: str = api_key
        self.username: str = username
        
    def __repr__(self) -> str:
        return f'<Login [{self.username}]>'
    
    def _encode(self) -> str:
        import base64
        return base64.b64encode(f'{self.username}:{self.api_key}'.encode()).decode()

    def vote(self, post_id: int, vote: int) -> None:
        url: str = f'{ROOT_URL}/posts/{post_id}/votes.json'
        parameters: dict = {
            'vote': vote,
            'no_unvote': True,
        }

        headers: dict = {
            'User-Agent': USER_AGENT,
            'Authorization': f'Basic {self._encode()}'
        }

        response: requests.Response = requests.post(url, params = parameters, headers = headers)
        match response.status_code:
            case 200:
                pass
            case status_code:
                raise Exception("failed with status code: " + str(status_code))
            
    def favorite(self, post_id: int) -> None:
        url: str = f'{ROOT_URL}/favorites.json'
        parameters: dict = {
            'post_id': post_id,
        }

        headers: dict = {
            'User-Agent': USER_AGENT,
            'Authorization': f'Basic {self._encode()}'
        }

        response: requests.Response = requests.post(url, params = parameters, headers = headers)
        match response.status_code:
            case 200:
                pass
            case status_code:
                raise Exception("failed with status code: " + str(status_code))