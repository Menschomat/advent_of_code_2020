target = 2020


def parseNumList(filename):
    with open(filename, 'r') as file:
        return [int(line) for line in file]


input_data = parseNumList('input.txt')


def part_one(input, target):
    for n in input:
        if (target - n) in input:  # If 2020 minus $number is in the input, we found the missing part
            return n*(target-n)


def part_two(input, target):
    for n in input:
        b = part_one(input, target - n)
        if b:
            return n*b


print("Part 1: ", part_one(input_data, target))
print("Part 2: ", part_two(input_data, target))
