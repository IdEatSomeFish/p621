class File:
    def __init__(self, file: dict) -> None:
        self.dimensions: list[int] = [
            file['width'],
            file['height'],
        ]
        self.extension: str = file['ext']
        self.size: int = file['size']
        self.md5: str = file['md5']
        self.url: str = file['url']


class Preview:
    def __init__(self, preview: dict) -> None:
        self.dimensions: list[int] = [
            preview['width'],
            preview['height'],
        ]
        self.url: str = preview['url']


class Score:
    def __init__(self, score: dict) -> None:
        self.upvotes: int = score['up']
        self.downvotes: int = -score['down']

    def total(self) -> int:
        return self.upvotes - self.downvotes
    

class Tags:
    def __init__(self, tags: dict) -> None:
        self.general: list[str] = tags['general']
        self.artists: list[str] = tags['artist']
        self.copyrights: list[str] = tags['copyright']
        self.characters: list[str] = tags['character']
        self.species: list[str] = tags['species']
        self.invalid: list[str] = tags['invalid']
        self.meta: list[str] = tags['meta']
        self.lore: list[str] = tags['lore']

    def dump(self) -> list[str]:
        return self.general + self.artists + self.copyrights + self.characters + self.species + self.invalid + self.meta + self.lore


class Post:
    def __init__(self, post: dict) -> None:
        self.id: int = post['id']
        self.description: str = post['description']

        self.file: File = File(post['file'])
        self.preview: Preview = Preview(post['preview'])
        self.sources: list[str] = post['sources']

        self.created_at: str = post['created_at']
        self.updated_at: str = post['updated_at']

        self.score: Score = Score(post['score'])
        self.favorite_count: int = post['fav_count']
        self.comment_count: int = post['comment_count']

        self.tags: Tags = Tags(post['tags'])

        self.change_sequence: int = post['change_seq']

        self.flags: dict = post['flags']
        self.rating: str = post['rating']

        self.pool_ids: list[int] = post['pools']

        self.parent_id: int = post['relationships']['parent_id']
        self.child_ids: list[int] = post['relationships']['children']

        self.approver_id: int = post['approver_id']
        self.uploader_id: int = post['uploader_id']

    def __repr__(self) -> None:
        return f'<Post [{self.id}]>'

    def page_url(self) -> str:
        return f'https://e621.net/posts/{self.id}'

    def download(self, path: str = None) -> None:
        from .interactions import download_post
        download_post(self, path)

    def open(self) -> None:
        from .interactions import open_post
        open_post(self)