class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius


    @property
    def celsius(self):
        return self._celsius

    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:  
            raise ValueError("Temperature cannot be below -273.15°C")
        self._celsius = value

    
    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9



temp = Temperature(25)  


print(f"Temperature in Celsius: {temp.celsius}°C")
print(f"Temperature in Fahrenheit: {temp.fahrenheit}°F")


temp.fahrenheit = 98.6
print("\nAfter setting Fahrenheit to 98.6°F:")
print(f"Temperature in Celsius: {temp.celsius}°C")
print(f"Temperature in Fahrenheit: {temp.fahrenheit}°F")


try:
    temp.celsius = -300
except ValueError as e:
    print(f"\nError: {e}")
