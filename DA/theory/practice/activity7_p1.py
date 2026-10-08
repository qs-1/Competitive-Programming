def mini(n,arr):
    i = 0
    j = len(arr[0])-1
    def helper(i,j):
        if i==n-1 or j==0: #last row or first column
            return arr[i][j]
        
        if arr[i][j] != None: # memoization, return if found already
            return arr[i][j]

        #otherwise keep making calls to get to base case
        bottom = helper(i+1,j)
        bottomleft = helper(i+1,j-1)

        #now we either have the values bottom and bottom bottom directly after base case
        #or either we returned from some other call within which gave us the 
        # i j-1th and i+1 j-1th values
        
        #place min of them in current now that we have the needed for comparison
        arr[i][j] = min(bottom, bottomleft)

        #return this (since we made this contract in base case?
        #and also since we need this as the bottom or bottom value in
        #some other's helper calls)
        return arr[i][j]
    helper(i,j)

    #now call for first row to fill the empty upper half triangle
    for k in range(n):
        helper(0,k)

n = int(input())
arr = []
for _ in range(n):
    row = input().split()
    arr.append([int(x) if x != '-' else None for x in row])

mini(n,arr)

for row in arr:
    print(*row)
