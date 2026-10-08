# Problem 4: Find key element in shuffled dataset where each step partitions array dynamically into two halves.
# Good Problem for dynamic Partitioning? Justify.
"""
No.

Partitioning isn't really helpful here, even if we partition, we
have no information about which half the key is in, so we'd have to 
check both halves anyway. A linear search makes more sense here.

Wouldve been helpful if we were asked kth smallest or largest because
in that case after moving the pivot to its correct position, we could
prune the search space, we'd know which half the kth lies in because
left of pivot are smaller than it and right are larger.
"""
key = int(input())
arr = list(map(int, input().split()))
n = len(arr)

# linear search O(n)
found = False
for i in range(n):
    if arr[i] == key:
        found = True
        break
print(found)

# # oneliner
# print(key in arr)