#Takes user input for current and determines the direction of current flow in the circuit.
current = int(input("Enter current in amperes: "))
if current >0:
    print("Current flows from A to B")
elif current <0:
    print("Current flows from B to A")
else:
    print("No current flows")
    