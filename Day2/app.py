def parseInputLine(in_line):
    out = {}
    in_line = in_line.split(" ")
    out["min"] = int(in_line[0].split("-")[0])
    out["max"] = int(in_line[0].split("-")[1])
    out["char"] = in_line[1].replace(':', '')
    out["pass"] = in_line[2]
    return out


def parse_pw_data(filename):
    with open(filename, 'r') as file:
        return [parseInputLine(line) for line in file]


def part_one(in_d):
    c = 0
    for char in in_d["pass"]:
        if char == in_d["char"]:
            c += 1
            if c > in_d["max"]:
                return False
    return True if c >= in_d["min"] else False


def part_two(in_d):
    o = 1  # Toboggan Corporate Policies have no concept of "index zero"!
    return True if (in_d["pass"][in_d["min"]-o] == in_d["char"]) is not (in_d["pass"][in_d["max"]-o] == in_d["char"]) else False


input_data = parse_pw_data('input.txt')
p1_c = 0
p2_c = 0

for in_d in input_data:
    p1_c += 1 if part_one(in_d) else 0
    p2_c += 1 if part_two(in_d) else 0
print("Part1: ", p1_c, " - Part2: ", p2_c)
