#Takes resistance readings and sorts them by tolerance
one_percent = 0
five_percent = 0
reject = 0

resistance = float(input('Enter a resistance (0 to quit): '))
while resistance != 0:
    if resistance >= 99.0 and resistance <= 101.0:
        one_percent += 1
    elif resistance >= 95.0 and resistance <= 105.0:
        five_percent += 1
    else:
        reject += 1 
    resistance = float(input('Enter a resistance (0 to quit): '))
print('1% tolerance:',one_percent)
print('5% tolerance:',five_percent)
print('Rejected:',reject)