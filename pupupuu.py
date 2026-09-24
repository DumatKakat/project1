readings = [-1, -2, 3,]
for reading in readings:
    if reading < 0:
        readings.remove(reading)
print(readings)