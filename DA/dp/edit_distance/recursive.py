#making a into b
def edist_recur(a,b):
    alen=len(a)
    blen=len(b)
    
    memo={}
    def helper(i,j):
        if (i,j) in memo:
            return memo[(i,j)]
            
        if j == blen:
            #was a completed? all chars used? ie i=len(a)?
            #if not delete them
            memo[(i, j)] = alen - i
            return alen - i
            
        if i == alen:
            #reached end of a, was b made? or some left to match?
            #if left then insert those
            memo[(i, j)] = blen - j
            return blen - j

        maintain = float("inf")
        if a[i]==b[j]: 
            maintain = helper(i+1,j+1) 
        insert =  1+helper(i,j+1) #a pointer same, but j matched go to next j
        remove =  1+helper(i+1,j) #check next ith, j to be matched still
        replace = 1+helper(i+1,j+1) #matched, next for both

        best = min(maintain,
                   insert,
                   remove,
                   replace)

        memo[(i,j)] = best
        return best


    cost = helper(0, 0)
    transcript = []
    i=0
    j = 0
    while i < alen or j < blen:
        if i == alen:
            transcript.append(f"Insert {b[j]}")
            j += 1
            continue
        
        if j == blen:
            transcript.append(f"Delete {a[i]}")
            i += 1
            continue
        
        curr = memo[(i, j)]

        if a[i] == b[j]:
            if curr == memo[(i+1, j+1)]:
                transcript.append(f"Match {a[i]}")
                i += 1
                j += 1
                continue
        
        if curr == 1 + memo[(i+1, j+1)]:
            transcript.append(f"Sub {a[i]}->{b[j]}")
            i += 1
            j += 1
            continue
            
        if curr == 1 + memo[(i, j+1)]:
            transcript.append(f"Insert {b[j]}")
            j += 1
            continue
            
        transcript.append(f"Delete {a[i]}")
        i += 1

    return cost, transcript

