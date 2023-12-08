import sys

def rank_hand(hand):
    d = {}
    rank = 1
    kicker = 0
    exp = 0.01
    j=0
    for card in hand:
        kicker = kicker+(int(card)*exp) if card.isdigit() else kicker+(convert_face(card)*exp)
        exp = exp * 0.01
        d[card] = d.setdefault(card, 0) +1
        if card == 'J':
            j = j+1
    
    m = max(d.values())
    values = [x for x in d.values()]

    if m == 2 and values.count(2) == 2:
        if j == 2:
            rank = 6
        elif j == 1:
            rank = 5
        else:
            rank = 3
    elif m==2:
        rank = 4 if (j==1 or j==2) else 2
    elif m == 3 and 2 in values:
        if j == 2 or j == 3:
            rank = 7
        elif j == 1:
            rank = 6
        else:
            rank = 5
    elif m==3 :
        rank = 6 if (j==1 or j==3) else 4
    elif m==2 and j==1:
        rank = 4
    elif m==1 and j==1:
        rank = 2
    elif m==5:
        rank = 7
    elif m==4:
        rank = 7 if (j==1 or j==4) else 6
    
    return rank + kicker

def compare_card(card, other):
    if not card.isdigit():
        card = int(convert_face(card))
    else:
        card = int(card)
    if other.isdigit():
        other = int(other)
    else:
        other = int(convert_face(other))

    if card>other:
        return 1
    elif card<other:
        return -1
    else:
        return 0

def convert_face(card):
    match card:
        case "T":
            return 10
        case "J":
            return 1
        case "Q":
            return 12
        case "K":
            return 13
        case "A":
            return 14

answer = 0

f = open(sys.argv[1], 'r')
lines = f.readlines()

table=[]
for line in lines:
    # process input
    hand = {'cards':line[:5], 'bid': int(line.strip()[6:])}

    #rank hands
    hand.update({"rank": rank_hand(hand['cards'])})
    print(hand)
    table.append(hand)

#calculate winnings
sorted_table = [d['bid'] for d in sorted(table, key=lambda x:x['rank'])]
for i in range(len(sorted_table)):
    answer = answer + sorted_table[i]*(i+1)

print(answer)