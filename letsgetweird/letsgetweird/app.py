import falcon
import json
from slackclient import SlackClient
from urllib.parse import unquote
import os
import requests

slack_token = os.environ["SLACK_AUTH_KEY"]
sc = SlackClient(slack_token)

class LetsGetWeird(object):

    def on_get(self, req, resp):
        print('get')

    def on_post(self, req, resp):
        body = req.stream.read()
        if not body:
            print('')

        else:
            body = body.decode()
            body = unquote(body)
            body = body.split('=')[1]
            body = json.loads(body)
            userIds = LetsGetWeird.getMentions(body['message']['text'])
            mentions = LetsGetWeird.getUserInfo(userIds)

            # url = "https://slack.com/api/users.info"
            # params = {
            #     'user':body['user']['id'],
            #     'token':slack_token
            # }
            # userInfo = requests.get(url=url, params=params)
            # userInfo = userInfo.json()
            output = LetsGetWeird.mockInput(body['message']['text'])
            sc.api_call("chat.postMessage",
                        channel=body['channel']['id'],
                        text=body,
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

    def getMentions(string):
        array = []
        string = string.split("+")
        for x in string:
            if x[0] == '@':
                array.append(x)
        return array

    def getUserInfo(userIds):
        array = []
        for userId in userIds:

            url = "https://slack.com/api/users.info"
            params = {
                'user': userId[1:],
                'token': slack_token
            }
            userInfo = requests.get(url=url, params=params)
            userInfo = userInfo.json()
            userInfo = userInfo['user']['profile']['display_name']
            array.append(userInfo)
        return array


api = application = falcon.API()
api.add_route('/mock', LetsGetWeird())
