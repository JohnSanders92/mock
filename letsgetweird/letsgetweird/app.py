import falcon


class LetsGetWeird(object):

    def on_get(self, req, resp):
        print('get')

    def on_post(self,req, resp):
        print('post')


api = application = falcon.API()
api.add_route('/mock', LetsGetWeird())
