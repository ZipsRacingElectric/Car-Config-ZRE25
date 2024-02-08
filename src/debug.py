import can
from canmatrix import canmatrix

# Load the dbc file
dbc_file = "../database/Main_2023.dbc"
matrix = canmatrix.load(dbc_file)

# Set up the CAN bus interface
bus = can.interface.Bus(channel='can0', bustype='socketcan')

# Read messages from can0
for msg in bus:
    # Check if the message ID is defined in the dbc file
    if msg.arbitration_id in matrix.messages:
        # Get the message object from the matrix
        message = matrix.messages[msg.arbitration_id]

        # Parse the message data using the dbc file
        signals = message.decode(msg.data)

        # Print the parsed signals
        for signal in signals:
            print(f"Signal: {signal.name}, Value: {signal.phys}")