#!/usr/bin/python3
"""A script to retrieve top posts from Reddit API."""

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

def top_ten(subreddit):
    """Query the Reddit API to get the titles of the first 10 hot posts for a given subreddit."""
    subreddit = sys.argv[1]
    url = 'https://oauth.reddit.com/r/{}/hot'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful
    if response.status_code == 200:
        subreddit_info = response.json()
        if 'data' in subreddit_info and 'children' in subreddit_info['data']:
            # Extract the list of posts
            posts = subreddit_info['data']['children']
            # Print the titles of the first 10 posts
            for post in posts[:10]:
                hots = post['data']['title']
    else:
        return None
    return hots

