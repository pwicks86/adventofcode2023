from operator import mul
from functools import reduce

from collections import defaultdict
import re
with open("input.txt") as f:
    lines = f.readlines()

regex = re.compile(r"(\d+)\s+(red|blue|green)")
cube_sum = 0
for line in lines:
    max_color = defaultdict(int)
    draws = line.split(":")[1].split(";")
    for draw in draws:
        for match in regex.findall(draw):
            num = int(match[0])
            color = match[1]
            max_color[color] = max(max_color[color], num)
    cube_power = reduce(mul,max_color.values(), 1)
    cube_sum += cube_power
print(cube_sum)
