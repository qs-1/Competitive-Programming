# Problem 5: Dutch National Flag Problem (3-way partitioning)
# Given an array with values {0,1,2}, sort them so that all 0s come first, 1s next, and 2s last.
# Good Problem for dynamic Partitioning? Justify.
"""
Yes, this is a good problem for dynamic partitioning.

We can sort the 3 different values by maintaining 3 partitions using pointers a,i,b:
# arr[0 to a-1] is all 0s
# arr[a to i-1] is all 1s
# arr[i to b] is unknown
# arr[b+1 to n-1] = all 2s

We process the array from left to right, placing all the 0s before the start of the a region
and placing all the 2s after the end of the b region. Doing so, we implicitly place the 1s in
the middle. 

Whenever we come accross a 2, we swap it with the value at b and decrement b (b--)
But we don't know what we just swapped it with, so we need to check current value again (skipping i++).

If it is a 0, we swap it with `a` (which is either current 0 itself incase of no 1s yet or 
start of 1s region). In either case, we have the 0 placed where it should be and so we move on (i++)

This partitioning is done in one pass and takes constant space, unlike the naive linear space approach.
"""

arr = list(map(int, input().split()))
n = len(arr)

a = 0
b = n-1
i=0
while i<=b:
    #will either be swapped with itself, or with a 1 always (start of 1s region)
    if arr[i] == 0: 
        arr[i], arr[a] = arr[a], arr[i]
        a+=1
        i+=1

    #move 2 to the end, but we don't know what was swapped back at this place
    #unlike for 0 case where we knew due to the invariant and left right processing
    #that to the left of that 0 we could only have 0s or 1s
    #and so we need to check the swapped number at ith again, dont increment i due to this
    elif arr[i] == 2: 
        arr[i], arr[b] = arr[b], arr[i]
        b-=1

    else:    
        i+=1

print(*arr)