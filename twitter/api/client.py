from _pytest.assertion import AssertionState
from config import Config
import requests
import json

class TwitterAPI:

    BASE_URL = "https://api.twitter.com/2/"

    def __init__(self, api_key, secret, token):
        self.API_KEY = api_key
        self.SECRET = secret
        self.BEARER_TOKEN = token

    def request_header(self):
        return {"Authorization": f"Bearer {self.BEARER_TOKEN}"}

    def _get_request(self, endpoint, params={}):
        resp = requests.request("GET", endpoint, headers=self.request_header(), params=params)
        if resp.status_code != 200:
            raise Exception( f"Request returned an error: {resp.status_code} {resp.text}")
        return resp.json()

    def get_user(self, username):
        endpoint = self.BASE_URL+f"users/by?usernames={username}"
        resp = self._get_request(endpoint)
        if "data" not in resp.keys():
            raise AssertionError(f"User not found: {username}")
        if len(resp["data"]) != 1:
            raise AssertionError(f"Multiple users found with username: {username}")
        return resp["data"][0]

    def get_tweets(self, user_id):
        endpoint = self.BASE_URL+f"users/{user_id}/tweets"
        params = {
            "tweet.fields": "created_at"
        }
        resp = self._get_request(endpoint, params=params)
        return resp

    def get_tweet(self, tweet_id):
        endpoint = self.BASE_URL+f"tweets?ids={tweet_id}"
        resp = self._get_request(endpoint)
        return resp

    def get_latest_tweet(self, user_id):
        tweets = self.get_tweets(user_id)
        if "data" not in tweets.keys():
            raise AssertionError(f"No tweet found for user {user_id}")
        newest_id = tweets["meta"]["newest_id"]
        latest_tweet = self.get_tweet(newest_id)
        if "data" not in latest_tweet.keys():
            raise AssertionError(f"Latest tweet id {newest_id} found for user {user_id}")
        return latest_tweet["data"][0]
