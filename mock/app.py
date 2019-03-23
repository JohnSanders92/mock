import falcon

class Mock(object):

    def on_get(self, req, resp):
        print()

    def on_post(self, req, resp):
        print()

app = falcon.API()
mock = Mock()
app.add_route("/mock", mock)

