import re
with open("input.txt") as f:
    lines = [l for l in f.readlines() if l]

val_map = {str(v):v for v in range(10)}
val_map.update(dict(one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9))
regex = re.compile(r"(?=(\d|(one|two|three|four|five|six|seven|eight|nine)))")
total = 0
for line in lines:
    matches = regex.findall(line)
    num = int(str(val_map[matches[0][0]]) + str(val_map[matches[-1][0]]))
    total += num
print(total)
