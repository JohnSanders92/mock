import falcon
import json

class LetsGetWeird(object):

    def on_get(self, req, resp):
        print('get')

    def on_post(self, req, resp):
        data = json.loads(req.stream.read())
        # message = data['message']['text']
        response = {
            "text": "I've been hacked",
            "response_type": "in_channel"
        }
        resp.body = json.dumps(response)

api = application = falcon.API()
api.add_route('/mock', LetsGetWeird())
