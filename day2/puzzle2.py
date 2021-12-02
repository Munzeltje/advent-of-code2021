with open("../input.txt") as file:
    planned_course = [
        (x.replace("\n", "").split()[0], int(x.replace("\n", "").split()[1]))
        for x in file.readlines()
        if not x == "\n"
    ]

horizontal_pos = 0
depth = 0
aim = 0

for direction, magnitude in planned_course:
    if direction == "forward":
        horizontal_pos += magnitude
        depth += magnitude * aim
    elif direction == "up":
        aim -= magnitude
    elif direction == "down":
        aim += magnitude

print(horizontal_pos * depth)
