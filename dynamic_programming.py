from unittest import TestCase

# LONGEST SUBSEQUENCE #

# BRUTE
def brute(s1, s2):
    print(s1, s2)

    if len(s1) == 0 or len(s2) == 0:
        return 0

    if s1[0] == s2[0]:
        print("+1")
        return 1 + brute(s1[1:], s2[1:])
    
    return max(brute(s1, s2[1:]), brute(s1[1:], s2))


#print(brute("AGGTAB", "GXTXAYB"))
print(brute("abcde", "ace"))