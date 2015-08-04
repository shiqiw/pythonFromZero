class Vehicle(object):
    # object is base class, in Python 3 can escape this and write as
    # class Vehivle:
    """
    Create a vehicle
    """

    def __init__(self, color, doors, tires):
        """Constructor"""
        # pass
        self.color = color
        self.doors = doors
        self.tires = tires

    def brake(self):
        """
        Stop the car
        """
        print(self.tires)
        return "Braking"

    def drive(self):
        """
        Drive the car
        """
        return "I'm driving"

class Car(Vehicle):
    """
    The Car class
    """
    
    def brake(self):
        """
        Override brake
        """
        return "The car is braking slowly"


if __name__ == '__main__':
    # double underscores, name of the script
    # if you run the script directly, name is main
    # if the statement is true, everything underneath is going to run
    car = Car('blue', 2, 4)
    truck = Vehicle('red', 5, 6)

    print(car.brake())

    # the self argument refers to whatever instance it is 
