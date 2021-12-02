def get_input(inputfile):
    puzinput = []
    with open(inputfile) as file:
        for line in file:
            puzinput.append(line.strip())
    return puzinput

d = get_input('input2.txt')

def part_one(input):
    x = 0
    y = 0
    for i in input:
        c = i.split()
        if c[0] == 'forward':
            x = x + int(c[1])
        elif c[0] == 'up':
            y = y - int(c[1])
        else: y = y + int(c[1])
    return x * y

def part_two(input):
    x = 0
    y = 0
    aim = 0
    for i in input:
        c = i.split()
        if c[0] == 'forward':
            x = x + int(c[1])
            y = y + int(c[1]) * aim
        elif c[0] == 'up':
            aim = aim - int(c[1])
        else: aim = aim + int(c[1])
    return x * y

part_one(d)
part_two(d)