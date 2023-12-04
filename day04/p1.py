with open("input.txt") as f:
    lines = f.readlines()

total = 0
for line in lines:
    card, line = line.split(":")
    win_nums, have_nums = line.split("|")
    win_nums = [int(num) for num in win_nums.split()]
    have_nums = [int(num) for num in have_nums.split()]
    win_count = 0
    for num in have_nums:
        if num in win_nums:
            win_count += 1  
    if win_count:
        card_score = 2**(win_count - 1)
        total += card_score
print(total)

