#Takes user input for two bits and performs a logical AND, OR and, XOR operation on them.

bit_1 = int(input("Enter the first bit (0 or 1): "))
bit_2 = int(input("Enter the second bit (0 or 1): "))
if bit_1 not in [0, 1] or bit_2 not in [0, 1]:
    print('Bits must be 0 or 1')
elif bit_1 == 1 and bit_2== 1:
    print('AND = 1')
    print('OR = 1')
    print('XOR = 0')
elif bit_1 == 0 and bit_2== 0:
    print('AND = 0')
    print('OR = 0')
    print('XOR = 0')
else:
    print('AND = 0')
    print('OR = 1')
    print('XOR = 1')

