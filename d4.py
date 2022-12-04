#AOC day 4

with open('./2022/day4/input.txt') as f:
    lines = f.read().strip().split('\n')
    # lines = f.readlines().Split('\n')
tot = 0
for x in lines:
    
    l,r = x.split(',')
    # l1,l2,r1,r2 = map(int, list(x.split(',')).split('-'))
    l1,l2 = l.split('-')
    r1,r2 = r.split('-')
    arr1 = set(range(int(l1),int(l2)+1))
    arr2 = set(range(int(r1),int(r2)+1))
    

    # if arr1.issubset(arr2) or arr2.issubset(arr1):
    #     tot = tot + 1
    if arr1 & arr2:
        tot = tot + 1
print(tot)

   # x = l.split(',')
    
    #print(x)
#print(lines)
