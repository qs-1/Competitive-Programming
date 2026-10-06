
# instead of max value for each weight, find min weight for each value, cuz thats smaller in constraint

# dp table of objects x values
n,wn = list(map(int, input().split()))

w=[]; v=[] #0 indexed
for _ in range(n):
    x,y=list(map(int, input().split()))
    w.append(x); v.append(y)

max_v = int(sum(v))

dp = [[float("inf")]*(max_v+1) for i in range(n+1)]

dp[0][0] = 0 # no objects, can make no value using no weight
for i in range(n+1): # dont take any to make val 0
    dp[i][0] = 0


for i in range(1,n+1):
    for j in range(1,max_v+1): #DP STORES MIN WEIGHT TO MAKE EXACTLY J (VALUE)
        
        # if cant make exactly j using this object then ans is making j without 
        # this new object (can be -1 incase we couldnt make it before either)
        # this obj has more val than possible using a combination with prev or taking this alone, so have to skip
        if v[i-1] > j: 
            dp[i][j] = dp[i-1][j]; continue

        #otherwise we might be able to make exactly j using JUST this new object, or maybe this and some previous ones
        #if not then it would be -inf, ie impossible to make exactly j using any combiantion of objs so far (till curr i)
        # !!! consider both cases, maybe skip will lead to a lower weight to make exactly j value
        dp[i][j] = min(dp[i-1][j],
                        w[i-1] + dp[i-1][j-v[i-1]])
    
# we know max weight should be <= wn
# find the highest value with the weight <= wn
# notice: What's the minimum weight to get exactly value j, having considered ALL N items?
# thats in the last row, so check that
for i in range(max_v,-1,-1):
    if dp[-1][i]<=wn:
        print(i)
        break