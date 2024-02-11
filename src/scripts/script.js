let socket;
const canMessageElement = document.getElementById('messages');

function connectWebSocket() {
    socket = new WebSocket('ws://localhost:6789');

    // Event listener for when the connection is established
    socket.addEventListener('open', () => {
        console.log('WebSocket connection established');
    });

    // Event listener for incoming messages
    socket.addEventListener('message', (event) => {
        console.log('Received message:', event.data);
        canMessageElement.textContent += event.data + '\n';
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
connectButton.addEventListener('click', () => {
    connectWebSocket();
    document.getElementById('status').innerHTML = 'Connected';
});

const disconnectButton = document.getElementById('disconnectButton');
disconnectButton.addEventListener('click', () => {
    if (socket) {
        socket.send('Closing WebSocket connection');
        socket.close();
        document.getElementById('status').innerHTML = 'Disconnected';
    }
});

const CANview = document.getElementById('CAN');
CANview.addEventListener('click', () => {
    socket.send('CAN');
    openMessageWindow();
});

// Open a new window with a message input box
function openMessageWindow() {
    const messageWindow = window.open('', 'Message Window', 'width=400,height=200');
    messageWindow.document.write(`
        <h2>Message Box</h2>
        <textarea id="messageInput" rows="4" cols="50"></textarea>
        <br>
        <button onclick="sendMessage()">Send Message</button>
    `);
    messageWindow.sendMessage = function() {
        message = messageWindow.document.getElementById('messageInput').value;
        socket.send(message);
    };
}

const openWindowButton = document.getElementById('openWindowButton');
openWindowButton.addEventListener('click', openMessageWindow);
