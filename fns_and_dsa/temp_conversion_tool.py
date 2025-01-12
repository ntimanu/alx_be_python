# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt user for input
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Determine the conversion based on the unit
        if unit == "F":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        elif unit == "C":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
from datetime import datetime, timedelta

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def celsius_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date

def main():
    display_current_datetime()
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)

        temp = float(input("Enter a temperature in Fahrenheit: "))
        print(f"{temp}°F is {fahrenheit_to_celsius(temp):.2f}°C")
    except ValueError:
        print("Please enter valid inputs.")

if __name__ == "__main__":
    main()
