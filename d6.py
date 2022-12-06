

with open('./2022/day6/input.txt') as f:
    lines = f.read().strip()

def find_distinct(sw_size):
    for i in range(len(lines)):
        l = lines[i:i+sw_size]
        if len(set(l)) == sw_size:
            return i+sw_size

def part1():
    return find_distinct(4)

def part2():
    return find_distinct(14)


print(part1())
print(part2())
    

