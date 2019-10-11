class Vehicle(object):
    
    def __init__(self, doors, tires, color, fuelType, vehicleType):
        self.doors = doors
        self.tires = tires
        self.color = color
        self.fuelType = fuelType
        self.vehicleType = vehicleType
    
    def fuel(self, isfuel=True):
        return 'Full Fuel' if isfuel else 'No Fuel'
    
    def door(self, isopen=False):
        return 'Open' if isopen else 'Close'
    
    def brake(self, isbrake=True):
        if isbrake:
            return 'Brake a %s %s' % (self.color, self.vehicleType)
        else:
            return 'Drive a %s %s' % (self.color, self.vehicleType)

    def drive(self, isdrive=False):
        if isdrive:
            return 'Drive a %s %s' % (self.color, self.vehicleType)
        else:
            return 'Brake a %s %s' % (self.color, self.vehicleType)


class Car(Vehicle):
    
    def set(self, doors, tires, color, fuelType, vehicleType):
        self.doors = doors
        self.tires = tires
        self.color = color
        self.fuelType = fuelType
        self.vehicleType = vehicleType


class Truck(Vehicle):
    
    def set(self, doors, tires, color, fuelType, vehicleType, hindcarriage):
        self.doors = doors
        self.tires = tires
        self.color = color
        self.fuelType = fuelType
        self.vehicleType = vehicleType
        self.hindcarriage = hindcarriage
    

car = Car(5, 4, 'red', 'benzine', 'car')
print(car.doors, car.tires, car.color, car.fuelType, car.vehicleType)

truck = Truck(2, 6, 'blue', 'diesel', 'truck')
print(truck.doors, truck.tires, truck.color, truck.fuelType, truck.vehicleType)

print(car.brake())
print(car.brake(False))

print(truck.drive())
print(truck.drive(True))

print('Car fuel: ', car.fuel())
print('Car fuel: ', car.fuel(False))

print('Truck fuel: ', truck.fuel())
print('Truck fuel: ', truck.fuel(False))


print('Car door:', car.door())
print('Car door:', car.door(True))

print('Truck door:', truck.door())
print('Truck door:', truck.door(True))

car.set(5, 4, 'red', 'benzine', 'car')
print('Doors:', car.doors, ', tires:', car.tires, ', color:', car.color, ', type fuel:', car.fuelType,
      ', type vehicle:', car.vehicleType)

truck.set(2, 6, 'black', 'diesel', 'truck', True)
print('Doors:', truck.doors, ', tires:', truck.tires, ', color:', truck.color, ', type fuel:', truck.fuelType,
      ', type vehicle:', truck.vehicleType, ', hindcarriage:', truck.hindcarriage)
