#!/usr/bin/python3
'''
This script make petitions to the Reddit API
'''
import requests


def number_of_subscribers(subreddit):
    '''
    Function that queries the Reddit API and returns the number
    of subscribers for a given subreddit
    '''

    if subreddit is None or type(subreddit) is not str:
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    header = {
        'User-Agent': 'MyAgentLE',
    }

    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get('data', {}).get('subscribers', 0)
