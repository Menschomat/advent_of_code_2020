import re

to_check = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]  # cid is optional
with open('input.txt') as file:
    passports = [{item.split(":")[0]:item.split(":")[1] for item in x.replace(
        "\n", " ").split(" ") if len(item.split(":")) > 1} for x in file.read().split("\n\n")]


def is_digit_in_range(in_str, span):
    return True if in_str.isdigit() and span[0] <= int(in_str) <= span[1] else False

def is_digit_with_len(in_str, t_len):
    return True if len(in_str) is t_len and in_str.isdigit() else False

def check_pass_for_hgt(passport):
    if re.compile(r'^\d{3}cm$').match(passport['hgt']):
        return True if 150 <= int(passport['hgt'].replace("cm", "")) <= 193 else False
    elif re.compile(r'^\d{2,3}in$').match(passport['hgt']):
        return True if 59 <= int(passport['hgt'].replace("in", "")) <= 76 else False
    return False

def check_pass_for_hcl(passport):
    return True if re.compile(r'^#\w{6}$').match(passport['hcl']) else False

def check_pass_for_ecl(passport):
    check_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return True if passport['ecl'] in check_list else False

def check_pass(passport, to_check):
    return True if all(elem in passport.keys() for elem in to_check) \
        and is_digit_in_range(passport['byr'], (1920, 2002)) \
        and is_digit_in_range(passport['iyr'], (2010, 2020)) \
        and is_digit_in_range(passport['eyr'], (2020, 2030)) \
        and is_digit_with_len(passport['pid'], 9)  \
        and check_pass_for_ecl(passport) \
        and check_pass_for_hcl(passport) \
        and check_pass_for_hgt(passport) else False

prat_one = len(list(filter(lambda d: all(elem in d.keys() for elem in to_check), passports)))
prat_two = len(list(filter(lambda d: check_pass(d, to_check), passports)))
print("Part1: ", prat_one, " - Part2: ", prat_two)
