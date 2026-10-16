#Defines a function that converts a user given positive decimal number to binary

def decimal_to_binary(n):
    binary = ""

    while n > 0:
        remainder = n%2
        binary = str(remainder) + binary
        n = n //2
    return binary

result1 = decimal_to_binary(10)
result2 = decimal_to_binary(25)

print(result1)
print(result2)
