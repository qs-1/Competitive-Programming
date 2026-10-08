# brute force
def solve_brute_force(arr):
    double_factorials = [None]*len(arr)
    for i in range(len(arr)):
        df = 1
        num = arr[i]
        for j in range(1,num+1):
            if (num^j)&1==0: df*=j
        double_factorials[i] = df
    return double_factorials

# divide & conquer
def solve_divide_and_conquer(arr):
    double_factorials = [None]*len(arr)
    memo = {}
    def dq(arr,i=0,j=None):
        if j is None:
            j = len(arr)-1
        if i == j:
            if arr[i] in memo:
                double_factorials[i] = memo[arr[i]]
                return
            df = 1
            for k in range(1,arr[i]+1):
                if (k^arr[i])&1 == 0: df*=k
            memo[arr[i]] = df
            double_factorials[i] = df
            return
        m = (i+j) // 2
        dq(arr,i,m)
        dq(arr,m+1,j)
    dq(arr)
    return double_factorials

# stack only with memoization
def solve_stack_memo(stack):
    result = []
    memo = {}
    stack = stack.copy()
    while stack:
        num = stack.pop()
        if num in memo: df = memo[num]
        else:
            df = 1
            for j in range(1, num+1):
                if (num^j)&1 == 0: df*=j
            memo[num] = df
        result.append(df)
    double_factorials = []
    while result:
        double_factorials.append(result.pop())
    return double_factorials

# div & conq with explicit stack
def solve_divconq_explicit_stack(arr):
    i = 0
    j = len(arr)-1
    callstack = [(i,j)]
    memo = {}
    double_factorials = [None]*len(arr)
    while callstack:
        l,r = callstack.pop()
        if l!=r:
            m = (l+r) // 2
            callstack.append((l,  m))
            callstack.append((m+1,r))
            continue
        if arr[l] in memo: double_factorials[l] = memo[arr[l]]; continue
        df = 1
        num = arr[l]
        for x in range(1,num+1):
            if (num^x)&1 == 0:
                df*=x
        memo[arr[l]] = df
        double_factorials[l] = df
    return double_factorials