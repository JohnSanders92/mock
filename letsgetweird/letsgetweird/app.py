import falcon
import json
import requests
from slackclient import SlackClient
import os


class LetsGetWeird(object):

    def on_get(self, req, resp):
        print('get')

    def on_post(self, req, resp):
        data = json.loads(req.stream.read())

        slack_token = os.environ["SLACK_AUTH_KEY"]
        sc = SlackClient(slack_token)
        sc.api_call("chat.postMessage",
                    channel="shithole",
                    text="test",
                    # username="Francisco Duran"
        )


api = application = falcon.API()
api.add_route('/mock', LetsGetWeird())
