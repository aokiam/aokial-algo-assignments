###################################################################################################
# Allyson Aoki
# Assignment 2
#
# Given two sorted arrays of size m and n respectively, find the element that would be at the kth
# position in combined sorted array.
###################################################################################################

# mergeSort and merge code used from the 'Divide-and-Conquer Algorithms' module
def mergeSort(arr, start, end):
    if (start < end):
        mid = (start+end)//2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid+1, end)
        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    left_size = (mid-start) + 1
    right_size = (end-mid)
    
    left_array = [0]*left_size
    right_array = [0]*right_size

    for i in range(0, left_size):
        left_array[i] = arr[start+i]

    for i in range(0, right_size):
        right_array[i] = arr[mid+1+i]

    i=0
    j=0
    k=start

    while (i < left_size and j < right_size):
        if (left_array[i] < right_array[j]):
            arr[k]=left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1

    while (i < left_size):
        arr[k] = left_array[i]
        k += 1
        i += 1

    while (j < right_size):
        arr[k] = right_array[j]
        k += 1
        j += 1


# function to find the kth element in a sorted array
def kthElement(arr1, arr2, k):
    new_arr = arr1 + arr2                      #combines both arrays into one
    length = len(new_arr)   
    mergeSort(new_arr, 0, length-1)            #sends the array through mergeSort and returns the sorted array
    """ 
    print ("Sorted array:")                    #displays the sorted array
    for i in new_arr:
        print(i, end = ' ')
    print('\n')
    """
    return new_arr[k-1]                          #prints out the value at the kth position

"""
if __name__ == '__main__':  
    arr1 = [1,2,3,5,6]
    arr2 = [3,4,5,6,7]
    k = 5
    kthElement(arr1,arr2,k)
"""
