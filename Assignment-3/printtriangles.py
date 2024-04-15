# Brute force method to check the output
edges = []
with open('data.txt', 'r') as file:
    for line in file:
        edges.append(line.split())

num_edges = len(edges)
adj_list = {}
for edge in edges:
    if edge[0] not in adj_list:
        adj_list[edge[0]] = []
    adj_list[edge[0]].append(edge[1])
    if edge[1] not in adj_list:
        adj_list[edge[1]] = []
    adj_list[edge[1]].append(edge[0])

triangles = 0
for edge in edges:
    for node in adj_list[edge[0]]:
        if node in adj_list[edge[1]]:
            triangles += 1
print("No of triangles: ", int(triangles / 3))