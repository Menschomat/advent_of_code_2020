import decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

input_file = 'input.txt'
plane_col_max = 7
plane_row_max = 127


def to_int(in_num):
    return int(decimal.Decimal(in_num).to_integral_value())


def calc_pos(in_str, max_idx, up_c, down_c):
    span = (0, max_idx)
    for c in in_str:
        if c == up_c:
            span = (span[0]+to_int((span[1]-span[0])/2), span[1])
        elif c == down_c:
            span = (span[0], span[1]-to_int((span[1]-span[0])/2))
    return min(span)


def calc_id(row, col):
    return row*8+col


def part_one(file_path):
    with open(file_path) as file:
        return sorted([calc_id(calc_pos(f[:7], plane_row_max, 'B', 'F'), calc_pos(f[7:], plane_col_max, 'R', 'L')) for f in file])


def part_two(p1_out):
    compare = []
    compare.extend(range(100, 900))
    return list(sorted(set(compare) - set(p1_out)))


p1_out = part_one(input_file)
p2_out = part_two(p1_out)
print('Part1: ', max(p1_out), ' - Part2: ', max(p2_out))
