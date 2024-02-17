import asyncio
import websockets
import logging

async def handle_message(websocket, message):
    if message == "CAN start":
        logging.info("Starting CAN")
        message = "CAN"
        await send_message(websocket, message)
        return message


async def send_message(websocket, message):
    await websocket.send(message)

async def websocket_handler(websocket, path):
    try:
        while True:
            print("Waiting for message from client...")
            # Wait for any message from the client
            message = await websocket.recv()
            print(f"Received message from client: {message}")
            # Call the function based on the received message
            await handle_message(websocket, message)
            # Send a response back to the client
            response = f"Message received: {message}"
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosedOK:
        logging.error("Connection closed")
        return
# Start the server
def main():
    start_server = websockets.serve(websocket_handler, "localhost", 6789)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()