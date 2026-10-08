# Problem 2: Rearrange array elements so that all even numbers come before all odd numbers.
# Good Problem for dynamic Partitioning? Justify.
"""
No.

We only need a single partition to separate evens and odds, and no pivot 
is needed either since we only look at parity. Recurrance is a waste 
since after the first partition, we already have the separation.
"""
array = list(map(int, input().split())) # 3 8 5 12 7 6 4
n = len(array)

# #lomuto style partitioning, O(1) space, unstable
# ────────────────────────────────────────────────
q = 0
for i in range(n):
    if array[i]&1 != 1: #even, swap with q
        array[q], array[i] = array[i], array[q]
        q+=1
print(*array)


# # O(n) space, stable
# ────────────────────
# evens = []
# odds = []
# for x in array:
#     if x&1: odds.append(x);continue
#     evens.append(x)
# ans = evens+odds
# print(*ans)


# # nlogn time and n space oneliner, stable
# ─────────────────────────────────────────
# array.sort(key = lambda x: x&1)
# print(*array)


# quicksort, works but is pointless since after first parition, we already have 
# all evens to left and all odds to right, recurring further does not help in any way
# ─────────────────────────────────────────────────────────────────────────────────────
# import random
# def quicksort(array):
#     arr = array[::]

#     def helper(i,j):
#         if i>=j: return

#         def partition(l,r):
#             # put a random num at pivot
#             random_idx = random.randint(l, r)
#             arr[l], arr[random_idx] = arr[random_idx], arr[l]
#             pivot = l
#             q = l+1
#             for i in range(l+1, r+1): #after pivot, including end
#                 if arr[i]&1!=1: #move evens before pivot
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

