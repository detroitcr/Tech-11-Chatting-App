// code in JAVASCRIPT
//javascript is non blocking language

console.log('Hello') ///Using JavaScript To Make An API Call

var socket = io();
    
    // socket.on('connect', function() {
    //     socket.emit('my event', {data: 'I\'m connected!'});
    // });
    function send() {
        var Inbox = document.getElementById('Inbox')
    	socket.emit('msg', Inbox.value)
        Inbox.value = ""
    }
socket.on('push',function(data){
    var msgList = document.getElementById('msgList')
    msgList.innerHTML += "<p>" + data + "</p>" 
})

function fetchUsers() {
	fetch('/users').then(function(res){
		res.json().then(function(data){
			console.log(data)
		})
	}) // send request to javascript to use fetch function
}

