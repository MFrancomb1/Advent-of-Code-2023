import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()
x = []
answer = 0

for line in lines:
   line = int(line.strip().split(":")[1].replace(" ", ""))
   print(line)
   x.append(line)
x = [(x[0],x[1])]

winning = []
for time, record in x:
    for i in range(1, time):
        distance = i*(time-i)
        if distance>record:
            winning.append((time-i)-i+1)
            break
answer = winning[0]
for i in range(1, len(winning)):
    answer = answer*winning[i]

print(answer)