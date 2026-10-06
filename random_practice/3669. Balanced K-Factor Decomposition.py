from typing import List
class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        best = [] # k factors that multiply to n with least diff between em
        bestdiff = float("inf")
        def recur(prev, n, k, facts):
            nonlocal best, bestdiff
            if k==1: # last num reached, this itself is a factor
                # k is the last and the biggest right?
                diff = n-facts[0]
                if diff<bestdiff:
                    best = facts + [n]
                return

            # start from prev to ensure non decreasing order of k factors 
            # (no different permutations of same factors this way)            
            for i in range(prev, int(n**(0.5))+1):
                if n%i==0: # fact found
                    recur(i, n//i, k-1, facts+[i])

        recur(1,n,k,[])
        return best