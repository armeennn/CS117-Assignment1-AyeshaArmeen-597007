#Defines 2 functions that calculates current using ohm's law and power dissipated 

def ohms_current(v, r):
    current = v/r
    return current

def power_dissipated(i, r):
    power = i**2 * r
    return power
current  = ohms_current(12,6)
power = power_dissipated(current,6) 
print(f'Current = {current} A')
print(f'Power = {power} W')