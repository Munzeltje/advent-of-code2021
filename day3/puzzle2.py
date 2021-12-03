import numpy as np

with open("../input.txt") as file:
    diagnostic = np.vstack(
        [
            np.fromstring(string.strip().replace("", " "), dtype=int, sep=" ")
            for string in file.readlines()
            if string != "\n"
        ]
    )

columns = diagnostic.shape[1]

oxygen_generator = np.copy(diagnostic)
for i in range(columns):
    frequencies = np.bincount(oxygen_generator[:, i])
    if frequencies[0] == frequencies[1]:
        oxygen_generator = oxygen_generator[np.where(oxygen_generator[:, i] == 1)]
    else:
        oxygen_generator = oxygen_generator[
            np.where(oxygen_generator[:, i] == frequencies.argmax())
        ]
    if oxygen_generator.shape[0] == 1:
        break

co2_scrubber = np.copy(diagnostic)
for i in range(columns):
    frequencies = np.bincount(co2_scrubber[:, i])
    if frequencies[0] == frequencies[1]:
        co2_scrubber = co2_scrubber[np.where(co2_scrubber[:, i] == 0)]
    else:
        co2_scrubber = co2_scrubber[
            np.where(co2_scrubber[:, i] == frequencies.argmin())
        ]
    if co2_scrubber.shape[0] == 1:
        break

OXYGEN_GENERATOR_RATING = int("".join(map(str, oxygen_generator[0])), 2)
CO2_SCRUBBER_RATING = int("".join(map(str, co2_scrubber[0])), 2)
print(OXYGEN_GENERATOR_RATING * CO2_SCRUBBER_RATING)
