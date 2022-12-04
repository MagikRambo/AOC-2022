#AOC day 4

with open('./2022/day4/input.txt') as f:
    lines = f.read().strip().split('\n')
    
def get_arrs(line:str) -> tuple:
    l,r = line.split(',')
    l1,l2 = l.split('-')
    r1,r2 = r.split('-')
    arr1 = set(range(int(l1),int(l2)+1))
    arr2 = set(range(int(r1),int(r2)+1))
    return (arr1,arr2)


def part1():
    tot = 0
    for x in lines:
        arr1,arr2 = get_arrs(x)
        if arr1.issubset(arr2) or arr2.issubset(arr1):
            tot = tot + 1
    return tot
def part2():
    tot = 0
    for x in lines: 
        arr1,arr2 = get_arrs(x)
        if arr1 & arr2:
            tot = tot + 1
    return tot

print(part1())
print(part2())
