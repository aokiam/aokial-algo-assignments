###################################################################################################
# Allyson Aoki
# Assignment 4
#
# Solve Dynamic Programming Problem and find its optimal solution. Given a list of numbers, return
# a subsequence of non-consecutive numbers in the form of a list that would have the maximum sum.
###################################################################################################


def max_independent_set(nums):
    # checks if the input list is empty or all numbers in the list are negative
    if (not nums or all(num < 0 for num in nums)):
        return []
    
    n = len(nums)
    # array that holds the max sum up to each index
    max_sum = [0] * n

    # base cases
    max_sum[0] = max(0, nums[0])    # max sum up to the first index
    if n > 1:
        max_sum[1] = max(max_sum[0], nums[1])   # max sum up to the second index

    # iterate through the list starting from the third element
    for i in range (2, n):
        #calculate the max sum at each index using dynamic programming
        max_sum[i] = max(max_sum[i-1], max_sum[i-2] + nums[i])

    # reconstruct the solution by backtracking trhough the dynamic programming array
    result = []
    i = n - 1
    while i >= 0:
        # if current element is included in the max sum, add it to the result
        if i == 0:
            result.append(nums[i])
            break
        elif max_sum[i] != max_sum[i-1]:
            result.append(nums[i])
            i -= 2
        else:
            i -= 1

    reverse_array(result)
    # checks for the case of distinct positive and negative numbers
    for i in range(len(result) - 1):
        if result[i] < 0:
            result.pop(i)

    # checks for case of negative numbers and zeros
    if len(result) == 1:
        if result[0] < 0:
            return [0]
        
    return result

# helper function to reverse the order of an array
def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n-1-i] = arr[n-1-i], arr[i]

'''
if __name__ == "__main__":
    test1 = [7,2,5,8,6]
    test2 = [-5, -5, 25, 1, 0, 3, 5]
    test3 = [-1,-1,0,-34]

    print(max_independent_set(test1))
    print(max_independent_set(test2))
    print(max_independent_set(test3))
'''