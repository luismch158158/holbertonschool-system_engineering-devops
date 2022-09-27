#!/usr/bin/python3
'''
This script make petitions to the Reddit API
'''

import requests

header = {
        'User-Agent': 'MyAgentLE',
}


def recurse(subreddit, hot_list=[], after="", counter=0):
    '''
    recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None
    '''

    url = 'https://www.reddit.com/r/{}/hot.json?after={}#'.format(
                                                            subreddit, after)

    if after is not None:
        response = requests.get(url, headers=header, allow_redirects=False)

        if (response.status_code != 200):
            return (None)

        data = response.json().get('data')
        array_elements = data.get('children')
        after = data.get('after')

        # print()
        # print()
        # print()
        # print('REQUEST N°: {}'.format(counter))
        # print()
        # print()
        # print()
        # print()
        appender(hot_list, array_elements, 0)
        recurse(subreddit, hot_list, after, counter + 1)

    return hot_list


def appender(hot_list, childrens, counter):
    '''
    This function will be append to the list for each request
    '''
    if (counter != len(childrens)):

        new_element = childrens[counter].get('data').get('title')
        # print(new_element)
        hot_list.append(new_element)
        appender(hot_list, childrens, counter + 1)
