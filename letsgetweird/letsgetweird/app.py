import falcon
import json
from slackclient import SlackClient


class LetsGetWeird(object):

    def on_get(self, req, resp):
        print('get')

    def on_post(self, req, resp):
        data = json.loads(req.stream.read())
        # message = data['message']['text']
        resp.body = json.dumps(data)



api = application = falcon.API()
api.add_route('/mock', LetsGetWeird())
