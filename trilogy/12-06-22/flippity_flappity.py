# Problem Description
# Given an integer array X with size A. Initially, all the elements of this array are 0.
# Given another integer array Y with the same size A, all the elements in it are also 0.
# You have to handle three types of operations/queries on the given arrays:
# • 1 LR - Flip all the elements from 0 to 1 and 1 to 0 in the range L to R in the array X.
# • 2 P - For every element i = [1, A], Y[i] = Y[i] + X[i] *P
# • 3 J - Find Y[J].
# Given a 2D array B that represents the queries.
# ● Query Type 1 - B[i][0] = 1, B[i][1] = L, B[i][2] = R.
# ● Query Type 2 - B[i][0] = 2, B[i][1] = P, B[i][2] = 0.
# ● Query Type 3 - B[i][0] = 3, B[i][1¹] = J, B[i][2] = 0.
# Problem Constraints
# 1 <= A <= 105
# 1 <= L <= R <= A
# 1 <= J <= A
# 1 <= P <= 10⁹
# 1 <= Number of Queries <= 5 * 105

# Input Format
# The first argument is a single integer A.
# The second argument is a 2D integer array B.
# Output Format
# Return an integer array that represents the output of query type 3 in the input order.
# Example Input
# Input 1:
# A = 5
# B = [[1, 2, 3], [2, 5, 0], [1, 1, 4], [3, 4, 0], [2, 6, 0], [3, 1, 0]]
# Input 2:
# A = 7
# B = [[1, 1, 7], [2, 4, 0], [1, 2, 5], [3, 5, 0], [2, 6, 0], [1, 4, 4], [2, 4, 0], [3, 4, 0]]

# Example Output
# Output 1:
# 0 6
# Output 2:
# 4 8

# Example Explanation
# Explanation 1:
# Initially,
# X = [0, 0, 0, 0, 0]
# Y = [0, 0, 0, 0, 0]
# Query 1: flip (2, 3)
# X = [0, 1, 1, 0, 0]
# Y = [0, 0, 0, 0, 0]
# Query 2: add (5)
# X= [0, 1, 1, 0, 0]
# Y = [0, 5, 5, 0, 0]
# Query 3: flip(1, 4)
# X = [1, 0, 0, 1, 0]
# Y = [0, 5, 5, 0, 0]
# Query 4: Y[4] = 0
# X = [1, 0, 0, 1, 0]
# Y = [0, 5, 5, 0, 0]
# Query 5: add (6)
# X = [1, 0, 0, 1, 0]
# Y = [6, 5, 5, 6, 0]
# Query 6: Y[1] = 6

# Explanation 2:
# Initially,
# X = [0, 0, 0, 0, 0, 0, 0]
# Y = [0, 0, 0, 0, 0, 0, 0]
# Query 1: flip(1, 7)
# X = [1, 1, 1, 1, 1, 1, 1]
# Y = [0, 0, 0, 0, 0, 0, 0]
# Query 2: add (4)
# X = [1, 1, 1, 1, 1, 1, 1]
# Y = [4, 4, 4, 4, 4, 4, 4]
# Query 3: flip (2, 5)
# X = [1, 0, 0, 0, 0, 1, 1]
# Y = [4, 4, 4, 4, 4, 4, 4]
# Query 4: Y[5] = 4
# X = [1, 0, 0, 0, 0, 1, 1]
# Y = [4, 4, 4, 4, 4, 4, 4]
# Query 5: add (6)
# X = [1, 0, 0, 0, 0, 1, 1]
# Y [10, 4, 4, 4, 4, 10, 10]
# Query 6: flip(4, 4)
# X = [1, 0, 0, 1, 0, 1, 1]
# Y = [10, 4, 4, 4, 4, 10, 10]
# Query 7: add (4)
# X = [1, 0, 0, 1, 0, 1, 1]
# Y = [14, 4, 4, 8, 4, 14, 14]
# Query 8: Y[4] = 8