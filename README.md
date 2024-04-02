**unfinished!**

# p621
an oversimplified wrapper and interactivity for the **e621** API

## features
### current
- searching posts
- listing favorites
- getting posts
- downloading posts
- opening posts

### future
- creating and updating posts
- creating and updating pools
- favoriting and unfavoriting posts
- voting posts
- listing tags

## installation
```console
$ python -m pip install p621
```

## documentation
**[documentation can be found here](docs/index.adoc)**

## example
### getting post
```python
>>> import p621
>>> post = p621.get_post('###', '###', 4517306)
>>> post.created_at
'2024-01-05T23:48:13.417-05:00'
>>> post.favorite_count
75
>>> post.file.extension
'jpg'
>>> post.page_url()
'https://e621.net/posts/4517306'
>>> post.tags.dump()
['anthro', 'band-aid', 'band-aid_on_face', 'band-aid_on_nose', 'bandage', 'bandage_on_face', 'bandage_on_nose', 'black_body', 'black_fur', 'cheek_tuft', 'chest_tuft', 'emoji', 'facial_tuft', 'fur', 'grey_body', 'grey_fur', 'half-closed_eyes', 'male', 'narrowed_eyes', 'simple_background', 'solo', 'text', 'tuft', 'wide_eyed', 'xing1', 'nick_(the_xing1)', 'lagomorph', 'leporid', 'mammal', 'rabbit', '1:1', 'absurd_res', 'english_text', 'hi_res']
>>> post.open()
```

### searching posts
```python
>>> import p621
>>> posts = p621.search_posts('###', '###', limit = 10, tags = ['male/male', 'cat', 'bird'])
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