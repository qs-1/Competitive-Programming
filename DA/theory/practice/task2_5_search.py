"""
Problem Statement:
Given an array of n values/records A1, A2, A3, ..., An such that
A1 <= A2 <= A3 <= ... <= An and a target search value T,

Step 1: Set L to 1 and R to n (Am is the middle element)
Step 2: If L > R, target not found
Step 3: If Am < T, set L to m + 1, go to Step 2
Step 4: If Am > T, set R to m - 1, go to Step 2
Step 5: If Am == T, return m

Practice Task 2: Design an iterative algorithm to solve the above problem.
Practice Task 3: Design a retcursive algorithm to solve the above problem.
Practice Task 4: Find the recurrence equation for the recursive approach.
Practice Task 5: Solve the recurrence equation above via iteration/substitution method to
find a closed form of the equation.
"""
#task 2
def solve_iter(n,arr):
    l = 0
    r = len(arr)-1
    while l<=r:
        m = (l+r)//2

        if arr[m] == n:
            return m
        if arr[m]>n:
            r = m-1
        else:
            l = m+1
    return -1

n = int(input())
arr = list(map(int, input().split()))
print(solve_iter(n,arr))

#task 3
def solve_recur(n,arr):
    def bs(l=0,r=len(arr)-1):
        if l>r:
            return -1
        
        m = (l+r)//2

        if arr[m] == n:
            return m
        if arr[m]>n:
            r = m-1
        else:
            l = m+1
        return bs(l,r)
    return bs()

# n = int(input())
# arr = list(map(int, input().split()))
print(solve_recur(n,arr))

#task 4
# T(n) = T(n/2) + 1

#task 5
# T(n) = log₂n