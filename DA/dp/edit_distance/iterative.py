def edist_iter(a, b):
    alen = len(a)
    blen = len(b)
    
    dp = [[0]*(blen+1) for _ in range(alen+1)]

    # base cases
    for j in range(blen+1):
        dp[0][j] = j
    for i in range(alen+1):
        dp[i][0] = i

    for i in range(1, alen+1):
        for j in range(1, blen+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],    # insert
                                   dp[i-1][j-1],  # replace
                                   dp[i-1][j])    # delete

    # backtracking from end to get the edit transcript
    i, j = alen, blen
    transcript = []
    while i > 0 or j > 0:
        # Mainstain, diagonal move with no cost
        if i > 0 and j > 0 and a[i-1] == b[j-1]:
            transcript.append(f"Match '{a[i-1]}'")
            i -= 1
            j -= 1
        
        # substitution, diagonal move with cost 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + 1:
            transcript.append(f"Substitute '{a[i-1]}' with '{b[j-1]}'")
            i -= 1
            j -= 1
            
        # insertion, horizontal move from left wit cost 1
        elif j > 0 and dp[i][j] == dp[i][j-1] + 1:
            transcript.append(f"Insert '{b[j-1]}'")
            j -= 1
            
        # deletion, vertical move from top and cost 1
        elif i > 0 and dp[i][j] == dp[i-1][j] + 1:
            transcript.append(f"Delete '{a[i-1]}'")
            i -= 1

    # we got the transcript from end to start,
    # so reverse the list to get it in correct order
    return dp[alen][blen], transcript[::-1]

