from collections import Counter

def part_one(adapters):
    adapters = [0]+adapters+[adapters[-1]+3]
    differeces = [adapters[i+1]-x for i,
                  x in enumerate(adapters) if i+1 < len(adapters)]
    return differeces.count(1)*differeces.count(3)

def part_two(jolts):
    jolts.append(jolts[-1] + 3)
    dp = Counter()
    dp[0] = 1
    for jolt in jolts:
        dp[jolt] = dp[jolt - 1] + dp[jolt - 2] + dp[jolt - 3]
    return dp[jolts[-1]]

with open('input.txt') as file:
    adapters = [int(i) for i in file]
    adapters.sort()
    print('Part1: ', part_one(adapters), ' - Part2: ', part_two(adapters))
