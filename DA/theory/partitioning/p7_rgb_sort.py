# Problem 7: Color Sort / RGB Partitioning
# Given a dataset of colors (Red, Green, Blue), partition it into 3 groups dynamically.
# Good Problem for dynamic Partitioning? Justify.
"""
Yes, this is a good problem for dynamic partitioning because it is identical
to the Dutch National Flag problem (Problem 5).

We can map the colors to numbers and apply the
same 3 way partitioning.

# arr[0 to a-1] is all 'R's (like 0s)
# arr[a to i-1] is all 'G's (like 1s)
# arr[i to b] is unknown
# arr[b+1 to n-1] = all 'B's (like 2s)

We iterate through the array with a pointer `i`. If we find an 'R', we swap it
to the 'R' section. If we find a 'B', we swap it to the 'B' section. The 'G's
implicitly be placed in the middle due to this logic.

This sorts the colors in a single pass and with constant space (O(1)).
"""

arr = input().split()
n = len(arr)

a = 0
b = n-1
i=0
while i<=b:
    if arr[i] == 'R':
        arr[i], arr[a] = arr[a], arr[i]
        a+=1
        i+=1
    elif arr[i] == 'B':
        arr[i], arr[b] = arr[b], arr[i]
        b-=1
    else:
        i+=1

print(*arr)