def accumulator(in_data):
    done = []
    acc = 0
    cursor = 0
    while cursor not in done:
        if cursor >= len(in_data):
            return {'acc': acc, 'terminated': True, 'positions': done}
        cur_task = in_data[cursor]
        done.append(cursor)
        if cur_task[0] == 'jmp':
            cursor += cur_task[1]
        else:
            if cur_task[0] == 'acc':
                acc += cur_task[1]
            cursor += 1
    return {'acc': acc, 'terminated': False, 'positions': done}

def part_one(in_data):
    return accumulator(in_data)
    
def part_two(in_data):
    def modify_in_data(in_data, idx):
        n_in_data = in_data.copy()
        n_in_data[idx] = ({"nop": "jmp", "jmp": "nop"}[n_in_data[idx][0]],n_in_data[idx][1])
        return n_in_data

    # Do a run to find potential swap-candidates:
    acc_jmp = [i for i in accumulator(in_data)['positions'] if in_data[i][0] == "nop" or in_data[i][0] == "jmp"]
    for i in acc_jmp:
        out = accumulator(modify_in_data(in_data, i))
        if out['terminated'] is True:
            return out

with open('input.txt') as file:
    in_data = [(op,int(arg)) for op, arg in (line.split() for line in file)]

print('Part1: ', part_one(in_data)['acc'], ' - Part2: ', part_two(in_data)['acc'])
