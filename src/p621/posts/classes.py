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


class Post:
    def __init__(self, post: dict) -> None:
        self.id: int = post['id']
        self.description: str = post['description']

        self.created_at: str = post['created_at']
        self.updated_at: str = post['updated_at']

        self.file: File = File(post['file'])
        self.preview: Preview = Preview(post['preview'])
        self.sources: list[str] = post['sources']

        self.score: Score = Score(post['score'])
        self.favorite_count: int = post['fav_count']
        self.comment_count: int = post['comment_count']

        self.tags: Tags = Tags(post['tags'])

        self.change_sequence: int = post['change_seq']

        self.flags: dict = post['flags']
        self.rating: str = post['rating']

        self.pools: list[str] = post['pools']

        self.parent: int = post['relationships']['parent_id']
        self.children: list[str] = post['relationships']['children']

        self.approver_id: int = post['approver_id']
        self.uploader_id: int = post['uploader_id']