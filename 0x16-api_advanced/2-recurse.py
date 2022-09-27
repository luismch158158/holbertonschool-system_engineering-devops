#!/usr/bin/python3
import requests
'''
This script make petitions to the Reddit API
'''

header = {
        'User-Agent': 'MyAgentLE',
}


def recurse(subreddit, hot_list=[]):
    '''
    recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None
    '''
    if subreddit is None or type(subreddit) is not str:
        return

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code != 200:
        return (None)

    len_hotlist = len(hot_list)

    data = response.json().get('data')
    array_elements = data.get('children')
    if (len_hotlist != len(array_elements)):
        new_element = array_elements[len_hotlist].get('data').get('title')
        hot_list.append(new_element)
        # print()
        # print(hot_list)
        # print()
        recurse(subreddit, hot_list)

    return hot_list
