n,k=list(map(int, input().split()))
arr = list(map(int, input().split()))
kth=arr[k-1]
print(sum(1 for num in arr if num >= kth and num>0))