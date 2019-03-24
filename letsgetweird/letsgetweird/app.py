import falcon
import json
import requests
from slackclient import SlackClient
from .config import token

class LetsGetWeird(object):

    def on_get(self, req, resp):
        print('get')

    def on_post(self, req, resp):


        # slack_token = "xoxp-304305798082-304290752420-577292894305-92e1cae38b04a2896605648c3a62c183"
        sc = SlackClient(token)
        sc.api_call("chat.postMessage",
                    channel="shithole",
                    text="Go fuck yourself"
        )

api = application = falcon.API()
api.add_route('/mock', LetsGetWeird())
