import sys
import fileinput

file = sys.argv[1]

answer = 0;

for line in fileinput.input(files=file):
    valid = True
    line = line.split(':')
    game_id = int(line[0][5:])
    for grab in line[1].split(';'):
        for pair in grab.split(','):
            num, color = pair.strip().split(' ')
            num = int(num)
            if color == 'red' and num>12:
                valid = False
            elif color == "green" and num>13:
                valid = False
            elif color == "blue" and num>14:
                valid = False
        if not valid:
            break
    if valid:
        answer += game_id

print(answer)