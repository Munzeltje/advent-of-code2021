import numpy as np

with open("../input.txt") as file:
    diagnostic = np.vstack(
        [
            np.fromstring(string.strip().replace("", " "), dtype=int, sep=" ")
            for string in file.readlines()
            if string != "\n"
        ]
    )


def find_rating(diagnostic, rating_type):
    columns = diagnostic.shape[1]
    rating_values = np.copy(diagnostic)
    for i in range(columns):
        frequencies = np.bincount(rating_values[:, i])
        if frequencies[0] == frequencies[1]:
            rating_values = rating_values[np.where(rating_values[:, i] == rating_type)]
        else:
            if rating_type == CO2_SCRUBBER:
                rating_values = rating_values[
                    np.where(rating_values[:, i] == frequencies.argmin())
                ]
            elif rating_type == OXYGEN_GENERATOR:
                rating_values = rating_values[
                    np.where(rating_values[:, i] == frequencies.argmax())
                ]
        if rating_values.shape[0] == 1:
            break
    return rating_values


OXYGEN_GENERATOR = 1
CO2_SCRUBBER = 0
OXYGEN_GENERATOR_RATING = int(
    "".join(map(str, find_rating(diagnostic, OXYGEN_GENERATOR)[0])), 2
)
CO2_SCRUBBER_RATING = int(
    "".join(map(str, find_rating(diagnostic, CO2_SCRUBBER)[0])), 2
)
print(OXYGEN_GENERATOR_RATING * CO2_SCRUBBER_RATING)
