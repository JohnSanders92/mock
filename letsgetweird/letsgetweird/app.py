import falcon
import json
from slackclient import SlackClient
from urllib.parse import unquote
import os
import time
slack_token = os.environ["SLACK_AUTH_KEY"]
sc = SlackClient(slack_token)

class LetsGetWeird(object):

    def on_get(self, req, resp):
        print('get')

    def on_post(self, req, resp):
        body = req.stream.read()
        # newBody = unquote(body)
        if not body:
            print('fuck you')
            # sc.api_call("chat.postMessage",
            #         channel="shithole",
            #         text="THERE IS NO BODY",
            #         # username="Francisco Duran"
            # )
        else:
            newBody = body.decode()
            newBody = unquote(newBody)
            newBody = newBody.split('=')[1]

            # newBody = json.loads(newBody.split('=')[1])
            newBody = json.loads(newBody)
            output = LetsGetWeird.mockInput(newBody['message']['text'])
            sc.api_call("chat.postMessage",
                        channel="shithole",
                        text=output,
                        as_user=False,
                        username="mock"
            )

    def mockInput(string):
        oddEven = 0
        output = ''
        for char in string:
            if char == '+':
                char = ' '
            elif char == ' ':
                char = ''
            elif (ord(char) >= 33 and ord(char) <= 64) \
                    or (ord(char) >= 91 and ord(char) <= 96) \
                    or (ord(char) >=123 and ord(char) <= 126):
                char = char
            else:
                if (oddEven % 2 == 0):
                    char = char.upper()
                    oddEven += 1
                elif (oddEven % 2 == 1):
                    char = char.lower()
                    oddEven += 1
            output = output + char

        return output



api = application = falcon.API()
api.add_route('/mock', LetsGetWeird())
