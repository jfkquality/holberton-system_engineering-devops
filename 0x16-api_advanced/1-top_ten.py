#!/usr/bin/python3
"""Query Reddit and return top ten posts of passed endpoint."""
import requests
from sys import argv


def top_ten(subreddit):
    """Query Reddit and return total subscribers of passed endpoint."""
    base_url = 'https://www.reddit.com'
    query = '/r/' + argv[1] + '/hot.json'
    if len(argv) < 2:
        print('None')
        return (0)
    res = requests.get(base_url+query, headers={'User-agent': 'your bot 0.1'})
    if res.status_code != 200:
        print('None')
        return (0)
    about = res.json()
    posts = about['data']['children']
    i = 0
    while i < 10:
        print(posts[i]['data']['title'])
        i += 1
