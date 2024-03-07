#!/usr/bin/python3

import json
import requests
import sys

CLIENT_ID = "l-kWeMxr8KBehyspZ-Yy-w"
SECRET_KEY = "FlcinD3d6kmC9B0fHOLrrukf8YlQ0Q"

# Request authorization for the Reddit API
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

# Read password from file
with open('pw.txt', 'r') as f:
    pw = f.read()

# Initialize dictionary with login information
data = {
    'grant_type': 'password',
    'username': 'LeMwaizz',
    'password': pw
}

# Set user agent header
headers = {'User-Agent': 'apiadvanced/0.0.1'}

response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

if response.status_code == 200:
    response_data = response.json()
    # Check if the response contains an access token
    if 'access_token' in response_data:
        token = response_data['access_token']
        # Manually construct the Authorization header with the token
        headers['Authorization'] = 'Bearer {}'.format(token)
    else:
        print("Failed to obtain access token.")
        sys.exit(1)
def number_of_subscribers(subreddit):
    """Query the Reddit API to get the number of subscribers for a given subreddit."""
    
    """assigning the argument to sys module"""
    subreddit = sys.argv[1]
    url = 'https://oauth.reddit.com/r/{}/about'.format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful
    if res.status_code == 200:
        subreddit_info = res.json()
        if 'data' in subreddit_info:
            return subreddit_info['data'].get('subscribers', 0)
        else:
            return 0
    else:
        # Check for redirect status code indicating invalid subreddit
        if response.status_code == 302:
            return 0  # Invalid subreddit, return 0 subscribers
        else:
            return 0


