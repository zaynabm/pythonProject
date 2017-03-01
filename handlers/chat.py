from tornado import web,websocket

clients = []
class WSHandler(websocket.WebSocketHandler):
	def open(self):
		clients.append(self)


	def on_message(self,message):
		for c in clients:
			if c is not self:
				c.write_message("Message:"+message)

class ChatHandler(web.RequestHandler):
	def get(self):
		self.render("../templates/chat.html")
		print ("this is chat handler")
