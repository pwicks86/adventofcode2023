import re

with open("input.txt") as f:
    schematic = [l.strip() for l in f.readlines()]

regex = re.compile(r"(\d+)")

part_sum = 0
for idx, line in enumerate(schematic):
    for m in regex.finditer(line):
        cur_num = int(m.group(0))
        start = m.start()
        end = m.end()
        lpos = max(0, start - 1)
        left = line[lpos]
        rpos = min(len(line) - 1, end)
        right = line[rpos]
        above = "" if idx == 0 else schematic[idx - 1][lpos:rpos + 1]
        below = "" if idx == len(schematic) -1  else schematic[idx + 1][lpos:rpos + 1]
        surround = [left, right, above, below]
        is_part_num = False
        for s in surround:
            for c in s:
                if c != "." and not c.isnumeric():
                    is_part_num = True
        if is_part_num:
            part_sum += cur_num
print(part_sum)