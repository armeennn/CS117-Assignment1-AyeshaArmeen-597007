#Takes user input for three resistors and outputs smallest and largest resistor values
r_1 = int(input("Enter the R1: "))
r_2 = int(input("Enter the R2: "))
r_3 = int(input("Enter the R3: "))
if r_1 >= r_2 and r_1 >= r_3:
    large = r_1
elif r_2 >= r_1 and r_2 >= r_3:
    large = r_2
else:
    large = r_3

if r_1 <= r_2 and r_1 <= r_3:
    small = r_1
elif r_2 <= r_1 and r_2 <= r_3:
    small = r_2
else:
    small = r_3

print(f'Smallest: {small} ohm')
print(f'Largest: {large} ohm')      