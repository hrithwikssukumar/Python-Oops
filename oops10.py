class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    # Getter for Celsius
    @property
    def celsius(self):
        return self._celsius

    # Setter for Celsius
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:  # Absolute zero check
            raise ValueError("Temperature cannot be below -273.15°C")
        self._celsius = value

    # Fahrenheit as a calculated property
    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    # Setter for Fahrenheit
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9


# Example usage
temp = Temperature(25)  # Initialize with 25°C

# Access Fahrenheit
print(f"Temperature in Celsius: {temp.celsius}°C")
print(f"Temperature in Fahrenheit: {temp.fahrenheit}°F")

# Update Fahrenheit
temp.fahrenheit = 98.6
print("\nAfter setting Fahrenheit to 98.6°F:")
print(f"Temperature in Celsius: {temp.celsius}°C")
print(f"Temperature in Fahrenheit: {temp.fahrenheit}°F")

# Try setting a very low Celsius value
try:
    temp.celsius = -300
except ValueError as e:
    print(f"\nError: {e}")
