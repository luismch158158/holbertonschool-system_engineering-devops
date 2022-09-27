#!/usr/bin/python3
'''
This script make petitions to the Reddit API
'''
import requests


def top_ten(subreddit):
    '''
    Function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
    '''

    if subreddit is None or type(subreddit) is not str:
        print('None')
        return

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    header = {
        'User-Agent': 'MyAgentLE',
    }

    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        print('None')
        return

    top = response.json().get('data').get('children')

    for element in top:
        print(element.get('data').get('title'))
