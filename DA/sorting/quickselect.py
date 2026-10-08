import random

def quickselect(k,array,largest = False):
    arr = array[::]
    n = len(arr)
    k-=1 #0 based
    if largest:
        k = n - k - 1  # kth largest is (n-k-1)th smallest

    def hoare(l,r):
        # randomize pivot to avoid O(n^2) worst case
        random_idx = random.randint(l, r)
        arr[l], arr[random_idx] = arr[random_idx], arr[l]
        pivot = arr[l]

        while True:
            while arr[l] < pivot: #left smaller
                l+=1

            while arr[r] > pivot: #right bigger
                r-=1

            if l>=r:
                return r
            
            arr[l], arr[r] = arr[r], arr[l]
            l+=1
            r-=1

    i=0
    j=n-1
    while i<j:
        split = hoare(i,j)

        if k<=split: 
            j = split # left half
        else:
            i = split+1 # right half

    return arr[i] # window length 1, found kth