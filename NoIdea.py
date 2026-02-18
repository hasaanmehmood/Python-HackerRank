# There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
# Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

# Constraints
# 1 <= n  <= 10^5
# 1 <= m <= 10^5
# 1 <= Any integer in input <= 10^9

# Input Format
# The first line contains integers  and  separated by a space.
# The second line contains  integers, the elements of the array.
# The third and fourth lines contain  integers,  and , respectively.

# Output Format
# Output a single integer, your total happiness.

# Read n, m
n, m = map(int, input().split())

# Basic range checks for n, m
if not (1 <= n <= 10**5 and 1 <= m <= 10**5):
    raise ValueError("n or m out of allowed range")

# Read arr and validate size
arr = list(map(int, input().split()))
if len(arr) != n:
    raise ValueError(f"Expected {n} elements in arr, got {len(arr)}")

# Range check for arr values
if any(x < 1 or x > 10**9 for x in arr):
    raise ValueError("arr contains value out of allowed range")

# Read A and B as lists first so we can validate count == m
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

if len(A_list) != m:
    raise ValueError(f"Expected {m} elements for A, got {len(A_list)}")
if len(B_list) != m:
    raise ValueError(f"Expected {m} elements for B, got {len(B_list)}")

# Range checks for A and B values
if any(x < 1 or x > 10**9 for x in A_list):
    raise ValueError("A contains value out of allowed range")
if any(x < 1 or x > 10**9 for x in B_list):
    raise ValueError("B contains value out of allowed range")

# Convert to sets for fast membership checks
A = set(A_list)
B = set(B_list)

happiness = 0
for num in arr:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1

print(happiness)