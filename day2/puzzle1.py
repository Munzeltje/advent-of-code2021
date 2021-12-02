with open("../input.txt") as file:
    planned_course = [
        (x.replace("\n", "").split()[0], int(x.replace("\n", "").split()[1]))
        for x in file.readlines()
        if not x == "\n"
    ]

horizontal_pos = 0
depth = 0
for direction, magnitude in planned_course:
    if direction == "forward":
        horizontal_pos += magnitude
    elif direction == "up":
        depth -= magnitude
    elif direction == "down":
        depth += magnitude

print(horizontal_pos * depth)
