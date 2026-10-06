import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1,1<<32)
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    s = input().strip()
    n = len(s)

    stack = [-1]
    maxx = 0
    same = 1
    for i,v in enumerate(s):
        if v=="(":
            stack.append(i)
        else:
            stack.pop()
            if stack:
                # after popping, top of stack points to the closest unmatched bracket (or a ')', either way we treat it as the start of our sequence)
                # and since this is 1 before our start of our valid sequence, and indices are 0 based, the math works out 
                currlen = i - stack[-1] 
                if maxx<currlen:
                    same = 1
                    maxx = currlen
                elif maxx==currlen:
                    same+=1
            else:
                stack.append(i)

    print(maxx,same)


# # v2

# import sys
# import math
# import random
# input = sys.stdin.readline
# #hsh = random.randint(1,1<<32)
# from collections import defaultdict, Counter

# s = input().strip()
# n = len(s)

# stack = []
# maxx = 0
# same = 1
# last_invalid = -1
# for i,v in enumerate(s):
#     if v=="(":
#         stack.append(i)
#     else:
#         if not stack:
#             last_invalid = i
#         else:
#             stack.pop()
#             if not stack:
#                 currlen = i - last_invalid
#             else:
#                 currlen = i - stack[-1] 

#             if maxx<currlen:
#                 same = 1
#                 maxx = currlen
#             elif maxx==currlen:
#                 same+=1

# print(maxx,same)

# # v3 (bad)
# import sys
# import math
# import random
# input = sys.stdin.readline
# #hsh = random.randint(1,1<<32)
# from collections import defaultdict, Counter

# cases = int(input())
# for _ in range(cases):
#     s = input().strip()
#     n = len(s)

#     maxx = -1
#     same = 1

#     last_invalid = -1
#     stack = []
#     j = 0

#     while j<n:
#         curr = s[j]
#         if curr == ")" and not stack:
#             last_invalid = j
#             longest = 0
#             j+=1
#             continue

#         if curr == "(":
#             stack.append(j) #stack has indices of ('s
#         else:
#             stack.pop()
#             if stack:
#                 longest = j - stack[-1]

#             else: #end of a valid seq like ()
#                 #might be possible to extend a valid before it [prev] (()) -> [curr] ()
#                 longest = j - last_invalid

#             if maxx == longest:
#                 same+=1
#             elif maxx<longest:
#                 same=1
#             maxx = max(maxx,longest)
#         j+=1
        
#     if maxx!=-1:
#         print(maxx, same)
#     else:
#         print(0,1)