import asyncio
import websockets

# Define a WebSocket handler
async def websocket_handler(websocket, path):
    try:
        while True:
            message = await websocket.recv()
            # Process the message as needed
            # You can also send messages back to the frontend using `await websocket.send(response)`
    except websockets.exceptions.ConnectionClosed:
        pass

# Start the WebSocket server
start_server = websockets.serve(websocket_handler, "69.42.0.69", 4200)  # Replace with your IP and port
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()