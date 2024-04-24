var socket = new WebSocket("ws://localhost:8000/ws/random_number/");

socket.onmessage = function (event) {
    var data = JSON.parse(event.data)
    console.log(data)
    document.getElementById('random_number').innerText = data.message;
};