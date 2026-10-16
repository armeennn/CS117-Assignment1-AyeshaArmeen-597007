#Takes user input for resistor band colour code and outputs the corresponding digit value.

resistor_colour = input('Enter resistor band colour code: ').lower()
if resistor_colour == 'black':
    print('Digit = 0')
elif resistor_colour == 'brown':
    print('Digit = 1')
elif resistor_colour == 'red':
    print('Digit = 2')
elif resistor_colour == 'orange':
    print('Digit = 3')
elif resistor_colour == 'yellow':
    print('Digit = 4')
elif resistor_colour == 'green':
    print('Digit = 5')
elif resistor_colour == 'blue':
    print('Digit = 6')
elif resistor_colour == 'violet':
    print('Digit = 7')
elif resistor_colour == 'grey':
    print('Digit = 8')
elif resistor_colour == 'white':
    print('Digit = 9')
else:
    print('Invalid colour')