from .posts import Post

import urllib.request
import webbrowser
from PIL import Image

def download_image(post: Post, path: str = None) -> None:
    target: str = path + '/' + str(post.id) + '.' + post.file.extension
    url: str = post.file.url
    urllib.request.urlretrieve(url, target)

def open_post(post: Post) -> None:
    url: str = 'https://e621.net/posts/' + str(post.id)
    webbrowser.open(url)