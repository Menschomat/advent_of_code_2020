from functools import reduce

def part_one(str_list):
  return len(reduce(set.union, str_list))

def part_two(set_list):
  return len(reduce(set.intersection, set_list))
  
with open('input.txt') as file:
  p1_c = 0
  p2_c = 0
  parsed_input = [[set(x) for x in line.split('\n')] for line in file.read().split("\n\n")]
  for decl in parsed_input:
    p1_c += part_one(decl)
    p2_c += part_two(decl)
    
print('Part1: ', p1_c, ' - Part2: ', p2_c)