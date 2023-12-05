import sys
import fileinput

file = sys.argv[1]

answer = 0;

for line in fileinput.input(files=file):
    max_rgb = [0,0,0]
    line = line.split(":")[1].split(";")
    for grab in line:
        for pair in grab.split(','):
            num, color = pair.strip().split(' ')
            num = int(num)
            if color == 'red' and num>max_rgb[0]:
                max_rgb[0] = num
            if color == 'green' and num>max_rgb[1]:
                max_rgb[1] = num
            if color == 'blue' and num>max_rgb[2]:
                max_rgb[2] = num
    power = max_rgb[0]*max_rgb[1]*max_rgb[2]
    answer += power
print(answer)