from collections import defaultdict
import re

with open("input.txt") as f:
    schematic = [l.strip() for l in f.readlines()]

regex = re.compile(r"(\d+)")

gears = defaultdict(list)
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
        if left == "*":
            gears[(lpos,idx)].append(cur_num)
        elif right == "*":
            gears[(rpos,idx)].append(cur_num)
        elif (below.find("*") != -1):
            star_pos = below.find("*") + lpos
            gears[(star_pos, idx + 1)].append(cur_num)
        elif ((star_pos := above.find("*")) != -1):
            star_pos = above.find("*") + lpos
            gears[(star_pos, idx - 1)].append(cur_num)
gear_sum = 0
for gear in gears.values():
    if len(gear) == 2:
        gear_sum += (gear[0] * gear[1])

print(gear_sum)