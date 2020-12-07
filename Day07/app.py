import re

def parse_input_line(in_str):
    def parse_contain(contain_str):
        regex = r"(\d)\s(\w*\s\w*)\D*"
        return {x[1]: int(x[0]) for x in re.findall(regex, contain_str)}

    regex = r"^(.*) bags contain (.*)."
    return re.search(regex, in_str).group(1), parse_contain(re.search(regex, in_str).group(2))

def part_one(in_dict, search_str):
    out_set = set()
    for bag, colors in rule_dict.items():
        if search_str in colors:
            out_set.add(bag)
            out_set.update(part_one(in_dict, bag))
    return out_set

def part_two(in_dict, search_str):
    sum = 0
    for k, v in in_dict[search_str].items():
        sum += v + part_two(in_dict, k)*v
    return sum

with open('input.txt') as file:
    rule_dict = {k: v for k, v in (parse_input_line(line) for line in file)}

print('Part1: ', len(part_one(rule_dict, 'shiny gold')),
      ' - Part2: ', part_two(rule_dict, 'shiny gold'))
