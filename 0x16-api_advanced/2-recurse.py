#!/usr/bin/python3
"""Query Reddit recursively and return all posts of passed endpoint."""
import requests
from sys import argv


def create_list(hot_list, posts, posts_len):
    i = 0
    while i < posts_len:
        hot_list.append(posts[i]['data']['title'])
        # print(posts[i]['data']['title'])
        i += 1
    return (hot_list)


def recurse(subreddit, hot_list=[], nextpage=None):
    """Query Reddit recursively and return all posts of passed endpoint."""

    if len(argv) < 2:
        return (None)

    base_url = 'https://www.reddit.com'
    query = '/r/' + argv[1] + '/hot.json'  # ?after=nextpage'
    payload = {'after': nextpage, 'limit': 100}
    res = requests.get(base_url+query, params=payload,
                       headers={'User-agent': 'your bot 0.1'})
    if res.status_code != 200:
        return (None)
    about = res.json()
    posts = about['data']['children']
    posts_len = len(posts)

    if posts_len == 0:
        return (None)
    (create_list(hot_list, posts, posts_len))
    nextpage = about['data']['after']

    if nextpage:
        (recurse(subreddit, hot_list, nextpage))

    return (hot_list)
