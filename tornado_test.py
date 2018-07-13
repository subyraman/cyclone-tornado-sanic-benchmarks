import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
import logging

from tornado.options import define, options

define("port", default=8080, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps({'hello': 'world'}))


def main():
    tornado.options.parse_command_line()
    logging.getLogger('tornado.access').disabled = True
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()