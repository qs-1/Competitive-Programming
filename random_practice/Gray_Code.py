n = int(input())
for i in range(2**n):
    print(f"{(i >> 1) ^ i:0{n}b}")

# n = int(input())
# ans = [
#        "0","1"
#         ]

# def hams(nth):
#     global ans
#     if nth == n:
#         return

#     temp = []
#     for ham in ans:
#         temp.append("0" + ham)
#     for ham in ans[::-1]:
#         temp.append("1" + ham)
#     ans=temp
#     hams(nth+1)

# hams(1)
# for r in ans: print(r,end='');print()

