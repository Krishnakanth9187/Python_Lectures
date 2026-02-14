class Light:
    def operate(self):
        print("normal light")

class Fan:
    def operate(self):
        pass

class EcoLight(Light):
    def operate(self):
        print("Eco Light Running")

class PerformanceLight(Light):
    def operate(self):
        print("Performance Light Running")

class DeviceFactory:
    def create_light(self):
        return Light()
    def create_fan(self):
        return Fan()

# inheritance enforces methods and attributes

class EcoFactory(DeviceFactory):
    def create_light(self):
        return EcoLight()
    
    def create_fan(self):
        return EcoFan()

class PerformanceFactory(DeviceFactory):
    def create_light(self):
        return PerformanceLight()
    
class HyperPerformanceFactory(DeviceFactory):
    def create_light(self):
        return PerformanceLight()
    


factory = PerformanceFactory()
light = factory.create_light()
light.operate()




class SmartHomeController:
    _instance = None

    # def __new__(cls):
    #     print("Creating new object")
    #     return super().__new__(cls)

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = SmartHomeController()
b = SmartHomeController()


print(a is b)  # True
