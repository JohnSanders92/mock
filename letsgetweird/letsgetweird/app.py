import falcon
import json
import requests
from slackclient import SlackClient
from urlib.parse import unquote
import os
slack_token = os.environ["SLACK_AUTH_KEY"]
sc = SlackClient(slack_token)

class LetsGetWeird(object):

    def on_get(self, req, resp):
        print('get')

    def on_post(self, req, resp):
        body = req.stream.read()
        if not body:
            print('fuck you')
            # sc.api_call("chat.postMessage",
            #         channel="shithole",
            #         text="THERE IS NO BODY",
            #         # username="Francisco Duran"
            # )
        else:
            # body = json.loads(body.decode('utf-8'))
            # print(body)
            newBody = unquote.parse(body)
            sc.api_call("chat.postMessage",
                        channel="shithole",
                        text=newBody,
                        # username="Francisco Duran"
            )



api = application = falcon.API()
api.add_route('/mock', LetsGetWeird())
