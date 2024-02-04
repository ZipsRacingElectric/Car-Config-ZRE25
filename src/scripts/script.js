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

// Function to handle button click event
function connect() {
    connectWebSocket();
    document.getElementById('status').innerHTML = 'Connected';
}

// Function to handle disconnect button click event
function disconnect() {
    if (socket) {
        socket.send('Closing WebSocket connection');
        socket.close();
        console.log('WebSocket connection closed');
        document.getElementById('status').innerHTML = 'Disconnected';
    }
}

// Get the button elements
const connectButton = document.getElementById('connectButton');

const disconnectButton = document.getElementById('disconnectButton');

const CANview = document.getElementById('CAN');

// Add event listeners to the buttons
connectButton.addEventListener('click', connect);

disconnectButton.addEventListener('click', disconnect);

CANview.addEventListener('click', function() {
    socket.send('CAN');
});

