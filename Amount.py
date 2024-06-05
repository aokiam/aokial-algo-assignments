###################################################################################################
# Allyson Aoki
# Assignment 5
#
# Implement a backtracking algorithm. Given a collecioction of amount values (A) and a target sum 
# (S), find all unique combinations in A where the amount values sum up to S.
###################################################################################################

def amount(A, S):
    result = []   
    A.sort()

    def backtrack(current_combo, start_index, remaining_target):
        # base case
        if remaining_target == 0:
            # if remaining target is zero, add the current combination to the result
            result.append(list(current_combo))
            return
        
        # recursion
        for i in range(start_index, len(A)):
            # avoid duplicates
            if i > start_index and A[i] == A[i-1]:
                continue

            if A[i] <= remaining_target:
                # add the current amount value to the combination
                current_combo.append(A[i])
                # recur w the updated combination, start index, and remaining target
                backtrack(current_combo, i+1, remaining_target - A[i])
                # backtrack by removing the last added amount value
                current_combo.pop()

    # call the recursive funtion with initial parameters
    backtrack([], 0, S)
    result.reverse()
    return result

'''
if __name__ == "__main__":
    A = [11, 1, 3, 2, 6, 1, 5]
    S = 8
    print(amount(A, S))
'''