# Problem Description
# You are a librarian, and after a long day, you decide to collect all the books kept on tables.
# In front of you, there are several stacks of books, A[i] denotes the size of the i'th stack of books. In one move you can pick an existing stack of books
# and merge it with another stack of books. The efforts required for this task is the size of stack being added. After this move new stack size is sum of both the
# stacks.
# To make this task fun you like to add some challenge to it and decide that, to any stack you will not add books to it for more than B times after that it will be
# added to any other stack.
# What is the minimum efforts required to collect all the books in one stack?
# Problem Constraints
# 1 <= |A| <= 105
# 1 <= A[i] <= 10⁹
# 1 <= B <= 105
# Input Format
# First argument A is an array of sizes of stacks of books.
# Second argument B is the integer denoting the maximum time books can be merged to a particular stack.

# Output Format
# Return an integer denoting minimum efforts required by librarian.
# Example Input
# Input 1:
# A = [3, 2, 1, 10]
# B = 2
# Input 2:
# A = [3, 3, 2]
# B = 1
# Example Output
# Output 1:
# 7
# Output 2:
# 7

# Example Explanation
# Explanation 1:
# Add stack of size 1 to stack of size 2 with '1' efforts, and resulting stack becomes 3.
# Currecnt stacks would look like [3, 3, 10]
# Now add both the '3's to '10' with efforts 3 + 3.
# So total efforts become 7.
# Explanation 2:
# Add stack of size 2 to stack of size 3 with '2' efforts.
# Resulting array looks like [3, 5]
# Now since we cannot add 3 to 5 as already 1 stack has been added to it.
# We add 5 to 3. So total efforts become 7