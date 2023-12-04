from collections import defaultdict
from dataclasses import dataclass
with open("input.txt") as f:
    lines = f.readlines()

@dataclass
class Card:
    winning: list[int]
    have: list[int]

    def win_nums(self):
        return len([n for n in self.have if n in self.winning])

all_cards = defaultdict(list)
total = 0
for line in lines:
    card, line = line.split(":")
    win_nums, have_nums = line.split("|")
    win_nums = [int(num) for num in win_nums.split()]
    have_nums = [int(num) for num in have_nums.split()]
    card_num = int(card.split()[1])
    all_cards[card_num].append(Card(winning=win_nums, have=have_nums))

max_card = max(all_cards.keys()) + 1
card_count = 0
for i in range(1, max_card):
    print(i)
    while len(all_cards[i]) > 0:
        cur_card = all_cards[i].pop()
        card_count += 1
        win_nums = cur_card.win_nums()
        end = min(max_card, i + win_nums + 1)
        for j in range(i + 1, end):
            all_cards[j].append(all_cards[j][0])
print(card_count)

