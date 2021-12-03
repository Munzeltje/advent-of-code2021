import numpy as np

with open("../input.txt") as file:
    diagnostic = np.vstack(
        [
            np.fromstring(string.strip().replace("", " "), dtype=int, sep=" ")
            for string in file.readlines()
            if string != "\n"
        ]
    )

gamma = []
epsilon = []
columns = diagnostic.shape[1]
for i in range(columns):
    most_freq = np.bincount(diagnostic[:, i]).argmax()
    least_freq = np.bincount(diagnostic[:, i]).argmin()
    gamma.append(most_freq)
    epsilon.append(least_freq)

gamma = int("".join(map(str, gamma)), 2)
epsilon = int("".join(map(str, epsilon)), 2)

print(gamma * epsilon)
