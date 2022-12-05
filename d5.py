#AOC day 5
import re

lines = ''
with open('./2022/day5/input.txt') as f:
    lines = f.read().strip().split('\n')

def getData(idx, lines) -> tuple:
    s = []
    for l in lines[::-1]:
        if idx > len(l):
            continue
        if str.isalpha(l[idx]):
            s.append(l[idx])
    return s



# i = 0
# s = ''
# c_arr = []
# for l in lines:
#     #print(l)
#     c_arr.append(l)
#     i = i+1
#     if i == 4:
#         s = l
#         break 

# idx = 0
# s = ''
# arr = []
# for l in lines:
#     if any(i.isdigit() for i in l):
#         s = l
#         break

# for c in s:
#     if c.isdigit():
#         arr.append(idx)
#     idx = idx + 1

# c = lines[:4]
# print(c)

# s1 = getData(arr[0], c_arr)
# s2 = getData(arr[1], c_arr)
# s3 = getData(arr[2], c_arr)

s1 = ['H','R','B','D','Z','F','L','S']
s2 = ['T','B','M','Z','R']
s3 = ['Z','L','C', 'H', 'N', 'S']
s4 = ['S', 'C', 'F', 'J']
s5 = ['P', 'G', 'H', 'W', 'R', 'Z', 'B']
s6 = ['V','J','Z','G','D','N','M','T']
s7 = ['G','L','N','W','F','S','P','Q']
s8 = ['M','Z','R']
s9 = ['M','C','L','G','V','R','T']

# s1 = ['Z','N']
# s2 = ['M','C','D']
# s3 = ['P']
#print(s1.pop())
# s4 = getData(arr[3], c_arr)
# s5 = getData(arr[4], c_arr)
# s6 = getData(arr[5], c_arr)
# s7 = getData(arr[6], c_arr)
# s8 = getData(arr[7], c_arr)
# s9 = getData(arr[8], c_arr)

sa = [s1,s2,s3,s4,s5,s6,s7,s8,s9]
#sa = [s1,s2,s3]
#print(sa)
# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(s5)
# print(s6)
# print(s7)
# print(s8)
# print(s9)
lines = lines[10:]
for l in lines:
    e = list(map(int, re.findall(r'\d+', l)))
    ar = []
    for d in range(e[0]):
        if len(sa[e[1]-1]) > 0:
            ar.append(sa[e[1]-1].pop())
        #sa[e[2]-1].append(sa[e[1]-1].pop())
    sa[e[2]-1].extend(ar[::-1])

a = []
for e in sa:
    if len(e) > 0:
        a.append(e.pop())
    
print(a)
#     break
#     #print(arr)

