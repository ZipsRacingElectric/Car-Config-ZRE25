import asyncio
import websockets

async def handle_message(message):
    if message == "CAN":
        print("CAN")
        message = "CAN"
        return message


async def websocket_handler(websocket, path):
    while True:
        print("Waiting for message from client...")
        # Wait for any message from the client
        message = await websocket.recv()
        print(f"Received message from client: {message}")
        # Call the function based on the received message
        await handle_message(message)
        # Send a response back to the client
        response = f"Message received: {message}"
        await websocket.send(response)

# Start the server
start_server = websockets.serve(websocket_handler, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
