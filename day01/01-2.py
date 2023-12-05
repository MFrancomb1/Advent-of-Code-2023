import sys
import fileinput

file = sys.argv[1]

d = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
     }

answer = 0

for line in fileinput.input(files=file):
    line = line[:-1]
    for key in d.keys():
        if key in line:
            line = line.replace(key, d.get(key))
    ten, one = False, False
    total = 0
    print("line",line)
    for i in range(len(line)):
        if (ten==False and line[i].isdigit()):
            ten=True
            total+= 10*int(line[i])
        if (one==False and line[len(line)-1-i].isdigit()):
            one=True
            total+=int(line[len(line)-1-i])
        if (ten==True and one==True):
            print(total)
            answer += total
            break
print(answer)