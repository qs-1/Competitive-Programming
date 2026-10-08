# Problem 3: Move all negative numbers before positive numbers.
# Good Problem for dynamic Partitioning? Justify.
"""
No. (exact same idea as with even odd separation Q2)
We only need a single partition to separate negatives and positives, 
and no pivot is needed either since we only check sign (< 0).
Recursion is useless, we already have the separation after one partition.
"""

array = list(map(int, input().split())) # -3 8 -5 12 -7 6 4
n = len(array)

# #lomuto style partitioning, O(1) space, unstable
# ────────────────────────────────────────────────
q = 0
for i in range(n):
    if array[i] < 0: #negative, swap with q
        array[q], array[i] = array[i], array[q]
        q+=1
print(*array)


# # O(n) space, stable
# ────────────────────
# negatives = []
# positives = []
# for x in array:
#     if x < 0: negatives.append(x);continue
#     positives.append(x)
# ans = negatives+positives
# print(*ans)


# # nlogn time and n space oneliner, stable
# ─────────────────────────────────────────
# array.sort(key = lambda x: x >= 0)
# print(*array)


# # quicksort, works but is pointless since after first parition, we already have 
# # all negatives to left and positives to right, recurring further does not help in any way
# ─────────────────────────────────────────────────────────────────────────────────────
# def quicksort(array):
#     arr = array[::]
#     def helper(i,j):
#         if i>=j: return
#         def partition(l,r):
#             pivot = l
#             q = l+1
#             for i in range(l+1, r+1): #after pivot, including end
#                 if arr[i] < 0: #move negatives before pivot
#                     arr[i], arr[q] = arr[q], arr[i]
#                     q+=1
#             q-=1
#             arr[pivot], arr[q] = arr[q], arr[pivot]
#             return q
#         p = partition(i,j) # move i to its correct position
#         # recursively do it for left and right of p
#         helper(i,p-1)
#         helper(p+1,j)
#     i=0
#     j=len(arr)-1
#     helper(i,j)
#     return arr
# arr = quicksort(array)
# print(*arr)