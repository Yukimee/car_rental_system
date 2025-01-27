# Define a class
class Car:
    # Constructor to initialize the car object
    def __init__(self, color, model, engine_type):
        # Attributes
        self.color = color
        self.model = model
        self.engine_type = engine_type

    # Method to start the car
    def start(self):
        print(f"The {self.model} car with a {self.engine_type} engine is starting.")

    # Method to stop the car
    def stop(self):
        print(f"The {self.model} car is stopping.")

    # Method to accelerate the car
    def accelerate(self):
        print(f"The {self.model} car is accelerating.")

# Create objects (instances) of the Car class
my_car = Car("Red", "Toyota Corolla", "Petrol")
your_car = Car("Blue", "Honda Civic", "Diesel")

# Call methods on the objects
my_car.start()        # Output: The Toyota Corolla car with a Petrol engine is starting.
my_car.accelerate()   # Output: The Toyota Corolla car is accelerating.
your_car.stop()       # Output: The Honda Civic car is stopping.


