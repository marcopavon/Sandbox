import bluetooth
import time

# Set the target Raspberry Pi's Bluetooth address
target_address = "D8:3A:DD:1D:B7:3F"  # Replace with the actual address of the receiver Raspberry Pi

# Set the Bluetooth service UUID (should be the same as in the receiver script)
service_uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

try:

    while True:
        # Establish a Bluetooth connection
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((target_address, 1))

        # Send the service UUID first
        sock.send(service_uuid.encode())

        # Send the message
        message = f"Hello from sender - {time.time()}"
        sock.send(message.encode())

        # Close the connection
        sock.close()

        print(f"Message sent successfully. Data sent at {time.ctime()}")

        time.sleep(3)
    
    else:
        print("stopped working")

except Exception as e:
    print("Error:", e)
