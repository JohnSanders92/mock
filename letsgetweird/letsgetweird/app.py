import falcon
import json
from slackclient import SlackClient


class LetsGetWeird(object):

    def on_get(self, req, resp):
        print('get')

    def on_post(self, req, resp):
        data = json.loads(req.stream.read())
        # message = data['message']['text']
        # resp.body = json.dumps(data)
        
        slack_token = os.environ["xoxp-304305798082-304290752420-585706548595-acee226ba455c89cdd3a54a514af7724"]
        sc = SlackClient(slack_token)

        sc.api_call(
          "chat.postMessage",
          channel="shithole",
          text="Hello from Python! :tada:"
        )


api = application = falcon.API()
api.add_route('/mock', LetsGetWeird())
