import unittest
import random

# Array must be sorted first, if so runs in log(n) time.
def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper: 
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   
                break    
            lower = x
        elif target < val:
            upper = x
    
    
class Tests(unittest.TestCase):

    def test_binary(self):

        cases = [
            sorted(random.sample(range(1, 40), 5)),
            sorted(random.sample(range(-50, 20), 12)),
            sorted(random.sample(range(0, 1000), 200)),
        ]

        items = [random.choice(case) for case in cases]

        for i in range(len(cases)):
            self.assertEqual(
                cases[i].index(items[i]),
                binary_search(cases[i], items[i])
            )

unittest.main()