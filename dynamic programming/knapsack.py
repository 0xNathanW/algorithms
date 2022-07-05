import unittest

def knapsack(items, capacity):

    item_arr = [0] + list(items.keys()) # Adds empty & make indexable.
    dp = [[0 for c in range(capacity+1)] for item in item_arr]

    for i in range(1, len(dp)): # First row is empty.
        for j in range(capacity+1):
            
            not_include = dp[i-1][j] # Cell direct above.

            include = -1 # If cant include -1 will always lose.
            item = items[item_arr[i]]
            weight = item[1] 
            if weight <= j:
                include = dp[i-1][j-weight] + item[0]

            dp[i][j] = max(include, not_include)
    
    included = [] # Items optimally included in knapsack.
    i, j = len(dp)-1, len(dp[0])-1
    while i > 0:

        if dp[i][j] != dp[i-1][j]: # If item included.
            included.append(item_arr[i])
            j -= items[item_arr[i]][1]
        i -= 1
    
    return included


def print_dp(dp):
    for line in dp:
        print(line)


class Test(unittest.TestCase):

    def test_knapsack(self):

        items = {
        # Item: (value, weight)
            "A": (2, 3), 
            "B": (2, 1),
            "C": (4, 3),
            "D": (5, 4), 
            "E": (3, 2),
        }

        self.assertEqual()

items = {
# Item: (value, weight)
    "A": (2, 3), 
    "B": (2, 1),
    "C": (4, 3),
    "D": (5, 4), 
    "E": (3, 2),
}

knapsack(items, 7)