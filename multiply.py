import unittest
import numpy as np 

def grade_school(num1: int, num2: int) -> int:
    result, n = 0, 1
    for i in str(num1)[::-1]:
        carry, b = 0, n
        for j in str(num2)[::-1]:
            ij = int(i) * int(j) + carry
            if ij >= 10: # Will always be < 100 bcus 2 single digits nums.
                carry = int(str(ij)[0])
                result += int(str(ij)[1]) * b
            else:
                result += ij * b    
            b *= 10
        n *= 10
        result += carry * b
    return result
                

def karatsuba(num1: int, num2: int) -> int:
    
    # If numbers small just return python answer.
    if num1 < 10 and num2 < 10:
        return num1 * num2

    # Length number 
    n = (max(len(str(num1)), len(str(num2)))) // 2 
    a = num1 // (10**n)
    b = num1 % (10**n)
    c = num2 // (10**n)
    d = num2 % (10**n)
    
    ac, bd = karatsuba(a, c), karatsuba(b, d)
    adbc = karatsuba(a+b, c+d) - ac - bd
    
    return ac * (10**(n*2)) + (adbc * (10**n)) + bd


# Only deal with square matrix, takes Theta(n^3) time due to triple nested for loops.
def naive_matrix(a, b):
    n = len(a)
    c = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):      # Rows of output.  
        for j in range(n):  # Cols of output.
            for k in range(n):
                c[i][j] += (a[i][k] * b[k][j])
    return c

# Strassen algorithm to multiply two matrices.
# Assumption a and b are n x n matrices, where n is a power of 2.
def strassen(A, B):
    # Base case.
    if len(A) == 1:
        return A[0] * B[0]

    a11, a12, a21, a22 = split(A)
    b11, b12, b21, b22 = split(B)

    p1 = strassen(a11, b12-b22)
    p2 = strassen(a11+a12, b22)
    p3 = strassen(a21+a22, b11)
    p4 = strassen(a22, b21-b11)
    p5 = strassen(a11+a22, b11+b22)
    p6 = strassen(a12-a22, b21+b22)
    p7 = strassen(a11-a21, b11+b12)

    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p5 + p1 - p3 - p7

    return np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
 
def split(mtx):
    mid = len(mtx)//2
    return mtx[:mid,:mid], mtx[:mid, mid:], mtx[mid:, :mid], mtx[mid:, mid:]


def test_karatsuba():
    print(
        karatsuba(
            num1=3141592653589793238462643383279502884197169399375105820974944592,
            num2=2718281828459045235360287471352662497757247093699959574966967627,
            )
    )


class Tests(unittest.TestCase):

    def test_naive_matrix(self):

        cases = [
            (
                np.random.randint(100, size=(i, i)),
                np.random.randint(100, size=(i, i)),
            ) for i in range(2, 5)
        ]

        for case in cases:
            self.assertEqual(np.matmul(case[0], case[1]).tolist(), naive_matrix(case[0], case[1]))

    def test_strassen(self):

        cases = [
            (
                np.random.randint(25, size=(2**i, 2**i)),
                np.random.randint(25, size=(2**i, 2**i)),
            ) for i in range(1, 4)
        ]

        for case in cases:
            self.assertEqual(np.matmul(case[0], case[1]).all(), strassen(case[0], case[1]).all())

unittest.main()