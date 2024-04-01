**unfinished!**

# p621
an oversimplified wrapper and interactivity for the **e621** API

## features
### current
- searching posts
- listing favorites
- downloading posts
- opening posts

### future
- creating and updating posts
- creating and updating pools
- favoriting and unfavoriting posts
- voting posts
- listing tags

## example
```python
>>> import p621
>>> posts = p621.search_posts('####', '####', limit = 10, tags = ['male/male', 'cat', 'bird'])
>>> for post in posts:
...     print(post.id, post.file.extension)
...     post.download()
...
4689397 jpg
4689236 jpg
4683029 png
4681267 jpg
4679249 png
4671358 png
4660654 png
4657220 png
4650173 jpg
4642501 jpg
```