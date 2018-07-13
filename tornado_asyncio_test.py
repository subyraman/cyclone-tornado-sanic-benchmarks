import asyncio

import tornado.concurrent
import tornado.ioloop
import tornado.web
import tornado.platform.asyncio
import tornado.httpclient
import json


class ReqHandler(tornado.web.RequestHandler):
    async def get(self):
        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps({'hello': 'world'}))


app = tornado.web.Application([
  (r'/', ReqHandler)
])

if __name__ == '__main__':
    tornado.platform.asyncio.AsyncIOMainLoop().install()
    app.listen(8080)
    asyncio.get_event_loop().run_forever()