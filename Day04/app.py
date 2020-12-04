import re

to_check = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]  # cid is optional
with open('input.txt') as file:
    passports = [{item.split(":")[0]:item.split(":")[1] for item in x.replace(
        "\n", " ").split(" ") if len(item.split(":")) > 1} for x in file.read().split("\n\n")]

def str_dig_len_check(t_len, in_str):
    return True if len(in_str) is t_len and in_str.isdigit() else False

def check_pass_for_byr(passport):
    return True if str_dig_len_check(4, passport['byr']) and 1920 <= int(passport['byr']) <= 2002 else False

def check_pass_for_iyr(passport):
    return True if str_dig_len_check(4, passport['iyr']) and 2010 <= int(passport['iyr']) <= 2020 else False

def check_pass_for_eyr(passport):
    return True if str_dig_len_check(4, passport['eyr']) and 2020 <= int(passport['eyr']) <= 2030 else False

def check_pass_for_hgt(passport):
    if re.compile(r'^\w*cm$').match(passport['hgt']):
        return True if 150 <= int(passport['hgt'].replace("cm", "")) <= 193 else False
    elif re.compile(r'^\w*in$').match(passport['hgt']):
        return True if 59 <= int(passport['hgt'].replace("in", "")) <= 76 else False
    return False

def check_pass_for_hcl(passport):
    return True if re.compile(r'^#\w\w\w\w\w\w$').match(passport['hcl']) else False

def check_pass_for_ecl(passport):
    check_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return True if passport['ecl'] in check_list else False

def check_pass_for_pid(passport):
    return True if str_dig_len_check(9, passport['pid']) else False

def check_pass(passport, to_check):
    return True if all(elem in passport.keys() for elem in to_check) \
        and check_pass_for_byr(passport) \
        and check_pass_for_iyr(passport) \
        and check_pass_for_eyr(passport) \
        and check_pass_for_pid(passport) \
        and check_pass_for_ecl(passport) \
        and check_pass_for_hcl(passport) \
        and check_pass_for_hgt(passport) else False

prat_one = len(list(filter(lambda d: all(elem in d.keys() for elem in to_check), passports)))
prat_two = len(list(filter(lambda d: check_pass(d, to_check), passports)))
print("Part1: ", prat_one, " - Part2: ", prat_two)
