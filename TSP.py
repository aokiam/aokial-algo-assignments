###################################################################################################
# Allyson Aoki
# Assignment 9
#
# Implement Travelling Salesman Problem using the nearest-neighbot heuristic
# ###################################################################################################

def solve_tsp(G):
    num_nodes = len(G)  # number of nodes (cities) in the graph
    visited = [False] * num_nodes   # keeps track of visited nodes
    path = []   # store the path taken

    current_node = 0
    total_distance = 0

    # loop to visit each node exactly once
    for _ in range(num_nodes):
        path.append(current_node)
        visited[current_node] = True

        next_node = None
        min_distance = float('inf')

        # loop through all neighbors of the current node to find the nearest unvisited one
        for neighbor in range(num_nodes):
            if not visited[neighbor] and 0 < G[current_node][neighbor] < min_distance:
                min_distance = G[current_node][neighbor]
                next_node = neighbor

        # if we found a next node, move to it and add the distance to the total distance
        if next_node is not None:
            current_node = next_node
            total_distance += min_distance
        else:
            break

    # after visiting all nodes, return to the starting node to complete the cycle
    path.append(0)

    # add the distance from the last node to the starting node to the total distance
    total_distance += G[current_node][0]

    return path


'''
if __name__ == '__main__':
    G = [
    [0, 2, 3, 20, 1],
    [2, 0, 15, 2, 20],
    [3, 15, 0, 20, 13],
    [20, 2, 20, 0, 9],
    [1, 20, 13, 9, 0],
    ]

    path = solve_tsp(G)
    print(path)
'''