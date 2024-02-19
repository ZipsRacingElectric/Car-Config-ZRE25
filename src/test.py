#!/usr/bin/env python3
import cantools
import random
import can
# Load the DBC file
db = cantools.database.load_file('../database/Main_2023.dbc')

# Choose a message from the DBC
message_name = 'Input_Pedals'  # Replace with your actual message name
message = db.get_message_by_name(message_name)

# Generate random data for the message
data = {}
for signal in message.signals:
    # Generate a random value within the signal's range
    random_value = random.randrange(signal.minimum, signal.maximum)
    data[signal.name] = random_value

# Encode the data into a CAN frame
encoded_message = message.encode(data)

# Setup CAN interface (e.g., socketcan)
can_interface = 'vcan0'  # Replace with your actual interface name
with can.interface.Bus(can_interface, bustype='socketcan') as bus:
    # Send the message
    #bus.send(encoded_message)
    bus.send(can.Message(arbitration_id=message.frame_id, data=encoded_message, is_extended_id=False))

    # Print a confirmation message
    print(f'Sent message {message_name} with random data: {data}')


