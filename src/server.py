import asyncio
import websockets
import logging
import can
import cantools

async def handle_message(websocket, message):
    if message == "Meow":
        logging.info("Starting CAN")
        message = "CAN"
        message = reader(message)
        await send_message(websocket, message)

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
    
def reader(message):
    can_bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
    db = cantools.database.load_file('../database/Main_2023.dbc')
    while True: 
        message = can_bus.recv(timeout=1.0)
        if message is not None:
            message = db.decode_message(message.arbitration_id, message.data)
            print(message)
            return message

# Start the server
def main():
    start_server = websockets.serve(websocket_handler, "localhost", 6789)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()



if __name__ == "__main__":
    main()