import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop

# ////////////////////////////////////////////////////////////////////////////////
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ("connecrion started")

    def on_message(self, message):
        self.write_message("Your message that recived was : " + message)

    def on_close(self):
        print("connection closed")

# ////////////////////////////////////////////////////////////////////////////////
class chatPageHandler(tornado.web.RequestHandler):
    def get(self):
        #self.render("index.html")
        self.render("templates/index.html")
# ////////////////////////////////////////////////////////////////////////////////
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', chatPageHandler),
            (r'/ws', WebSocketHandler)
        ]
        # settings = {
        #     'template_path': 'templates'
        # }
        #tornado.web.Application.__init__(self, handlers, **settings)
        tornado.web.Application.__init__(self, handlers, static_path='static',debug=True)

if __name__ == '__main__':
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()






# import tornado.web
# import tornado.websocket
# import tornado.httpserver
# import tornado.ioloop
#
# # ////////////////////////////////////////////////////////////////////////////////
# class WebSocketHandler(tornado.websocket.WebSocketHandler):
#     def open(self):
#         print ("connecrion started")
#
#     def on_message(self, message):
#         self.write_message("Your message that recived was : " + message)
#
#     def on_close(self):
#         print("connection closed")
#
# # ////////////////////////////////////////////////////////////////////////////////
# class IndexPageHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.render("index.html")
# # ////////////////////////////////////////////////////////////////////////////////
# class Application(tornado.web.Application):
#     def __init__(self):
#         handlers = [
#             (r'/', IndexPageHandler),
#             (r'/websocket', WebSocketHandler)
#         ]
#
#         settings = {
#             'template_path': 'templates'
#         }
#         tornado.web.Application.__init__(self, handlers, **settings)
#
#
# if __name__ == '__main__':
#     ws_app = Application()
#     server = tornado.httpserver.HTTPServer(ws_app)
#     server.listen(8080)
#     tornado.ioloop.IOLoop.instance().start()
