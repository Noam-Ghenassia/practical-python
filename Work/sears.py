bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
sears_height = 442 # Height (meters)
num_bills = 1
day = 1

while bill_thickness * num_bills < sears_height :
    day += 1
    num_bills *= 2

print(day)