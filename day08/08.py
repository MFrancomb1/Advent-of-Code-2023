import sys

def create_graph(nodes):
    #construct graph from input nodes
    d={}
    for node in nodes:
        d[node[:3]]= {"left":node[7:10], "right":node[12:15]}
    return d
        
def traverse(graph, instructions):
    #traverse the graph to find ZZZ
    count = 0
    idx = 0
    current = "AAA"
    found_z = False
    while not found_z:
        current = graph[current]["left"] if instructions[idx]=='L' else graph[current]["right"]
        count += 1
        idx += 1
        if idx==len(instructions):
            idx = 0
        found_z = True if current == "ZZZ" else False
    return count

f = open(sys.argv[1], 'r')
lines = f.readlines()
instructions = lines.pop(0).strip()
lines.pop(0)

graph = create_graph(lines)
answer = traverse(graph, instructions)

print(answer)