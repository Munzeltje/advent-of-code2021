with open("../input.txt") as file:
    fish_population = [int(fish) for fish in file.readline().split(",")]

for i in range(80):
    new_fish = [8 for fish in fish_population if fish == 0]
    fish_population = [fish - 1 if fish > 0 else 6 for fish in fish_population]
    fish_population.extend(new_fish)
print(len(fish_population))
