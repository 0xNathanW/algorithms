# Inversion is a pair of array indicies i, j with i < j and array[i] > array[j].
def inversions(arr: list) -> int:
    n = len(arr)
    if n <= 1:
        return 0
    mid = n // 2
    left = inversions(arr[:mid])
    right = inversions(arr[mid:])
    