"""A. Hossam and Combinatorics
time limit per test
2 seconds
memory limit per test
256 megabytes

Hossam woke up bored, so he decided to create an interesting array with his friend Hazem.

Now, they have an array a
of n positive integers, Hossam will choose a number ai and Hazem will choose a number aj

.

Count the number of interesting pairs (ai,aj)

that meet all the following conditions:

    1≤i,j≤n

;
i≠j
;
The absolute difference |ai−aj|
must be equal to the maximum absolute difference over all the pairs in the array. More formally, |ai−aj|=max1≤p,q≤n|ap−aq|

    .

Input

The input consists of multiple test cases. The first line contains a single integer t
(1≤t≤100

), which denotes the number of test cases. Description of the test cases follows.

The first line of each test case contains an integer n
(2≤n≤105

).

The second line of each test case contains n
integers a1,a2,…,an (1≤ai≤105

).

It is guaranteed that the sum of n
over all test cases does not exceed 105

.
Output

For each test case print an integer — the number of interesting pairs (ai,aj)

.
Example
Input
Copy

2
5
6 2 3 8 1
6
7 2 8 3 2 10

Output
Copy

2
4

Note

In the first example, the two ways are:

    Hossam chooses the fourth number 8

and Hazem chooses the fifth number 1
.
Hossam chooses the fifth number 1
and Hazem chooses the fourth number 8

    . 

In the second example, the four ways are:

    Hossam chooses the second number 2

and Hazem chooses the sixth number 10
.
Hossam chooses the sixth number 10
and Hazem chooses the second number 2
.
Hossam chooses the fifth number 2
and Hazem chooses the sixth number 10
.
Hossam chooses the sixth number 10
and Hazem chooses the fifth number 2. """

cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))

    diff = abs(max(arr) - min(arr))
    if diff == 0: print(n*(n-1)); continue
    print(arr.count(max(arr))*arr.count(min(arr))*2)