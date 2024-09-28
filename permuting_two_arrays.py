

"""You have two arrays of integers, A and B, each with the same length n.
You need to check if you can rearrange the elements in these arrays so that for
every index i, the sum of A[i] and B[i] is greater than or equal to k.
Your task is to find out if such a rearrangement is possible."""

def twoArrays(k, A, B):
    # Sort A in ascending order
    A.sort()
    # Sort B in descending order
    B.sort(reverse=True)

    # Check if for every i, A[i] + B[i] >= k
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"

    return "YES"