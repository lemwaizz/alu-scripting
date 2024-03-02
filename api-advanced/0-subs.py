#!/usr/bin/python3
"""
A function that queries the reddit API.
"""


import json
import requests
import sys

CLIENT_ID = "l-kWeMxr8KBehyspZ-Yy-w"
SECRET_KEY = "FlcinD3d6kmC9B0fHOLrrukf8YlQ0Q"

"""request authorization for the reddit api"""
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

"""read password"""
with open('pw.txt', 'r') as f:
     pw = f.read()

"""initialize dictionary with login information"""
data = {
	'grant_type': 'password'
	'username': 'LeMwaizz'
	'password' : pw
	}
headers = {'User-Agent': 'apiadvanced/0.0.1'}

"""request to use reddit api"""
res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
TOKEN = res.json()['access_token']
headers['Authorization'] = f'bearer {TOKEN}' #adding token
if __name__ == "__main__":
	def number_of_subscribers(subreddit):
	    """this function queries the reddit API""" 
