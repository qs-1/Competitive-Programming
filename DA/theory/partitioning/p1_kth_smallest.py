# # Find the kth smallest element in an unsorted array
# Problem 1: Find the kth smallest element in an unsorted array (Quick Select).
# Good Problem for dynamic Partitioning? Justify.
# Perform partition like in Quicksort.
# If pivot index == k → return pivot.
# Else, recursively partition the relevant half.

"""
Yes, this is a good problem for dynamic partitioning.
The important part about Quickselect algorithm is the partition function, which rearranges the array
around a pivot. After partitioning, the pivot is in its final sorted position. This position tells us
whether the kth smallest element is the pivot itself, in the subarray to the left of the pivot, 
or in the subarray to the right.

We can then discard the half that we know does not contain our element. 
This dynamic partitioning of the array at each step is what allows the algorithm to achieve an average case
linear time complexity, which is much better than sorting the entire array.
"""

# quickselect -> kth smallest in n (n^2 near impossible with random pivot)
# since we'd have to pick the smallest each time, porbability of this is very low:
# P = (n/2) * ((n-1)/2) * ((n-2)/2) * ... * (2/2)  =  2^(n-1) / n!

import random

# Hoare-style partition with changing pivot
# https://www.youtube.com/watch?v=ZAXSFph_L-A
def quickselect(k,array):
    k-=1 #0 based
    arr=array[::]
    n = len(arr)

    def partition(l,r):
        # randomize pivot to avoid O(n^2) worst case
        random_idx = random.randint(l, r)
        arr[l], arr[random_idx] = arr[random_idx], arr[l]
        
        while l<r:
            if arr[l] >= arr[l+1]:
                arr[l], arr[l+1] = arr[l+1], arr[l]
                l+=1

            elif arr[r] > arr[l]:
                r-=1

            else:
                # before swap:
                #   arr[l] < arr[l+1]
                #   arr[r] <= arr[l]
                # so: arr[r] <= arr[l] < arr[l+1]
                
                # swap arr[r] and arr[l+1]

                # after swap:
                #   arr[l] >= arr[l+1]
                #   arr[r] > arr[l]
                # so: arr[l+1] <= arr[l] < arr[r]

                # now on next iteration, first condition will always be true
                arr[r], arr[l+1] = arr[l+1], arr[r]
        return l

    i=0
    j=n-1
    while i<=j:
        pivot = partition(i,j)
        
        if pivot==k:
            return arr[pivot]
        
        elif pivot<k:
            i=pivot+1

        else:
            j=pivot-1

k = int(input())
arr = list(map(int, input().split()))
ans = quickselect(k,arr)
print(ans)



# # CAR hoare partition
# def quickselect(k,array):
#     k-=1 #0 based
#     arr = array[::]
#     n = len(arr)

#     def hoare(l,r):
#         # randomize pivot to avoid O(n^2) worst case
#         random_idx = random.randint(l, r)
#         arr[l], arr[random_idx] = arr[random_idx], arr[l]
#         pivot = arr[l]

#         while True:
#             while arr[l] < pivot: #left smaller
#                 l+=1

#             while arr[r] > pivot: #right bigger
#                 r-=1

#             if l>=r:
#                 return r
            
#             arr[l], arr[r] = arr[r], arr[l]
#             l+=1
#             r-=1

#     i=0
#     j=n-1
#     while i<j:
#         split = hoare(i,j)

#         if k<=split: 
#             j = split # left half
#         else:
#             i = split+1 # right half

#     return arr[i] # window length 1, found kth

# k = int(input())
# arr = list(map(int, input().split()))
# ans = quickselect(k,arr)
# print(ans)



# # lomuto partition
# def quickselect(k,array):
#     arr = array[::]
#     n = len(arr)
#     k-=1 #0 based

#     def lomuto(l,r):
#         # randomize pivot to avoid O(n^2) worst case
#         random_idx = random.randint(l, r)
#         arr[r], arr[random_idx] = arr[random_idx], arr[r]
#         pivot = arr[r]
#         q = l
#         for z in range(l, r):
#             if arr[z] < pivot:
#                 arr[q], arr[z] = arr[z], arr[q]
#                 q += 1
#         arr[q], arr[r] = arr[r], arr[q]
#         return q

#     i = 0
#     j = n-1
#     while i<j:
#         pivot = lomuto(i,j)

#         if k < pivot:
#             j=pivot-1
#         elif k > pivot:
#             i=pivot+1
#         else:
#             i = k
#             break

#     return arr[i]

# k = int(input())
# arr = list(map(int, input().split()))
# ans = quickselect(k,arr)
# print(ans)


# def kthsmall(k,arr):
#     i = 0
#     j = len(arr)-1
    
#     def helper(i,j):
#         if j-i+1 <= k: #block of atmost len k
#             return sorted(arr[i:j+1])

#         m=(i+j)//2
#         left = helper(i,m)
#         right  = helper(m+1,j)

#         # returned left right arrays can have len <= k
#         # sort and return atmost len k block
#         return sorted(left+right)[:k]
    
#     return helper(i,j)[-1]

# k = int(input())
# arr = list(map(int, input().split()))
# ans = kthsmall(k,arr)
# print(ans)



# import heapq
# def kthsmallheap(k,arr):
#     i = 0
#     j = len(arr)-1
#     newarr = [-num for num in arr]

#     def helper(i,j):
#         if j-i+1 <= k: #block of atmost len k
#             temp = newarr[i:j+1]
#             heapq.heapify(temp)
#             return temp

#         m=(i+j)//2
#         left = helper(i,m)
#         right  = helper(m+1,j)

#         # returned left right arrays can have len <= k
#         # merge into one heap
#         merged = left + right
#         heapq.heapify(merged)

#         # pop extras
#         mergedlen = len(merged)
#         while mergedlen > k:
#             heapq.heappop(merged)
#             mergedlen-=1

#         return merged # return size <= k heap
    
#     # ans now has max heap of k smallest numbers, so top of this is kth smallest 
#     ans = helper(i,j)
#     return -ans[0]


# k = int(input())
# arr = list(map(int, input().split()))
# ans = kthsmallheap(k,arr)
# print(ans)

# # nlogk, but can be n without recursion ony heapifying till size k returning max