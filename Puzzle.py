###################################################################################################
# Allyson Aoki
# Assignment 8
#
# Traverse through the 2-D puzzle of size M x N covering the minimum number of cells from the
# starting cell to the end where you can only move to an empty cell and not to those with a
# barrier in it
# ###################################################################################################


from collections import deque

def solve_puzzle(board, source, destination):
    rows, cols = len(board), len(board[0])
    directions = {'L': (0,-1),
                  'R': (0,1),
                  'U': (-1,0),
                  'D': (1,0)}
    
    if source == destination:
        return [source], ''
    
    queue = deque([source])
    visited = set()
    visited.add(source)
    parent = {source: None}
    move_dir = {source: ''}

    # BFS loop
    while queue:
        # get the current cell from the queue
        current = queue.popleft()
        current_row, current_col = current

        # iterate through all possible directions
        for move, (dr, dc) in directions.items():
            new_row, new_col = current_row + dr, current_col + dc
            new_pos = (new_row, new_col)

            #check if the new position is within bounds, is an empty cell, and has not been visited
            if (0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] == '-' and new_pos not in visited):
                parent[new_pos] = current
                move_dir[new_pos] = move
                visited.add(new_pos)
                queue.append(new_pos)

                # if the new position is the destination, reconstruct the path and direction string
                if new_pos == destination:
                    path = []
                    directions_str = []

                    # backtrack from the destination to the source to build the path
                    while new_pos is not None:
                        path.append(new_pos)
                        if new_pos in move_dir:
                            directions_str.append(move_dir[new_pos])
                        new_pos = parent[new_pos]

                    return path[::-1], ''.join(directions_str[::-1])
                
    return None

'''
if __name__ == '__main__':
    puzzle = [['-', '-', '-', '-', '-'],
              ['-', '-', '#', '-', '-'],
              ['-', '-', '-', '-', '-'],
              ['#', '-', '#', '#', '-'],
              ['-', '#', '-', '-', '-']]
    
    source = (0,0)
    destination = (0,0)
    result = solve_puzzle(puzzle, source, destination)
    print(result)
'''