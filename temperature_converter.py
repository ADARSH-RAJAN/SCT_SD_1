# Temperature Converter

print("===== Temperature Converter =====")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")

choice = int(input("Enter the unit of the given temperature (1-3): "))
temp = float(input("Enter the temperature value: "))

print("\nConvert to:")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")

convert = int(input("Enter your choice (1-3): "))

if choice == convert:
    print("Converted Temperature =", temp)

elif choice == 1:  # Celsius
    if convert == 2:
        result = (temp * 9/5) + 32
        print("Temperature in Fahrenheit =", result)
    elif convert == 3:
        result = temp + 273.15
        print("Temperature in Kelvin =", result)
    else:
        print("Invalid Choice")

elif choice == 2:  # Fahrenheit
    if convert == 1:
        result = (temp - 32) * 5/9
        print("Temperature in Celsius =", result)
    elif convert == 3:
        result = ((temp - 32) * 5/9) + 273.15
        print("Temperature in Kelvin =", result)
    else:
        print("Invalid Choice")

elif choice == 3:  # Kelvin
    if convert == 1:
        result = temp - 273.15
        print("Temperature in Celsius =", result)
    elif convert == 2:
        result = ((temp - 273.15) * 9/5) + 32
        print("Temperature in Fahrenheit =", result)
    else:
        print("Invalid Choice")

else:
    print("Invalid Input")