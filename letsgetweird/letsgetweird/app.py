import falcon
import json
from .config import slack_auth
sc = slack_auth()


class LetsGetWeird(object):

    def on_get(self, req, resp):
        print('get')

    def on_post(self, req, resp):
        data = json.loads(req.stream.read())
        # message = data['message']['text']
        # resp.body = json.dumps(data)
        sc.api.call("chat.postMessage",
                    channel="shithole",
                    text="Hello from Python! :tada:"
        )



api = application = falcon.API()
api.add_route('/mock', LetsGetWeird())
