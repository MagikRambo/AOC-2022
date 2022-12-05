#AOC day 5
import re

lines = ''
with open('./2022/day5/input.txt') as f:
    lines = f.read().strip().split('\n')



    def part1(lines:list[str]):
        s1 = ['H','R','B','D','Z','F','L','S']
        s2 = ['T','B','M','Z','R']
        s3 = ['Z','L','C', 'H', 'N', 'S']
        s4 = ['S', 'C', 'F', 'J']
        s5 = ['P', 'G', 'H', 'W', 'R', 'Z', 'B']
        s6 = ['V','J','Z','G','D','N','M','T']
        s7 = ['G','L','N','W','F','S','P','Q']
        s8 = ['M','Z','R']
        s9 = ['M','C','L','G','V','R','T']

        sa = [s1,s2,s3,s4,s5,s6,s7,s8,s9]
        lines = lines[10:]
        for l in lines:
            e = list(map(int, re.findall(r'\d+', l)))
            for i in range(e[0]):
                sa[e[2]-1].append(sa[e[1]-1].pop())

        print(''.join(e.pop() for e in sa))

    def part2(lines:list[str]):
        s1 = ['H','R','B','D','Z','F','L','S']
        s2 = ['T','B','M','Z','R']
        s3 = ['Z','L','C', 'H', 'N', 'S']
        s4 = ['S', 'C', 'F', 'J']
        s5 = ['P', 'G', 'H', 'W', 'R', 'Z', 'B']
        s6 = ['V','J','Z','G','D','N','M','T']
        s7 = ['G','L','N','W','F','S','P','Q']
        s8 = ['M','Z','R']
        s9 = ['M','C','L','G','V','R','T']

        sa = [s1,s2,s3,s4,s5,s6,s7,s8,s9]
        lines = lines[10:]

        for l in lines:
            e = list(map(int, re.findall(r'\d+', l)))
            ar = []
            for i in range(e[0]):
                if len(sa[e[1]-1]) > 0:
                    ar.append(sa[e[1]-1].pop())
            sa[e[2]-1].extend(ar[::-1])
        print(''.join(e.pop() for e in sa))

part1(lines)
part2(lines)

