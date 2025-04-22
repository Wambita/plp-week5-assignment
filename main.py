# Base class for the Smartphone example
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    def call(self, number):
        return f"Calling {number} from {self.brand} {self.model}."

    def text(self, number, message):
        return f"Sending text to {number}: {message}"

    def show_specs(self):
        return f"{self.brand} {self.model} - {self.storage}GB Storage, {self.battery_life} hours battery life."


# Inherited class to demonstrate polymorphism and encapsulation
class Touchscreen(Smartphone):
    def __init__(self, brand, model, storage, battery_life, screen_size):
        super().__init__(brand, model, storage, battery_life)
        self.screen_size = screen_size

    def touch_action(self):
        return f"Touching the {self.screen_size}-inch screen."

    def show_specs(self):
        original_specs = super().show_specs()
        return f"{original_specs}, {self.screen_size}-inch Touchscreen."


# Base class for the Polymorphism challenge
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Derived class Car
class Car(Vehicle):
    def move(self):
        return "Driving"


# Derived class Plane
class Plane(Vehicle):
    def move(self):
        return "Flying"


# Derived class Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing"


# Main program to test both the Smartphone and Polymorphism example
def main():
    # Smartphone example
    smartphone = Smartphone("Apple", "iPhone 14", 128, 20)
    touchscreen_phone = Touchscreen("Samsung", "Galaxy S22", 256, 25, 6.1)

    print(smartphone.call("123-456-7890"))
    print(touchscreen_phone.touch_action())
    print(touchscreen_phone.show_specs())

    # Polymorphism example
    vehicles = [Car(), Plane(), Boat()]
    print("\nVehicles Moving:")
    for vehicle in vehicles:
        print(vehicle.move())


if __name__ == "__main__":
    main()
