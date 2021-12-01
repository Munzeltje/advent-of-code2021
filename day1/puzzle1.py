with open("../input.txt") as file:
    depth_measurements = [
        int(x.replace("\n", "")) for x in file.readlines() if not x == "\n"
    ]

increase_counter = 0
prev_measurement = depth_measurements[0]
for measurement in depth_measurements[1:]:
    if measurement > prev_measurement:
        increase_counter += 1
    prev_measurement = measurement

print(increase_counter)
