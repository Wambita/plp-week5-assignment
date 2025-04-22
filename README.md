# plp-week5-assignment

# Python Class Design and Polymorphism Challenge

## Overview

This project consists of two activities:

1. **Design Your Own Class**: Create a class representing a real-world object, adding attributes, methods, constructors, and inheritance. The example used here is a **Smartphone** class, with a derived **Touchscreen** class to demonstrate inheritance and polymorphism.
   
2. **Polymorphism Challenge**: Create a program with multiple vehicle classes (Car, Plane, Boat) that share the same method `move()`. Each class overrides `move()` to implement its own version of how it moves (Driving, Flying, or Sailing).

## Files

1. **`main.py`**: Contains the implementation of the Smartphone class, Touchscreen class, and the Vehicle polymorphism example. It includes the `main()` function, which runs both examples.
   
2. **`README.md`**: Provides an overview of the project, including details on the two activities, how to run the code, and what each part demonstrates.


### **How to Run the Code**

1. **Clone the Repository**: If you're using Git, you can clone this repository to your local machine:

   ```bash
   git clone https://github.com/Wambita/plp-week5-assignment.git
   ```

2. **Run the Program**: Navigate to the directory containing `main.py` and run the Python file:

   ```bash
   python main.py
   ```

### Explanation of Code

#### Smartphone Class and Inheritance

- The `Smartphone` class represents a basic smartphone with attributes like `brand`, `model`, `storage`, and `battery_life`. It includes methods for making calls and sending texts.
- The `Touchscreen` class inherits from `Smartphone` and adds a `screen_size` attribute. It also overrides the `show_specs()` method to include the touchscreen size.

#### Polymorphism Challenge

- The `Vehicle` class defines a `move()` method, which is then overridden in three derived classes: `Car`, `Plane`, and `Boat`. Each class has its own version of `move()`, demonstrating polymorphism.

### Example Output

When running `main.py`, the output will look like this:

```
Calling 123-456-7890 from Apple iPhone 14.
Touching the 6.1-inch screen.
Apple iPhone 14 - 128GB Storage, 20 hours battery life., 6.1-inch Touchscreen.

Vehicles Moving:
Driving
Flying
Sailing
```

## Contributing

Feel free to contribute by submitting issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
