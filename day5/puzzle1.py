from collections import Counter

import numpy as np


def read_input(file):
    regex = r"(\d+),(\d+) -> (\d+),(\d+)"
    lines = np.fromregex(file, regex, np.int64)
    lines = np.reshape(lines, (lines.shape[0], 2, 2))
    return lines


def find_points_covered(lines):
    points_covered = []
    for line in lines:
        if line[:, 0][0] == line[:, 0][1]:
            start_line = np.min(line[:, 1])
            end_line = np.max(line[:, 1])
            x_coor = line[:, 0][0]
            y_coors = range(start_line, end_line + 1)
            points_covered.extend([(x_coor, y_coor) for y_coor in y_coors])
        elif line[:, 1][0] == line[:, 1][1]:
            start_line = np.min(line[:, 0])
            end_line = np.max(line[:, 0])
            y_coor = line[:, 1][0]
            x_coors = range(start_line, end_line + 1)
            points_covered.extend([(x_coor, y_coor) for x_coor in x_coors])
    return points_covered


def main():
    lines = read_input("../input.txt")
    points_covered = find_points_covered(lines)
    cnt = Counter(points_covered)
    print(len([k for k, v in cnt.items() if v > 1]))


if __name__ == "__main__":
    main()
