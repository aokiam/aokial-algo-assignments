###################################################################################################
# Allyson Aoki
# Assignment 4
#
# Implement a backtracking algorithm. Write the implementation to solve the powerset problem.
# Given a set of n distinct numbers return its power set.
###################################################################################################

# helper function for the powerset function
def powerset_helper(pointer, choices_made, input_set, result):
    # base case
    if pointer < 0:
        # add the current subset to the result
        result.append(choices_made[:])
        return
    
    # include the current element pointed by the pointer in the subset
    choices_made.append(input_set[pointer])
    # recursively generating subsets without the current element
    powerset_helper(pointer - 1, choices_made, input_set, result)
    # backtracking: remove the last element added to the subset
    choices_made.pop()
    powerset_helper(pointer - 1, choices_made, input_set, result)



def powerset(inputSet):
    result = []
    # start generating subsets with the last element of the input set
    powerset_helper(len(inputSet) - 1, [], inputSet, result)
    return result

'''
if __name__ == "__main__":
    print(powerset([1,2,3]))
    print(powerset([]))
'''