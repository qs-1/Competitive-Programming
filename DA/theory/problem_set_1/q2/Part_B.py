class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.middle = None
        self.right = None

def is_balanced(root):
    def check_height_and_balance(node):
        if node is None:
            return 0, True

        left_height, left_balance = check_height_and_balance(node.left)
        middle_height, middle_balance = check_height_and_balance(node.middle)
        right_height, right_balance = check_height_and_balance(node.right)

        heights = [left_height, middle_height, right_height]
        current_height = max(heights) + 1
        
        current_balance = (max(heights) - min(heights)) <= 1

        is_tree_balanced = current_balance and left_balance and middle_balance and right_balance

        return current_height, is_tree_balanced

    _, result = check_height_and_balance(root)
    return result


t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.middle = TreeNode(3)
t1.right = TreeNode(4)
t1.left.left = TreeNode(5)

is_tree_balanced = is_balanced(t1)
print("Is the ternary tree balanced?", is_tree_balanced)

t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.middle = TreeNode(3)
t2.right = TreeNode(4)
t2.left.left = TreeNode(5)
t2.left.left.left = TreeNode(6)

is_tree_unbalanced = is_balanced(t2)
print("Is the ternary tree balanced?", is_tree_unbalanced)