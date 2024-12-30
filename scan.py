import bluetooth

def scan():
    print("start scanning...")
    devices = bluetooth.discover_devices(lookup_names=True, lookup_class= True)
    number_of_devices = len(devices)
    print(number_of_devices, " devices found")
    for addr, name, device_class in devices:
        print("Device")
        print(f"Device name: {name}")
        print(f"Device MAC Adress: {addr}")      
        print(f"Device Class: {device_class}")
        print("\n")
    return

scan()