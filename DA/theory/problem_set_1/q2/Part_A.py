class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.middle = None
        self.right = None

def max_depth(root):
    if root is None:
        return 0

    left_depth = max_depth(root.left)
    middle_depth = max_depth(root.middle)
    right_depth = max_depth(root.right)

    return max(left_depth, middle_depth, right_depth) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.middle = TreeNode(3)
root.right = TreeNode(4)
root.left.left = TreeNode(5)

result = max_depth(root)
print("Maximum Depth of the Ternary Tree:", result)