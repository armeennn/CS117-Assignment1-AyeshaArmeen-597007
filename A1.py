#Takes user input for voltage and resistance, calculates current, and checks if the circuit is safe or if the fuse will blow.

voltage = int(input('Enter voltage: '))
resistance = int(input('Enter resistance: '))

if resistance <= 0:
    print('Invalid resistance value')
else:
    current = voltage / resistance
    if current > 2:
        print('Fuse will blow')
    else:
        print('Circuit is safe')
