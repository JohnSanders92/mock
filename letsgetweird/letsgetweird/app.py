import falcon
import json

class LetsGetWeird(object):

    def on_get(self, req, resp):
        print('get')

    def on_post(self, req, resp):
        data = json.loads(req.stream.read())

        resp.body = json.dumps(data)

api = application = falcon.API()
api.add_route('/mock', LetsGetWeird())
