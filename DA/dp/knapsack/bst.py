class Node:
    def __init__(self, weight, value, idx):
        self.weight = weight
        self.value = value
        self.idx = idx
        self.left = None
        self.right = None

class knapBST:
    def __init__(self):
        self.root = None

    def insert(self, weight, value, idx):
        if self.root is None:
            self.root = Node(weight, value, idx)
        else:
            self.recursively_insert(self.root, weight, value, idx)

    def recursively_insert(self, current, w, v, idx):
        # left is lighter and right is heavier
        if w < current.weight:
            if current.left is None:
                current.left = Node(w, v, idx)
            else:
                self.recursively_insert(current.left, w, v, idx)
        else:
            if current.right is None:
                current.right = Node(w, v, idx)
            else:
                self.recursively_insert(current.right, w, v, idx)


def solve(n, wn, bst_root):
    dp = [[0]*(wn+1) for i in range(n+1)]
    curr_idx = [0] 

    def helper(node): # solve each for each dp in ascending order, using inorder traversal
        if node is None:
            return
        
        # left
        helper(node.left)

        curr_idx[0] += 1
        i = curr_idx[0]
        w = node.weight
        v = node.value
        for j in range(1, wn+1):
            print(f"First {i} objects, Weight limit {j}")

            if w > j: # must skip
                dp[i][j] = dp[i-1][j]
                print(f"Exclusion of object {i} gives value: {dp[i-1][j]}")
                print()
                continue

            # take best of take/skip
            skip = dp[i-1][j]
            take = v + dp[i-1][j-w]
            
            if skip > take:
                best = skip
                print(f"Exclusion of object {i} gives value: {best}")
            else:
                best = take
                print(f"Inclusion of object {i} gives value: {best}")
            
            dp[i][j] = best
            print()

        # right
        helper(node.right)

    helper(bst_root)
    return dp[n][wn]

n, wn = list(map(int, input().split()))
bst=knapBST()
for i in range(n):
    x, y = list(map(int, input().split()))
    bst.insert(x,y,i)

ans = solve(n, wn, bst.root)
print(ans)

