import can
import cantools

# Configure CAN interface
can_interface = 'vcan0'
bus = can.interface.Bus(can_interface, bustype='socketcan')

# Load DBC file
dbc_path = '../database/Main_2023.dbc'
db = cantools.database.load_file(dbc_path)

# Read and decode CAN message
message = bus.recv()  # Wait for a message
decoded_message = db.decode_message(message.arbitration_id, message.data)
print(f"Decoded message: {decoded_message}")
