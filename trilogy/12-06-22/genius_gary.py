# Gary being the smartest guy in the town is a friend of you.
# He challenges you with an interesting problem. He gives you a number A and asks you to find the number of "actual" greater pairs till A.
# An actual greater pair(a, b) means that it should hold following conditions
# • 0 <= a < b <= n
# • Sum of digits of a < Sum of digits of b
# The number A is given you in form of a string as it can be very huge!
# Return the number of actual greater pairs with above conditions modulo 1e9+7.

# Input:
# 2
# Output:
# 3
# Explanation:
# The actual greater pairs are [(0,1), (0,2), (1,2)]

# Input
# 5
# Output
# 15
# Explanation
# All possible pairs under 5 are actual greater pairs

def solve(A):
    count = 0
    num = int(A)
    for i in range(num+1):
        for j in range(i+1, num+1):
            if sum(map(int, str(i))) < sum(map(int, str(j))):
                count += 1
    return count % (10**9 + 7)

A = "777190496"
A = "5"
print(solve(A))

# Working but very inefficient function