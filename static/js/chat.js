var webSocket;
var loginName;
var msgToSend='';
//port=8080;

$(function(){
	//************ get chat room name and Type from Query String
	var chatRoom =getQueryStringValue("chatRoomName")
	var roomType =getQueryStringValue("room")
	console.log("chatRoom : ",chatRoom);

	///************ save login Name of the client  in session storage
	loginName = sessionStorage.getItem('loginName');
	console.log("LoginName",loginName);
	// test= sessionStorage.getItem('x');
	// console.log("?????????????????????",test)
	//************ set value of user name and group chat
	$("#userNameChat").html(loginName);
	$("#groupNameChat").html(chatRoom);

	//***************** Start web Socket


	webSocket = new WebSocket("ws://localhost:8080/ws");

	webSocket.onopen=function(){
		var notifyMsg ={"msgType":'Notify',"loginName":loginName,"content":msgToSend,"chatRoom":chatRoom,"roomType":roomType};
		//***************** send JSON file to server 'msg'
		webSocket.send(JSON.stringify(notifyMsg));
		//webSocket.send("saas");
	}
	//*****************  recieve Msg from server
	webSocket.onmessage = function(e){
		console.log("msg from client: ",loginName);  /// String
		console.log(e.data);
		msg_obj=JSON.parse(e.data)  //{"msgType":"Message","loginName":loginName,"content":msgToSend,"chatRoom":chatRoom,"roomType":roomType};
		console.log(msg_obj)

		switch (msg_obj.msgType) {
				case "loadMsgs":
					$("#overOldMsg").html('')
					console.log("LOAD DB Msggggggggggggggggggggggggggggggg")
					var DBsenderArray = msg_obj.DBsenders.split('>>');
					console.log(DBsenderArray)
					var DBmsgArray = msg_obj.DBmsgs.split('>>');
					console.log(DBmsgArray)
					for (var i=0;i<DBmsgArray.length;i++){
						$("#overOldMsg").append('<p style="float:left;color: blue">'+DBsenderArray[i]+': </p>');
						$("#overOldMsg").append('<p>'+DBmsgArray[i]+'</p>');
					}
					//$("#overOldMsg").append('<p style="float:left;color: blue">'+msg_obj.DBsenders+': </p>');
					//$("#overOldMsg").append('<p>'+msg_obj.DBmsgs+'</p>');
					break;
                case "onlineFriendsMsg":
					console.log("offlineFriendsMsggggggggggggggggggggggggggggggg")
					$("#olineList").html('');
					var onlineArray = msg_obj.onlineList.split(' ');
					console.log(onlineArray);
					onlineArray.forEach(function(c){
						$("#olineList").append("<li>"+c+"</li>");
					});
					break;
				case "offlineFriendsMsg":
					console.log("offlineFriendsMsggggggggggggggggggggggggggggggg")
					$("#offlineList").html('');
					var offlineArray = msg_obj.offlineList.split(' ');
					console.log(offlineArray)
					offlineArray.forEach(function(c){
						$("#offlineList").append("<li>"+c+"</li>");
					});
					break;

                case "Message":
					if (msg_obj.content != ''){
						console.log("lllllllllllllllllll")
						if(msg_obj.roomType =='private'){
							console.log("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
							$('#overOldMsg').html('')
						}
						$("#over").append('<p style="float:left;color: blue">'+msg_obj.loginName+': </p>');
						$("#over").append('<p>'+msg_obj.content+'</p>');
					}
					else {
						console.log("Empty Msg");
					}
					break;
            }
	}
	//***************** On click "send" Button
	$("#sendMsg").click(function(e){
		msgToSend= $("#msgText").val();
		$("#msgText").val('');
		var chatMsg ={"msgType":"Message","loginName":loginName,"content":msgToSend,"chatRoom":chatRoom,"roomType":roomType};
		//***************** send JSON file to server 'msg'
		webSocket.send(JSON.stringify(chatMsg));

	})

	//***************** this function return value of query String
	function getQueryStringValue (key) {
	  return decodeURIComponent(window.location.search.replace(new RegExp("^(?:.*[&\\?]" + encodeURIComponent(key).replace(/[\.\+\*]/g, "\\$&") + "(?:\\=([^&]*))?)?.*$", "i"), "$1"));
	}

})
