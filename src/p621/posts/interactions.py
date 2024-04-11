from .classes import Post

def download_post(post: Post, path: str = None) -> None:
    import requests
    from requests import Response
    import os

    target: str = str(post.id) + '.' + post.file.extension
    if path:
        target = path + '/' + target

        if not os.path.exists(path):
            os.mkdir(path)

    url: str = post.file.url

    if url:
        response: Response = requests.get(url)

        with open(target, 'wb') as file:
            file.write(response.content)

def open_post(post: Post) -> None:
    import webbrowser
    
    url: str = post.page_url()
    webbrowser.open(url)