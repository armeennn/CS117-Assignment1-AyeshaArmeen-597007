#Takes user input for a number of resistance in series and calculates the total resistance of the circuit

i = int(input('How many resistors are in series? '))
total = 0
for i in range(1,i+1):
    resistance = int(input(f'Enter R{i}: '))
    total += resistance
print(f'Total resistance = {total} ohm')