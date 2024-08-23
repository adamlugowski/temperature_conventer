def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32


def temperature_converter():
    while True:
        try:
            temp = float(input('Temperature value to convert: '))
            break
        except ValueError:
            print('The temperature value should be integer or float')
    while True:
        try:
            unit = input('Unit of entered temperature (C/F/K/): ').upper()
            if unit not in ['C', 'F', 'K']:
                print('The unit should be C/F/K')
            else:
                break
        except ValueError:
            print('The unit should be C/F/K')
    while True:
        try:
            convert = input('Type the unit you want to convert to (C/F/K/): ').upper()
            if convert not in ['C', 'F', 'K']:
                print('The unit should be C/F/K')
            else:
                break
        except ValueError:
            print('The unit should be C/F/K')
    if unit == 'C' and convert == 'F':
        print(f'Result: {temp}°C is {celsius_to_fahrenheit(temp)}°F')
    elif unit == 'C' and convert == 'K':
        print(f'Result: {temp}°C is {celsius_to_kelvin(temp)}°K')
    elif unit == 'F' and convert == 'C':
        print(f'Result: {temp}°F is {fahrenheit_to_celsius(temp)}°C')
    elif unit == 'F' and convert == 'K':
        print(f'Result: {temp}°F is {fahrenheit_to_kelvin(temp)}°K')
    elif unit == 'K' and convert == 'C':
        print(f'Result: {temp}°K is {kelvin_to_celsius(temp)}°C')
    elif unit == 'K' and convert == 'F':
        print(f'Result: {temp}°K is {kelvin_to_fahrenheit(temp)}°F')


if __name__ == '__main__':
    temperature_converter()
