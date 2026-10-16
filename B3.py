#Takes sensor readings and calculates the number of readings above 3.2V, highest, lowest and average readings

readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)
count = 0
sum_read = 0
lower = readings[0]
higher = readings[0]
for i in readings:
    sum_read += i
    if i > 3.2:
        count += 1

    if higher < i:
        higher = i
    if lower > i:
        lower = i
average = sum_read/len(readings)

print('Readings above 3.2 V:', count)
print('Highest:', higher, 'V')
print('Lowest:', lower, 'V')
print('Average:', average, 'V')
