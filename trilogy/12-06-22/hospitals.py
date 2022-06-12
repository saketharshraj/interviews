# Problem Description
# There are N villages located on a straight highway, the highway allows only one directional traffic that is away from the start of the highway.
# The positions of villages are given by an array A, where A₁ denotes the distance of village form start of the highway.
# The population of villages are given by another array B.
# Local government wants to build hospitals in C villages such that sum of the minimum distance travelled by every person to reach a hospital is minimum.
# Find minimum sum of distance to travel possible by buliding hospitals optimally in villages.
# Note: There should always be a hospital in the last village that is farthest village from the start of the highway.

# Input Format
# First argument is an integer array A.
# Second arguemnt is an integer array B.
# Third argument is an integer C.
# Output Format
# Return an integer.
# Example Input
# Input 1:
# A = [1, 2, 3]
# B = [1, 2, 3]
# C = 2
# Input 2:
# A = [1, 2, 3]
# B = [1, 2, 3]
# C = 3

# Example Output
# Output 1:
# 1
# Output 2:
# 0
# Example Explanation
# Explanation 1:
# We can build hospitals at the villages 2 and 3.
# The citizens of above two villages doesn't need to travel.
# Citizents of village 1 can go to village 2, thus distance travelled = (3-2)*1 = 1.
# Explanation 2:
# All villages can have their own hospital.


def calculate_minimum_distance(d, p, h):
    minimum_distance = 0
    left_hospital = right_hospital == h.index(1)
    for i in range(len(d)):
        if i < right_hospital:
            minimum_distance += abs(d[right_hospital] - d[i]) * p[i]
        else:
            left_hospital = right_hospital
            right_hospital = h.index(1, right_hospital + 1)


def solve(A, B, C):
   
    mean_A = sum(A) / len(A)
    mean_B = sum(B) / len(B)
    hospitals = [0 for i in  range(len(A))]
    hospitals[-1] = 1

    # find variance for each element
    distance_variance = [mean_A - i for i in A]
    distance_variance = distance_variance[:-1]

    population_variance = [mean_A - i for i in B]  
    population_variance = population_variance[:-1]
      
    print(mean_A, mean_B)
    print(population_variance)
    if mean_A > mean_B:
        a_sort = sorted(distance_variance)
        for i in range(c-1):
            hospitals[a_sort.index(distance_variance[i])] = 1
    
    elif mean_A < mean_B:
        b_sort = sorted(population_variance)
        print(b_sort)
        for i in range(c-1):
            hospitals[b_sort.index(population_variance[i])] = 1

    else:
        a_sort = sorted(distance_variance)
        b_sort = sorted(population_variance)
        for i in range(c-1):
            if a_sort[i] < b_sort[i]:
                hospitals[a_sort.index(distance_variance[i])] = 1
            else:
                hospitals[b_sort.index(population_variance[i])] = 1
    print(hospitals)

a = [2, 3, 5, 8]
b = [10, 30, 2, 100]
c = 2
solve(a, b, c)