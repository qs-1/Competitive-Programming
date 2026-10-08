# Problem 6: Determine if a given set can be partitioned into two subsets with equal sum.
# Good Problem for dynamic Partitioning? Justify.
"""
No, this is not a good problem for dynamic partitioning in the quickselect sense. We aren't rearranging array elements inplace based
on some property but instead try different combinations to check whether some leads to equal sum split.

This is usually solved using dp or recursion+memoization. Below is a recursive solution.
"""

arr = list(map(int, input().split())) #[1, 5, 11, 5]

def subsetsum(arr):
    total = sum(arr)
    n = len(arr)

    if total%2!=0: return False

    memo={}
    def helper(currsum, i=0, path=None):
        key = (currsum,i)
        if key in memo:
            return memo[key]
    
        if path == None:
            path = []

        if currsum == total-currsum:
            memo[key] = path
            return path

        if i==n:
            memo[key] = None
            return None
        
        take = helper(currsum+arr[i], i+1, path+[i])
        if take:
            memo[(currsum,i)] = take
            return take

        skip = helper(currsum, i+1, path)
        memo[(currsum,i)] = skip
        return skip

    indices = helper(0)
    if indices==None: return False # no valid split found
    
    a = [arr[i] for i in indices]
    indset = set(indices)
    b = [arr[i] for i in range(n) if i not in indset]
    return a,b
        
ans = subsetsum(arr)
if not ans:
    print(-1)
else:
    a,b=ans
    print(*a)
    print(*b)