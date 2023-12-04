import sys
import fileinput

file = sys.argv[1]
answer = 0

for line in fileinput.input(files=file):
    points = 0
    line = line[8:].split('| ')
    winning = line[0].split()
    match_to = line[1].split()
    for number in match_to:
        if number in winning:
            points = 1 if points == 0 else points*2
    answer+= points
print(answer)