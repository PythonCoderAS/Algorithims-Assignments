speed_limits = []
journey_speed = []

with open("speeding.in", "r") as f:
    n, m = [int(num) for num in f.readline().strip().split(" ")]
    for i in range(n):
        speed_limits.append([int(num) for num in f.readline().strip().split(" ")])
    for i in range(m):
        journey_speed.append([int(num) for num in f.readline().strip().split(" ")])

limits = [0]
for num, limit in speed_limits:
    limits.extend([limit] * num)

journey = [0]
for num, limit in journey_speed:
    journey.extend([limit] * num)

with open("speeding.out", "w") as f:
    f.write(str(max(b-a for a, b in zip(limits, journey))) + "\n")
