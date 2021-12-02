def get_input(infile):
    with open(infile) as file:
        output = [int(line.strip()) for line in file]
    return output

def part_one(day_input):
    n = 0
    t0 = 100000
    for i in day_input:
        if i > t0:
            n = n + 1
        t0 = i
    return n

def part_two(day_input):
    n = 0
    prev3 = 100000
    for num, depth in enumerate(day_input):
        if num >= 2:
            depth3 = sum(day_input[num-2:num+1])
            if depth3 > prev3:
                n = n + 1
            prev3 = depth3
    return n

d = get_input('input.txt')
part_one(get_input('input.txt'))
part_two(get_input('input.txt'))