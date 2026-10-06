"""A. Stone Game
time limit per test
2 seconds
memory limit per test
256 megabytes

Polycarp is playing a new computer game. This game has n
stones in a row. The stone on the position i has integer power ai

. The powers of all stones are distinct.

Each turn Polycarp can destroy either stone on the first position or stone on the last position (in other words, either the leftmost or the rightmost stone). When Polycarp destroys the stone it does not exist any more.

Now, Polycarp wants two achievements. He gets them if he destroys the stone with the least power and the stone with the greatest power. Help Polycarp find out what is the minimum number of moves he should make in order to achieve his goal.

For example, if n=5
and a=[1,5,4,3,2]

, then Polycarp could make the following moves:

    Destroy the leftmost stone. After this move a=[5,4,3,2]

;
Destroy the rightmost stone. After this move a=[5,4,3]
;
Destroy the leftmost stone. After this move a=[4,3]

    . Polycarp destroyed the stones with the greatest and least power, so he can end the game. 

Please note that in the example above, you can complete the game in two steps. For example:

    Destroy the leftmost stone. After this move a=[5,4,3,2]

;
Destroy the leftmost stone. After this move a=[4,3,2]

    . Polycarp destroyed the stones with the greatest and least power, so he can end the game. 

Input

The first line contains an integer t
(1≤t≤100). Then t

test cases follow.

The first line of each test case contains one integer n
(2≤n≤100

) — the number of stones.

The second line contains n
distinct integers a1,a2,…,an (1≤ai≤n

) — the power of the stones.
Output

For each test case, output the minimum number of moves required to destroy the stones with the greatest and the lowest power.
Example
Input
Copy

5
5
1 5 4 3 2
8
2 1 3 4 5 6 8 7
8
4 2 3 1 8 6 7 5
4
3 4 2 1
4
2 3 1 4

Output
Copy

2
4
5
3
2

1538A - Stone Game

If we want to destroy the largest and smallest stone, then there are only four options:

    Destroy the stones on the left until we destroy the smallest stone. Then destroy the stones on the right, until we destroy the largest stone.
    Destroy the stones on the right until we destroy the smallest stone. Then destroy the stones on the left, until we destroy the largest stone.
    Destroy the stones on the left until we destroy both stones.
    Destroy the stones on the right until we destroy both stones.

        You need to check all four options and choose the minimum answer."""

cases = int(input())
for i in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    
    hi = max(arr)
    lo = min(arr)
    
    for j in range(n):
        if arr[j] == hi:
            hi_idx = j
        
        elif arr[j] == lo:
            lo_idx = j
        
    #smallest from left
    one = (lo_idx + 1) + (n-hi_idx)

    #smallest from right
    two = (hi_idx + 1) + (n-lo_idx)

    #both frm right
    thr = max(lo_idx, hi_idx) + 1 #only rightmost matters

    #both frm left
    fou = n-min(lo_idx,hi_idx) #min since the leftmost only matters

    print(min(one,two,thr, fou))