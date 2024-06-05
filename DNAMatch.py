###################################################################################################
# Allyson Aoki
# Assignment 3
#
# Two functions -- one top-down and the other bottom-up -- that find the length of the longest 
# common sting alignment between two strings
###################################################################################################


# top-down approach to finding the longest common string alignment
def dna_match_topdown(DNA1, DNA2):
    # create a memoization dictionary
    dna_memo = {}

    # helper function to find the length of the longest common string alignment
    def find_length(i, j):
        # base case: when either of the strings are empty
        if i == 0 or j == 0:
            return 0
        # checks if result has already been computed and in the dictionary
        if (i, j) in dna_memo:
            return dna_memo[(i, j)]
        
        if DNA1[i-1] == DNA2[j-1]:  # if characters at the current position match, add to dict
            dna_memo[(i, j)] = 1 + find_length(i-1, j-1)
        else:   # if not, check the next character from either DNA string
            dna_memo[(i,j)] = max(find_length(i-1, j), find_length(i, j-1))

        return dna_memo[(i, j)]
    
    return find_length(len(DNA1), len(DNA2))


# bottom-down approach to finding the longest string alignment
def dna_match_bottomup(DNA1, DNA2):
    if not DNA1 or not DNA2:
        return 0

    # create a table and initialize it with zeros
    matches = [[0] * (len(DNA1) + 1) for _ in range((len(DNA2) + 1))]

    # iterate through both strings
    for i in range(1, (len(DNA1) + 1)):
        for j in range (1, (len(DNA2) + 1)):
            if DNA1[i-1] == DNA2[j-1]: # if characters at current position match, add 1 to current spot in table
                matches[i][j] = 1 + matches[i-1][j-1]
            else:   # if not, check the next character from either DNA string
                matches[i][j] = max(matches[i-1][j], matches[i][j-1])
        
    return matches[len(DNA1)][len(DNA2)]

    # bottom right corner of table contains the length of the longest string alignment

'''
if __name__ == "__main__":
    string1 = "ABCDEFG"
    string2 = "HIJKLMN"

    print(dna_match_topdown(string1, string2))
    print(dna_match_bottomup(string1, string2))
'''