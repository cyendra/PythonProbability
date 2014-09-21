import sys
import json
import requests
from requests.auth import HTTPBasicAuth
data ='{"scopes":["repo"]}'

#user = sys.argv[1]
#pw = sys.argv[2]
"""
user = "cyendra"
pw = "super430"
r = requests.post("https://api.github.com/authorizations",data=data,auth=HTTPBasicAuth(user, pw))
res = r.json()
print res
if('token' in res.keys()):
	print res['token']
else:
	print res['message']

"""

r = requests.get("https://github.com/login/oauth/authorize")
print r