#!/usr/bin/env python3

import asyncio
import websockets
import logging
import can
import cantools
import json

async def handle_message(websocket, message):
    if message == "Meow":
        logging.info("Starting CAN")
        message = "CAN"
        await send_message(websocket)

# TODO: JSON dump the message as float instead of int
db = cantools.database.load_file('../database/Main_2023.dbc')
async def send_message(websocket):
    bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
    try:
        while True:
            message = bus.recv()
            print(f"ID: {message.arbitration_id}, Data: {message.data}")
            
            # Find the CAN message in the DBC file
            can_message = db.get_message_by_frame_id(message.arbitration_id)
            
            # Decode the CAN message
            data_dict = can_message.decode(message.data)
            
            # Convert the dictionary to a JSON string
            message2 = json.dumps(data_dict)
            
            # Send the message over the WebSocket
            await websocket.send(message2)
            
            # Add a small delay to allow other tasks to run
            await asyncio.sleep(0.01)
    finally:
        bus.shutdown()

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