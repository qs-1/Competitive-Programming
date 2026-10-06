class FenwickTreeTuple:
    """(AI template) A Fenwick Tree that stores (count, sum) tuples."""
    def __init__(self, size):
        # Initialize the tree with tuples of (0, 0)
        self.tree = [(0, 0)] * (size + 1)

    def update(self, index, value_tuple):
        """Adds a (count, sum) tuple to the element at 'index'."""
        index += 1  # 1-based index
        delta_count, delta_sum = value_tuple
        
        while index < len(self.tree):
            current_count, current_sum = self.tree[index]
            # Add the deltas to the current node's tuple
            self.tree[index] = (current_count + delta_count, current_sum + delta_sum)
            index += index & (-index)

    def query(self, index):
        """Queries the prefix sum, returning a (total_count, total_sum) tuple."""
        index += 1  # 1-based index
        total_count, total_sum = 0, 0
        
        while index > 0:
            node_count, node_sum = self.tree[index]
            # Add the node's tuple to our running total
            total_count += node_count
            total_sum += node_sum
            index -= index & (-index)
            
        return (total_count, total_sum)

cases = int(input())
for _ in range(cases):
    r, c = list(map(int, input().split()))
    arr = []
    for __ in range(r):
        arr.append(list(map(int, input().split())))


    ans = 0
    for j in range(c):
        col_nums = [arr[i][j] for i in range(r)]
        u_col_nums = sorted(list(set(col_nums)))        
        comp = {v:i for i,v in enumerate(u_col_nums)}
        fw = FenwickTreeTuple(len(u_col_nums))

        sumsofar = 0
        cntsofar = 0
        for num in col_nums:
            numsle, sumle = fw.query(comp[num])    
            numsgt = cntsofar - numsle
            sumgt = sumsofar - sumle

            ans += (num*numsle - sumle) + (sumgt - num*numsgt)

            sumsofar+=num
            cntsofar+=1
            fw.update(comp[num], (1,num))
    print(ans)


# cases = int(input())
# for _ in range(cases):
#     r, c = list(map(int, input().split()))
#     arr = []
#     for __ in range(r):
#         arr.append(list(map(int, input().split())))

#     ans = 0
#     for j in range(c):
#         col = sorted([arr[i][j] for i in range(r)])

#         diff = 0
#         presum = 0
#         for k in range(r):
#             diff += col[k]*k - presum
#             presum += col[k]
#         ans += diff

#     print(ans)