from .classes import Post

def download_post(post: Post, path: str = None) -> None:
    import urllib.request

    target: str = str(post.id) + '.' + post.file.extension
    if path:
        target = path + '/' + target

    url: str = post.file.url
    urllib.request.urlretrieve(url, target)

def open_post(post: Post) -> None:
    import webbrowser
    
    url: str = post.page_url()
    webbrowser.open(url)