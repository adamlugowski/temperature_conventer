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

    if unit == convert:
        print(f'Result: {temp}°{unit} is the same as {temp}°{convert}')
    else:
        if unit == 'C' and convert == 'F':
            result = celsius_to_fahrenheit(temp)
        elif unit == 'C' and convert == 'K':
            result = celsius_to_kelvin(temp)
        elif unit == 'F' and convert == 'C':
            result = fahrenheit_to_celsius(temp)
        elif unit == 'F' and convert == 'K':
            result = fahrenheit_to_kelvin(temp)
        elif unit == 'K' and convert == 'C':
            result = kelvin_to_celsius(temp)
        elif unit == 'K' and convert == 'F':
            result = kelvin_to_fahrenheit(temp)

        print(f'Result: {temp}°{unit} is {result}°{convert}')


if __name__ == '__main__':
    temperature_converter()
