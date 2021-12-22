positions = []
with open("cowjog.in", "r") as file:
    n = int(file.readline().strip())
    for line in file:
        x, y = line.strip().split(" ")
        positions.append((int(x), int(y)))

groups = 1
cur_speed = positions[-1][1]
for pos, speed in reversed(positions[:-1]):
    if speed <= cur_speed:
        groups += 1
        cur_speed = speed

with open("cowjog.out", "w") as file:
    file.write(str(groups) + "\n")
