#!/usr/bin/python3
"""
A function that queries the reddit API.
"""


import json
import requests
import sys

CLIENT_ID = "XCDVknlXgCP7m5P-v1azPw"
SECRET_KEY = "g6JwkdLNyEVmzBkJ1HtgWLlweFai6A"

"""request authorization for the reddit api"""
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

"""read password"""
with open('pw.txt', 'r') as f:
     pw = f.read()

"""initialize dictionary with login information"""
data = {
	'grant_type': 'password',
	'username': 'LeMwaizz',
	'password' : pw
	}
headers = {'User-Agent': 'apiadvanced/0.0.2'}

"""request to use reddit api"""
res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers).json()
TOKEN = res['access_token']
print(res.json())
headers['Authorization'] = "bearer {}".format(TOKEN) #adding token
def number_of_subscribers(subreddit):
    """this function queries the reddit API""" 
    
    url = 'https://oauth.reddit.com/r/{}/about'.format(subreddit)
    res1 = requests.get(url, headers=headers).json()
    if 'data' in res1:
       return res1['data']['subscribers']
    else:
       return 0
subreddit = sys.argv[1]
print(number_of_subscribers(subreddit))
