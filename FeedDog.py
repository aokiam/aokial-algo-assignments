###################################################################################################
# Allyson Aoki
# Assignment 5
#
# Implement a greedy algorithm. Each dog has a specific hunger level given by array 
# hunger_level[1...n]. You have a couple of dog bisuits of biscuit_size[1...m]. Your goal is to
# satisfy maximum number of hungry dogs. 
###################################################################################################

def feedDog(hunger_level, biscuit_size):
    # sort both arrays in non-decreasing order
    hunger_level.sort()
    biscuit_size.sort()

    #initialize pointers and counter
    hunger_ptr = biscuit_ptr = 0
    dogs_satisfied = 0

    # iterate over hunger levels array
    while hunger_ptr < len(hunger_level) and biscuit_ptr < len(biscuit_size):
        # if the current biscuit size can satisfy the current hunger level
        if biscuit_size[biscuit_ptr] >= hunger_level[hunger_ptr]:
            dogs_satisfied += 1
            hunger_ptr += 1
            biscuit_ptr += 1
        else:
            # if biscuit size cannot satisfy current hunger, move to the next biscuit size
            biscuit_ptr += 1

    return dogs_satisfied

'''
if __name__ == "__main__":
    h1 = [1, 2, 3]
    b1 = [1, 1]
    print(feedDog(h1, b1))

    h2 = [2, 1]
    b2 = [1, 3, 2]
    print(feedDog(h2, b2))
'''