# quicksort (lomuto)
def quicksort(array):
    arr = array[::]

    def helper(i,j):
        if i>=j: return

        def partition(l,r):
            pivot = l
            q = l+1
            for i in range(l+1, r+1): #after pivot, including end
                if arr[i] < arr[pivot]:
                    arr[i], arr[q] = arr[q], arr[i]
                    q+=1
            q-=1
            arr[pivot], arr[q] = arr[q], arr[pivot]
            return q

        p = partition(i,j) # move i to its correct position
        # recursively do it for left and right of p
        helper(i,p-1)
        helper(p+1,j)

    i=0
    j=len(arr)-1
    helper(i,j)
    return arr

# # Hoare-style partition, but with a changing pivot
# # https://www.youtube.com/watch?v=ZAXSFph_L-A
# def quickselect(k,array):
#     k-=1 #0 based
#     arr=array[::]
#     n = len(arr)

#     def partition(l,r): 

#         while l<r:
#             if arr[l] > arr[l+1]:
#                 arr[l], arr[l+1] = arr[l+1], arr[l]
#                 l+=1

#             elif arr[r] > arr[l]:
#                 r-=1

#             else:
#                 arr[r], arr[l+1] = arr[l+1], arr[r]
#         return l

#     i=0
#     j=n-1
#     while i<=j:
#         pivot = partition(i,j)
        
#         if pivot==k:
#             return arr[pivot]
        
#         elif pivot<k:
#             i=pivot+1

#         else:
#             j=pivot-1