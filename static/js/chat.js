// var webSocket;
// $(function(){
// 	webSocket= new WebSocket("ws://localhost:8888/ws");
// 	webSocket.onmessage = function(e){
// 		console.log(e.data);
// 	}
// 	// webSocket.onclose = function(e){
// 	// 	// console.log(e);
// 	// }
// 	$('#send').click(function(e){
// 		var msg = $("#message").val()
// 		webSocket.send(msg)
// 		$("#message").val('')
// 	})
// })


var ws;

function onLoad() {
	ws = new WebSocket("ws://localhost:8080/websocket");

	/// when massage recived from server
	ws.onmessage = function(e) {
	   //alert(e.data);
	   console.log(e.data)
	};
}

function sendMsg() {
	ws.send(document.getElementById('msg').value);
	ws.send("hello from client")
}
