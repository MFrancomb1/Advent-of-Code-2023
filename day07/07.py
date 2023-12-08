import sys

def rank_hand(hand):
    d = {}
    rank = 1
    kicker = 0
    exp = 0.01
    for card in hand:
        kicker = kicker+(int(card)*exp) if card.isdigit() else kicker+(convert_face(card)*exp)
        exp = exp * 0.01
        d[card] = d.setdefault(card, 0) +1
        match d[card]:
            case 2:
                current_count = [value for value in d.values()]
                if current_count.count(2) > 1:
                    rank = max(rank, 3)
                elif 3 in current_count:
                    rank = max(rank, 5)
                else:
                    rank = max(rank, 2)
            case 3:
                if 2 in [value for value in d.values()]:
                    rank = max(rank, 5)
                else:
                    rank = max(rank, 4)
            case 4:
                rank = 6
            case 5:
                rank = 7

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
            return 11
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
    table.append(hand)

#calculate winnings
sorted_table = [d['bid'] for d in sorted(table, key=lambda x:x['rank'])]
for i in range(len(sorted_table)):
    answer = answer + sorted_table[i]*(i+1)

print(answer)