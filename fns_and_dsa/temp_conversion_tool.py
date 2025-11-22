FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return round(celsius, 2)

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return round(fahrenheit, 2)

def main():
    print("Temperature Conversion Tool")
    choice = input("Convert to (C)elsius or (F)ahrenheit? ").strip().upper()

    if choice == 'C':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = convert_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is {celsius}°C")
    elif choice == 'F':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = convert_to_fahrenheit(celsius)
        print(f"{celsius}°C is {fahrenheit}°F")
    else:
        print("Invalid choice. Please select 'C' or 'F'.")

if __name__ == "__main__":
    main()