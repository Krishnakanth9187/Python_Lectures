class Light:
    def turn_on(self):
        print("Light ON")

class Fan:
    def turn_on(self):
        print("Fan ON")

class DeviceFactory:
    @staticmethod
    def create_device(device_type):
        if device_type == "light":
            return Light()
        elif device_type == "fan":
            return Fan()
        else:
            raise ValueError("Unknown device")

device = DeviceFactory.create_device("light")
device.turn_on()

device1 = DeviceFactory.create_device("fan")
device1.turn_on()


l = Light()
l1 = Light()
l.turn_on()

f = Fan()
f.turn_on()
