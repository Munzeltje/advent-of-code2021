import numpy as np

with open("../input.txt") as file:
    fish_population = [int(fish) for fish in file.readline().split(",")]

number_of_fish = np.zeros((9,), dtype=np.int64)
for fish in fish_population:
    number_of_fish[fish] += 1

transition_matrix = np.array(
    [
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
    ],
    dtype=np.int64,
)


for _ in range(256):
    number_of_fish = np.matmul(transition_matrix, number_of_fish)
print(sum(number_of_fish))
