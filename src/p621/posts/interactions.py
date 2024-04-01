from .posts import Post

def download_post(post: Post, path: str = None) -> None:
    import urllib.request

    target: str = path + '/' + str(post.id) + '.' + post.file.extension
    url: str = post.file.url
    urllib.request.urlretrieve(url, target)

def open_post(post: Post) -> None:
    import webbrowser
    
    url: str = 'https://e621.net/posts/' + str(post.id)
    webbrowser.open(url)