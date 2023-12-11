import re

pile = open("day04.inp", "r")
scratchcards = [(re.split(r"\:|\|", line.strip())[1].strip().split(), re.split(r"\:|\|", line.strip())[2].strip().split()) for line in pile.readlines()]

points = 0
multipliers = [1 for _ in range(len(scratchcards))]

for i, card in enumerate(scratchcards):
    have, winning = card
    overlap = len(set(have).intersection(set(winning)))

    if overlap > 0: points += 2**int(overlap-1)

    for j in range(0, overlap):
        multipliers[i+j+1] += 1*multipliers[i]

print("A: ", points)
print("B: ", sum(multipliers))