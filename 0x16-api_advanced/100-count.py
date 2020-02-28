#!/usr/bin/python3
"""Query Reddit recursively and return all posts sorted of passed keywords."""
import requests
from sys import argv


def create_list(hot_list, posts, posts_len):
    i = 0
    while i < posts_len:
        hot_list.append(posts[i]['data']['title'])
        # print(posts[i]['data']['title'])
        i += 1
    return (hot_list)


def count_words(subreddit, word_list, hot_list=[], nextpage=None):
    """Query Reddit recursively and return sorted posts of passed keywords."""

    if len(argv) < 2:
        return (None)

    base_url = 'https://www.reddit.com'
    query = '/r/' + argv[1] + '/hot.json'  # ?after=nextpage'
    payload = {'after': nextpage, 'limit': 100, 'q': argv[len(argv) - 1]}
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
        (count_words(subreddit, word_list, hot_list, nextpage))
    else:
        keywords = argv[2].split()  # parse the keywords string by spaces
        count_dict = {}
        # Loop thru hot_list for each word in word_list with count() function
        for word in keywords:
            counts = 0
            for title in hot_list:
                counts += title.lower().count(word.lower())
            if word.lower() not in count_dict.keys():
                count_dict[word.lower()] = counts
        count_sorted = sorted(count_dict, key=count_dict.get, reverse=True)
        for k in count_sorted:
            if count_dict[k] > 0:
                print("{}: {}".format(k, count_dict[k]))
# for k, v in count_dict.items():
# for k, v in sorted(count_dict.items(), key=lambda kv: kv[1], reverse=True):
# counts = [hot_list.count(word) for word in keywords]  # list comprehension
# count_dict[word] = hot_list.count(word)

        # for k, v in sorted(count_dict.items(), reverse=True):
        #     if v > 0:
        #         print("{}: {}".format(k.lower(), v))
