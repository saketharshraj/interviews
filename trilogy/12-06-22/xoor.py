# You are given two integer arrays A and B. Let's define another array C of size |A| * |B| containing Bitwise OR of all possible pairs of elements of A with all elements
# of B i.e. A[i] | B[j] for all valid i and j.
# Find the Bitwise XOR of array C i.e C[1] ℗ C[2] + C[3] ℗ ... + C[|A| * |B|].

# Input
# A = [2]
# B = [5, 0, 3]
# Output
# 6
# Explanation
# Array C = [7, 2, 3]. Bitwise XOR of C is 6
# Input
# A = [1, 2]
# B = [4, 10]
# Output
# 2
# Explanation
# Array C = [5, 11, 6, 10]. Bitwise XOR of C is 2

def solve(A, B):
    # c = [a | b for a in A for b in B]
    # xor = 0
    # for i in c:
    #     xor ^= i
    # return xor
    # make above logic memory efficient
    res = 0
    for i in range(len(A)):
        for j in range(len(B)):
            res ^= A[i] | B[j]
    return res

a = [1, 2]
b = [4, 10]
print(solve(a, b))