class Device:
    def __init__(self, device_id, location, status, firmware):
        self.id = device_id
        self.location = location
        self.status = status
        self.firmware = firmware

    def get_device_info(self):
        print(f'''DEVICE INFO:
            ID: {self.id}
            Location: {self.location}
            Status: {'Online' if self.status else 'Offline'}
            FW: {self.firmware}
        ''')


device1 = Device(1, 'Kothrud, Pune', True, 'X24311003')
device1.get_device_info()

# there are no true private variables in Python. Instead, programmers use _<var_name> to indicate it as a private variable
