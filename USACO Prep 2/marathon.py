def get_distance(coords1, coords2):
    """Gets the distance between 2 pairs of coordinates

    Args:
        coords1 ([int, int]): The first set of coordinates
        coords2 ([int, int]): The second set of coordinates
    """
    return abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1])


coordinates = []
with open("marathon.in", "r") as file:
    n = int(file.readline().strip())
    for line in file:
        x, y = line.strip().split(" ")
        coordinates.append((int(x), int(y)))

distance_pairs = {}

for i in range(n - 1):
    start = coordinates[i]
    finish = coordinates[i + 1]
    distance = get_distance(start, finish)
    distance_pairs[start, finish] = distance

distance_pairs_list = list(distance_pairs.items())
normal_max = sum([distance for _, distance in distance_pairs_list])
possible_values = distance_pairs_list[:-1]
possible_sums = []
for combo in range(len(possible_values)):
    current_sum = normal_max
    actual_index = combo
    removed_coordinate_set = distance_pairs_list[actual_index]
    modified_coordinate_set = distance_pairs_list[actual_index + 1]
    current_sum -= (removed_coordinate_set[1] + modified_coordinate_set[1])
    # removed_coordinate_set[0][1] is the coordinate pair that was removed, and is equal
    # to modified_coordinate_set[0][0]. We need to add the distance between the new
    # coordinate pairs.
    current_sum += get_distance(removed_coordinate_set[0][0], modified_coordinate_set[0][1])
    possible_sums.append(current_sum)

with open("marathon.out", "w") as file:
    file.write(str(min(possible_sums)) + "\n")
