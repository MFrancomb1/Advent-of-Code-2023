import sys

file = sys.argv[1]

f = open(file, "r")

lines = f.readlines()
cards = {k:1 for k in range(1, len(lines)+1)}
card = 1

for line in lines:
    points = 0
    line = line[8:].strip().split('| ')
    winning = line[0].split()
    candidates = line[1].split()

    for number in candidates:
        if number in winning:
            points += 1

    for i in range(1, points+1):
        cards[card+i] = cards[card+i]+(1*cards[card])
    card += 1
    
print(sum(cards.values()))