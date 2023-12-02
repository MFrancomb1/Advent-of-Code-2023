import sys
import fileinput

file = sys.argv[1]
answer = 0
for line in fileinput.input(files=file):
   line = line[:-1]
   ten, one = False, False
   total = 0
   for i in range(len(line)):
        if (ten==False and line[i].isdigit()):
            ten=True
            total+= 10*int(line[i])
        if (one==False and line[len(line)-1-i].isdigit()):
            one=True
            total+=int(line[len(line)-1-i])
        if (ten==True and one==True):
            answer += total
            break
print(answer)