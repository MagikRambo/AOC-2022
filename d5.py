#AOC day 5
import re
import copy
from collections import defaultdict

with open('./2022/day5/input.txt') as f:
    lines = f.read().strip().split('\n')
def part1(crates : defaultdict(lambda: []), lines:list[str]):

    for l in lines:
        e = list(map(int, re.findall(r'\d+', l)))
        for _ in range(e[0]):
            crates[e[2]].append(crates[e[1]].pop())

    print(''.join(e.pop() for e in crates.values()))

def part2(crates: defaultdict(lambda: []), lines:list[str]):

    for l in lines:
        e = list(map(int, re.findall(r'\d+', l)))
        ar = []
        for _ in range(e[0]):
            ar.append(crates[e[1]].pop())
        crates[e[2]].extend(ar[::-1])
    print(''.join(e.pop() for e in crates.values()))

crates = {
    1: ['H','R','B','D','Z','F','L','S'],
    2: ['T','B','M','Z','R'], 
    3: ['Z','L','C', 'H', 'N', 'S'],
    4: ['S', 'C', 'F', 'J'],
    5: ['P', 'G', 'H', 'W', 'R', 'Z', 'B'],
    6: ['V','J','Z','G','D','N','M','T'],
    7: ['G','L','N','W','F','S','P','Q'],
    8: ['M','Z','R'],
    9: ['M','C','L','G','V','R','T']}

crates_1 = defaultdict(int,crates)
crates_2 = copy.deepcopy(crates_1)

lines_1 = copy.deepcopy(lines[10:])
lines_2 = copy.deepcopy(lines_1)
part1(crates_1, lines_1)
part2(crates_2, lines_2)

