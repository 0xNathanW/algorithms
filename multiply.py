from math import ceil, floor

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

print(
    karatsuba(
        num1=3141592653589793238462643383279502884197169399375105820974944592,
        num2=2718281828459045235360287471352662497757247093699959574966967627,
        )
)
