def main():
    print("(Thanks You)")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':

    print("This program converts Fahrenheit to Celsius.")
    degrees_fahrenheit: str = input("Enter temperature in Fahrenheit: ")
    degrees_fahrenheit: float = float(degrees_fahrenheit)
    degrees_celsius: float = (degrees_fahrenheit - 32) * 5.0 / 9.0
    print("Temperature: " + str(degrees_fahrenheit) + "F = " + str(degrees_celsius) + "C")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
