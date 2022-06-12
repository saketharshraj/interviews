# There are N rabbits standing on an infinite number line.
# Every rabbit has some specific charcateristic represented by lowercase latin letters given by string A.
# Initially they are at some integer position B₁. They will start moving when you order them with 1 unit per second.
# Their initial direction will be given by an integer array C, which contains only 1 or -1.
# 1 mean that rabbit will move in positive direction or right side of the number line and -1 mean opposite direction.
# If two rabbits with same characteristic value meet they will change their direction of movement.
# Find the sum of distance of all the the possible pair of rabbits after D seconds when you ordered them to move.
# Problem Constraints
# 1 <= N <= 105
# A₁ = {lowercase latin aplhabets}
# -10^6 <= B₁ <= 10^6
# C = {1, -1}
# 0 <= D <= 10^6
# Input Format
# First argument is a string A.
# Second argument is an integer array B.
# Third argument is an integer array C.
# Fourth argument is an integer D.

# Output Format
# Return an integer.
# Example Input
# Input 1:
# A = "aba"
# B = [-2, 0, 2]
# C = [1, -1, -1]
# D = 3
# Input 2:
# A = "cd"
# B = [1, 0]
# C = [1, -1]
# D = 2
# Example Output
# Output 1:
# 8
# Output 2:
# 5
# Example Explanation
# Explanation 1:
# After 0 second the positions are [-2, 0, 2]
# After 1 second the positions are [-1, -1, 1]
# After 2 second the positions are [0, 2, 0]
# After 3 second the positions are [-1, 3, 1]
# Distance between all pairs are 8
# Explanation 2:
# After 0 second the positions are [1, 0]
# After 1 second the positions are [2, -1]
# After 2 second the positions are [3, -2]
# Distance between all pairs are 5