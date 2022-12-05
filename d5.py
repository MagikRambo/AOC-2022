#AOC day 5
import re
import copy
from collections import defaultdict

with open('./2022/day5/input.txt') as f:
    lines = f.read().split('\n')

def parseData(idx, lines) -> tuple:
    s = []
    for l in lines[::-1]:
        if idx > len(l):
            continue
        if str.isalpha(l[idx]):
            s.append(l[idx])
    return s

def getData() -> list[list[str]]:
    i = 0
    s = ''
    c_arr = []
    for l in lines:
        #print(l)
        c_arr.append(l)
        i = i+1
        if i == 10:
            s = l
            break 

    idx = 0
    s = ''
    arr = []
    for l in lines:
        if any(i.isdigit() for i in l):
            s = l
            break

    for c in s:
        if c.isdigit():
            arr.append(idx)
        idx = idx + 1
    sa = []
    for i in range(0,9):
        sa.append(parseData(arr[i], c_arr))
    return sa

def part1(crates : defaultdict(lambda: []), lines:list[str]):

    for l in lines:
        e = list(map(int, re.findall(r'\d+', l)))
        for _ in range(e[0]):
            crates[e[2]-1].append(crates[e[1]-1].pop())

    print(''.join(e.pop() for e in crates.values()))

def part2(crates: defaultdict(lambda: []), lines:list[str]):

    for l in lines:
        e = list(map(int, re.findall(r'\d+', l)))
        ar = []
        for _ in range(e[0]):
            ar.append(crates[e[1]-1].pop())
        crates[e[2]-1].extend(ar[::-1])
    print(''.join(e.pop() for e in crates.values()))

crates = getData()
d = defaultdict(lambda:[])

for i in range(9):
    d[i] = crates[i]

crates_1 = defaultdict(int,d)
crates_2 = copy.deepcopy(crates_1)

lines_1 = copy.deepcopy(lines[10:])
lines_2 = copy.deepcopy(lines_1)
part1(crates_1, lines_1)
part2(crates_2, lines_2)
