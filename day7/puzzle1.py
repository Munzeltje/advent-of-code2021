import numpy as np


with open("../input.txt") as file:
    crabs = np.array([int(crab) for crab in file.readline().split(",")], dtype=np.int64)

positions_to_check = np.max(crabs) + 1  # 0-based
fuel_needed = np.zeros((positions_to_check,), dtype=np.int64)
for position in range(positions_to_check):
    fuel_cost_position = np.absolute(crabs - position)
    fuel_needed[position] = np.sum(fuel_cost_position)
print(np.min(fuel_needed))
