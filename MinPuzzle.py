###################################################################################################
# Allyson Aoki
# Assignment 7
#
# Using BFS/DFS, write an algorithm to reach the destination cell with minimum effort. How effort
# is defined: the effort of the route the the maximum absolute difference between two consecutive 
# cells.
###################################################################################################

def minEffort(puzzle):
    m = len(puzzle)
    n = len(puzzle[0])

    #initialize a 2D array to store the efforts
    efforts = [[float('inf')] * n for _ in range(m)]
    efforts[0][0] = 0

    #define the directions to move
    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    #helper function to check if a cell is valid
    def isValid(x,y):
        return 0 <= x < m and 0 <= y < n
    
    #helper function to get the maximum difference in a path
    def getMaxDiff(path):
        max_diff = 0
        for i in range(1, len(path)):
            diff = abs(path[i] - path[i-1])
            max_diff = max(max_diff, diff)
        return max_diff
    
    #perform bfs
    queue = [(0,0)]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if isValid(new_x, new_y):
                new_effort = max(efforts[x][y], abs(puzzle[new_x][new_y] - puzzle[x][y]))
                if new_effort < efforts[new_x][new_y]:
                    efforts[new_x][new_y] = new_effort
                    queue.append((new_x, new_y))


    return efforts[m-1][n-1]

'''
if __name__ == '__main__':
    puzzle = [[1,3,5], [2,8,3], [3,4,5]]
    print(minEffort(puzzle))
'''