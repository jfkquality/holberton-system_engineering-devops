#!/usr/bin/python3
"""Query Reddit and return total subscribers of passed endpoint."""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """Query Reddit and return total subscribers of passed endpoint."""
    base_url = 'https://www.reddit.com'
    query = '/r/' + argv[1] + '/about.json'
    if len(argv) < 2:
        return (0)
    res = requests.get(base_url + query, headers = {'User-agent': 'your bot 0.1'})
    if res.status_code != 200:
        return 0
    about = res.json()
    return (about['data']['subscribers'])
