#AOC 2022 Day 1 solution

with open('./2022/day1/input.txt') as f:
    raw = f.read().strip()
    lines = raw.split("\n\n")

    cal_arr = []
    for l in lines:
        cal = sum(map(int, l.split()))
        cal_arr.append(cal)
    s_cal_arr = sorted(cal_arr)

def part1():
    print(s_cal_arr[-1])

def part2():
    print(sum(s_cal_arr[-3:]))



    
part1()
part2()