from functools import reduce
filepath = 'input.txt'
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

with open(filepath, 'r') as file:
    work_map = [list(line.replace("\n", "")) for line in file]


def expand_map(in_map):
    return [x + x for x in in_map]


def get_count_for_slope(slope, w_map):
    c = 0
    pos = (0, 0)
    while pos[1] < len(w_map)-1:
        pos = tuple(map(sum, zip(pos, slope)))
        if len(w_map[0]) <= pos[0]:
            w_map = expand_map(w_map)
        if w_map[pos[1]][pos[0]] is "#":
            c += 1
    return c


def part_one(slope, w_map):
    return get_count_for_slope(slope, w_map)


def part_two(slopes, w_map):
    return reduce(lambda x, y: x*y, [get_count_for_slope(s, w_map) for s in slopes])


print('Part1: ', part_one((3, 1), work_map), ' - Part2: ', part_two(slopes, work_map))
