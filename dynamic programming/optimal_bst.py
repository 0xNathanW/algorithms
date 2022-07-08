import unittest

def optimal_bst(keys, freq):

    dp = [[None for j in keys] for i in keys]

    for i in range(len(dp)):
        for j in range(i+1):

            if i == j:
                dp[i][j] = freq[i]
            else:
                dp[i][j] = 0
    
    for i in range(len(dp-1), -1, -1):
        for j in range(len(dp), i, -1):


    for line in dp:
        print(line)


test_keys = [10, 12, 16, 21]
test_freq = [4, 2, 6, 3]

optimal_bst(test_keys, test_freq)