# this file contains example for using the auth system.
#
import requests
import json

# Define user login data
data = {"username": "insert_username_here", "password": "insert_password_here"}

# request to get refresh_token
resp = requests.post(
    "http://localhost:5001/token",
    data=data,
)
refresh_token = resp.json()["refresh"]

# json.dumps is required, otherwise `requests` will try to send form.
# request to get access_token
access_token_resp = requests.post(
    "http://localhost:5001/authenticate",
    data=json.dumps({"refresh_token": refresh_token}),
    headers={"Content-type": "application/json", "accept": "application/json"},
)


# And to test that all is working, running this section as well.
# You need to pass in the token to get your userinformation.
access_token = access_token_resp.json()["access_token"]
foo = requests.get(
    "http://localhost:5001/users/me",
    headers={"Authorization": f"Bearer {access_token}"},
)