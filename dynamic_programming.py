import unittest

# LONGEST COMMON SUBSEQUENCE #

def brute(s1, s2):

    if len(s1) == 0 or len(s2) == 0:
        return 0

    if s1[0] == s2[0]:
        return 1 + brute(s1[1:], s2[1:])
    
    return max(brute(s1, s2[1:]), brute(s1[1:], s2))

# Works from end of array rather than start.
def brute2(s1, s2):

    if len(s1) == 0 or len(s2) == 0:
        return 0
    
    if s1[-1] == s2[-1]:
        return 1+brute2(s1[:-1], s2[:-1])
    
    return max(brute2(s1, s2[:-1]), brute2(s1[:-1], s2))

# With pointers.
def brute3(s1, s2, i=None, j=None):
    
    if i is None or j is None:
        i, j = len(s1)-1, len(s2)-1
    
    if i == -1 or j == -1:
        return 0

    if s1[i] == s2[j]:
        return 1 + brute3(s1, s2 , i-1, j-1)
    
    return max(brute3(s1, s2, i, j-1), brute3(s1, s2, i-1, j))

# Top down memoisation approach.
def top_down(s1, s2, i=None, j=None, dp=None):

    if i is None and j is None: i, j = len(s1)-1, len(s2)-1

    if dp is None: dp = [[-1 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

    if i==-1 or j==-1: return 0
    
    if dp[i][j] != -1:
        return dp[i][j]

    if s1[i] == s2[j]:
        dp[i][j] = 1 + top_down(s1, s2, i-1, j-1, dp)
        return dp[i][j]
    
    else:
        dp[i][j] = max(
            top_down(s1, s2, i, j-1, dp),
            top_down(s1, s2, i-1, j, dp),
        )
        return dp[i][j]

# Bottom up tabulation approach.
def bot_up(s1, s2):

    m, n = len(s1), len(s2)
    dp = [[None for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):

            if i==0 or j==0:
                dp[i][j] = 0

            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]


class Tests(unittest.TestCase):

    cases =[
        ("ABCBDAB", "BDCABA", 4),
        ("ABCDGH", "AEDFHR", 3),
        ("ABC", "AC", 2),
        ("AAAAAA", "AAAAAA", 6)
    ]

    def tests(self):

        for c in self.cases:
            self.assertEqual(brute(c[0], c[1]), c[2])
            self.assertEqual(brute2(c[0], c[1]), c[2])
            self.assertEqual(brute3(c[0], c[1]), c[2])
            self.assertEqual(top_down(c[0], c[1]), c[2])
            self.assertEqual(bot_up(c[0], c[1]), c[2])
            print("ok")

unittest.main()