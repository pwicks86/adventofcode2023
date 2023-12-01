with open("input.txt") as f:
    lines = [l for l in f.readlines() if l]

total = 0
for line in lines:
    nl = [l for l in line if l.isnumeric()]
    num = int(nl[0] + nl[-1])
    total += num
print(total)
