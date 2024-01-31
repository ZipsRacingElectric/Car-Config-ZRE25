var socket = null;

document.getElementById('connectButton').onclick = function() {
    // Connect to WebSocket server
    socket = new WebSocket("ws://localhost:6789");

    socket.onopen = function(e) {
        console.log("[open] Connection established");
        document.getElementById('status').textContent = "Connected";
        this.disabled = true;
        document.getElementById('disconnectButton').disabled = false;
    };

    socket.onmessage = function(event) {
        console.log(`[message] Data received from server: ${event.data}`);
        var messages = document.getElementById('messages');
        messages.innerHTML += `<div>${event.data}</div>`;
    };

    socket.onclose = function(event) {
        if (event.wasClean) {
            console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
        } else {
            console.error('[close] Connection died');
        }
        document.getElementById('status').textContent = "Disconnected";
        document.getElementById('connectButton').disabled = false;
        this.disabled = true;
    };

    socket.onerror = function(error) {
        console.error(`[error] ${error.message}`);
    };
};

document.getElementById('disconnectButton').onclick = function() {
    if (socket) {
        socket.close();
    }
};