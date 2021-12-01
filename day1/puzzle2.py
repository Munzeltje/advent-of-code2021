import collections
from itertools import islice


def sliding_window(iterable, n):
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


with open("../input.txt") as file:
    depth_measurements = [
        int(x.replace("\n", "")) for x in file.readlines() if not x == "\n"
    ]

increase_counter = 0
windows = list(sliding_window(depth_measurements, 3))
prev_window = windows[0]
for window in windows[1:]:
    if sum(window) > sum(prev_window):
        increase_counter += 1
    prev_window = window

print(increase_counter)
