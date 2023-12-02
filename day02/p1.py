from collections import defaultdict
import re
with open("input.txt") as f:
    lines = f.readlines()

regex = re.compile(r"(\d+)\s+(red|blue|green)")
id_sum = 0
for line in lines:
    max_color = defaultdict(int)
    draws = line.split(":")[1].split(";")
    game_id = int(line.split(":")[0].split()[1])
    for draw in draws:
        for match in regex.findall(draw):
            num = int(match[0])
            color = match[1]
            max_color[color] = max(max_color[color], num)
    if max_color["red"] <= 12 and max_color["green"] <= 13 and max_color["blue"] <= 14:
        id_sum += game_id
print(id_sum)
