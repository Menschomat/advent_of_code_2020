def check_in_range(watch_list, val):
    for i in watch_list:
        if val-i in watch_list:
            return True

def find_wrong_number(in_data, back_look=25):
    for cursor in range(back_look, len(in_data)):
        if not check_in_range(in_data[cursor-back_look:cursor], in_data[cursor]):
            return in_data[cursor]

def find_encryption_weakness(in_data, invalid_val):
    for l in range(2, len(in_data)):
        for i in range(len(in_data)-l):
            if sum(in_data[i:i+l]) == invalid_val:
                return min(in_data[i:i+l]) + max(in_data[i:i+l])

with open('input.txt') as file:
    in_data = [int(i) for i in file]
    p1 = find_wrong_number(in_data)
    p2 = find_encryption_weakness(in_data, p1)
    print('Part1: ', p1, ' - Part2: ', p2)
