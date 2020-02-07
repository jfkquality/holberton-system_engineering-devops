#!/usr/bin/python3
"""Query Reddit recursively and return all posts of passed endpoint."""
import requests
from sys import argv

def create_list(hot_list, posts, posts_len):
    i = 0
    while i < posts_len:
        # hot_list.append(posts[i]['data']['title'])
        print(posts[i]['data']['title'])
        i += 1
    return (hot_list)
    # hot_list.append(posts[posts_len - 1]['data']['title'])
    # print(posts[posts_len - 1]['data']['title'])

def recurse(subreddit, hot_list=[], nextpage=""):
    """Query Reddit recursively and return all posts of passed endpoint."""

    # print("HOT LIST IS EMPTY")
    if len(argv) < 2:
        return (None)

    base_url = 'https://www.reddit.com'
    query = '/r/' + argv[1] + '/hot.json?after=nextpage'
    print(base_url + query)
    res = requests.get(base_url+query, headers={'User-agent': 'your bot 0.1'})
    if res.status_code != 200:
        return (None)
    print(res.headers.get('Content-Type'))
    about = res.json()
    posts = about['data']['children']
    posts_len = len(posts)
    print("POSTS LENGTH ", posts_len)

    if posts_len == 0:
        return (None)
    hot_list.extend(create_list(hot_list, posts, posts_len))
    # nextpage = posts[posts_len - 1]['data']['after']
    nextpage = about['data']['after']
    print("NEXT PAGE ", nextpage)

    if nextpage:
        (recurse(subreddit, hot_list, nextpage))

    # while i < posts_len:
    #     # hot_list.append(posts[i]['data']['title'])
    #     print(posts[i]['data']['title'])
    #     i += 1

    return (hot_list)
