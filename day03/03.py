import sys
import fileinput

file = sys.argv[1]

answer = 0
matrix = []
for line in fileinput.input(files=file):
    matrix.append([*line[:]])
    print([*line[:-1]])

d = {}

for row in range(len(matrix)):
    for column in range(len(matrix[0])):
        current = matrix[row][column]

print(answer)