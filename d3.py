#AOC day 3

with open('./2022/day3/input.txt') as f:
    lines = f.read().strip().split('\n')
    # lines = f.readlines().Split('\n')

def part1():
    
    tot = 0
    for l in lines:
        i = len(l) // 2
        left = l[:i]
        right = l[i:]

        L = set(list(left))
        R = set(list(right))

        x = L.intersection(R)
        x = list(x)[0]
        if ord("a") <= ord(x) <= ord("z"):
            tot = tot + (ord(x) - ord("a") + 1)
        else:
            tot = tot + (ord(x) - ord("A") + 1) + 26

    return tot
    
def part2():

    tot = 0 
    for i in range(0, len(lines), 3):
        sw = lines[i:i+3]

        a1,a2,a3 = map(set, sw)
        x = set.intersection(a1,a2,a3)
        x = list(x)[0]
        if ord("a") <= ord(x) <= ord("z"):
            tot = tot + (ord(x) - ord("a") + 1)
        else:
            tot = tot + (ord(x) - ord("A") + 1) + 26

    return tot


print(part1())
print(part2())
