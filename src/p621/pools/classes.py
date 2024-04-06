class Pool:
    def __init__(self, pool: dict) -> None:
        self.id: int = pool['id']
        self.name: str = pool['name']
        self.description: str = pool['description']
        self.post_count: int = pool['post_count']

        self.created_at: str = pool['created_at']
        self.updated_at: str = pool['updated_at']

        self.category: str = pool['category']
        self.is_active: bool = pool['is_active']

        self.post_ids: list[int] = pool['post_ids']

        self.creator_id: int = pool['creator_id']
        self.creator_name: str = pool['creator_name']

    def page_url(self) -> str:
        return 'https://e621.net/pools/' + str(self.id)