# BFS ASSIGNMENT
graph = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '5'],
    '4': ['2', '5', '6'],
    '5': ['2', '3', '4', '6'],
    '6': ['4', '5']
}

visited = []  # List for visited nodes
queue = []  # Initialize a queue

# Function of BFS
def BFS(visited, graph, current_node):
    visited.append(current_node)
    queue.append(current_node)

    # Creating loop to visit each node
    while queue:
        s = queue.pop(0)
        print(s, end="   ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

ans = input("Enter the starting vertex (1, 2, 3, 4, 5, 6) :  ")
print("The Breadth-First Search : ")
BFS(visited, graph, ans)
