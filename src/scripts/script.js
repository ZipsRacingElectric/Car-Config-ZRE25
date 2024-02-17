let socket;

function connectWebSocket() {
    socket = new WebSocket('ws://localhost:6789');

    // Event listener for when the connection is established
    socket.addEventListener('open', () => {
        console.log('WebSocket connection established');
    });

    // Event listener for incoming messages
    socket.addEventListener('message', (event) => {
        console.log('Received message:', event.data);
    });

    // Event listener for when the connection is closed
    socket.addEventListener('close', () => {
        console.log('WebSocket connection closed');
    });

    // Event listener for errors
    socket.addEventListener('error', (error) => {
        console.error('WebSocket error:', error);
    });
}

const connectButton = document.getElementById('connectButton');
connectButton.addEventListener('click', connect);

const connect = () => {
    connectWebSocket();
    document.getElementById('status').innerHTML = 'Connected';
};


const disconnectButton = document.getElementById('disconnectButton');
disconnectButton.addEventListener('click', disconnect);

const disconnect = () => {
    if (socket) {
        socket.send('Closing WebSocket connection');
        socket.close();
        console.log('WebSocket connection closed');
        document.getElementById('status').innerHTML = 'Disconnected';
    }
};

const CANview = document.getElementById('CAN');
CANview.addEventListener('click', () => {
    socket.send('CAN')
});
