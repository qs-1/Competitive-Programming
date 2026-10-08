# brute force
def solve_brute_force(arr):
    for i in range(3, len(arr), 2):
        if arr[i] < arr[i-2]:
            return False
    return True

# div & conq
def solve_divide_and_conquer(arr):
    def dq(i=0,j=None):
        if j is None:
            j = len(arr)-1
        if j-i == 1:
            return (True,arr[j])
        m = (i+j) // 2
        left = dq(i,m)
        right = dq(m+1,j)
        return (left[0] and right[0] and left[1]<=right[1], right[1])
    return dq()[0]

# using queue
from collections import deque
def solve_queue(arr):
    queue = deque(arr[1::2])
    prev = None if len(queue)==0 else queue.popleft()
    while queue:
        n = queue.popleft()
        if n<prev:
            return False
        prev = n
    return True

# linked list
class ll:
    def __init__(self, idx_val):
        self.idx_val = idx_val
        self.next = None

def solve_linked_list(arr):
    head = None
    for i in range(1,len(arr),2):
        if not head: head = ll(arr[i]); temp = head; continue
        temp.next = ll(arr[i])
        temp = temp.next
    prev = head
    curr = head.next
    while curr:
        if curr.idx_val < prev.idx_val:
            return False
        curr = curr.next
    return True