#Takes user input for voltage and resistance and calculate current for a range of voltages from 1 to 10 volts

resistance = 10
for voltage in range (1,11):
    current = voltage/resistance
    print(f"Voltage: {voltage} V, Current: {current} A")