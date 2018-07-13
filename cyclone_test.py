import cyclone.web
from twisted.internet import reactor
import json
from twisted.internet import defer
from twisted.internet import reactor


class MainHandler(cyclone.web.RequestHandler):
    @defer.inlineCallbacks
    def get(self):
        yield defer.callLater(reactor, .25)
        self.set_header('Content-Type', 'application/json')

        self.write(json.dumps({'hello': 'world'}))


if __name__ == "__main__":
    application = cyclone.web.Application([
        (r"/", MainHandler),
    ])
    reactor.listenTCP(8080, application)
    reactor.run()