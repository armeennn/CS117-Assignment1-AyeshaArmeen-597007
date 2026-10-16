#The function takes values of resistors in a parallel combination and outputs the equivalent resistance

def parallel_resistance(resistors):
    total = 0
    for i in resistors:
        total = total + (1/i)
    equivalent = 1/total  
    return equivalent  

result1 = parallel_resistance([10, 10])
result2 = parallel_resistance([100, 200, 300])

print(result1)
print(round(result2,2))