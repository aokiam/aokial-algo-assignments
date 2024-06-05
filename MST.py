###################################################################################################
# Allyson Aoki
# Assignment 8
#
# Using a priority queue, implement Prim's algorithm
# ###################################################################################################


import heapq

def Prims(G):
    num_vertices = len(G)
    if num_vertices == 0:
        return []
    
    # to keep track of the vertices included in the MST
    in_mst = [False] * num_vertices
    mst_edges = []      # stores edges of MST
    edge_queue = []     # priority queue to pick the smallest edge

    # start with vertex 0
    start_vertex = 0
    in_mst[start_vertex] = True

    # add al edges from the start vertex to the priority queue
    for dest_vertex, weight in enumerate(G[start_vertex]):
        if weight != 0:
            heapq.heappush(edge_queue, (weight, start_vertex, dest_vertex))

    while edge_queue and len(mst_edges) < num_vertices-1:
        weight, u, v = heapq.heappop(edge_queue)

        if not in_mst[v]:
            # include this edge in the MST
            in_mst[v] = True
            mst_edges.append((u, v, weight))

            # add all edges from the newly included vertex to the priority queue
            for next_vertex, next_weight in enumerate(G[v]):
                if not in_mst[next_vertex] and next_weight != 0:
                    heapq.heappush(edge_queue, (next_weight, v, next_vertex))

    return mst_edges


'''
if __name__ == '__main__':
    graph = [[0, 8, 5, 0, 0, 0, 0], 
             [8, 0, 10, 2, 18, 0, 0], 
             [5, 10, 0, 3, 0, 16, 0], 
             [0, 2, 3, 0, 12, 30, 14], 
             [0, 18, 0, 12, 0, 0, 4], 
             [0, 0, 16, 30, 0, 0, 26], 
             [0, 0, 0, 14, 4, 26, 0]] 

    mst_result = Prims(graph)
    print(mst_result)
'''